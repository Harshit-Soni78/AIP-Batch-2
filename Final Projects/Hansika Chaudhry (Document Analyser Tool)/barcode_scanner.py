import cv2
#from pyzbar.pyzbar import decode
import json
import re

def scan_codes(image_path):
    """Scan image for barcodes and QR codes."""
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        if image is None:
            return "Error: Could not read image file."
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Scan for codes
        decoded_objects = decode(gray)
        
        if not decoded_objects:
            # Try different preprocessing if no codes found
            # Apply adaptive threshold
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)
            decoded_objects = decode(thresh)
        
        # Prepare results
        results = []
        for obj in decoded_objects:
            # Get data and type
            data = obj.data.decode("utf-8")
            code_type = obj.type
            
            # Determine data type (URL, text, etc.)
            data_type = determine_data_type(data)
            
            # Get coordinates
            points = obj.polygon
            if points:
                coords = [(p.x, p.y) for p in points]
            else:
                rect = obj.rect
                coords = [(rect.left, rect.top), (rect.left + rect.width, rect.top),
                          (rect.left + rect.width, rect.top + rect.height), 
                          (rect.left, rect.top + rect.height)]
            
            # Add to results
            results.append({
                'type': code_type,
                'data': data,
                'data_type': data_type,
                'coordinates': coords
            })
        
        # Generate report
        if not results:
            return "No barcodes or QR codes detected in the image."
        
        report = []
        report.append(f"BARCODE/QR CODE SCAN RESULTS\n")
        report.append(f"Found {len(results)} code(s) in the image:\n")
        
        for i, result in enumerate(results, 1):
            report.append(f"CODE #{i}:")
            report.append(f"  Type: {result['type']}")
            report.append(f"  Data Type: {result['data_type']}")
            report.append(f"  Data: {result['data']}")
            
            # For structured data (like JSON), try to parse and display it nicely
            if result['data_type'] == 'JSON':
                try:
                    json_data = json.loads(result['data'])
                    formatted_json = json.dumps(json_data, indent=2)
                    report.append(f"  Parsed JSON:")
                    for line in formatted_json.split('\n'):
                        report.append(f"    {line}")
                except:
                    pass
            
            report.append("")
        
        return "\n".join(report)
    
    except Exception as e:
        return f"Error scanning barcodes: {str(e)}"

def determine_data_type(data):
    """Determine the type of data encoded in the barcode/QR code."""
    # Check if it's a URL
    url_pattern = re.compile(r'^https?://\S+$')
    if url_pattern.match(data):
        return 'URL'
    
    # Check if it's JSON
    try:
        json.loads(data)
        return 'JSON'
    except:
        pass
    
    # Check if it's a vCard
    if data.startswith('BEGIN:VCARD') and data.endswith('END:VCARD'):
        return 'vCard'
    
    # Check if it's a product code (numeric only)
    if data.isdigit():
        return 'Product Code'
    
    # Default
    return 'Text'
