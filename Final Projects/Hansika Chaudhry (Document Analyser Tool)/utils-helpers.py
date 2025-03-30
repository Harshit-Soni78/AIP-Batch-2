import os
import re
import json
import datetime

def create_output_directory(path):
    """Create output directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def sanitize_filename(filename):
    """Remove invalid characters from filenames."""
    # Remove invalid characters
    sanitized = re.sub(r'[\\/*?:"<>|]', "", filename)
    # Replace spaces with underscores
    sanitized = sanitized.replace(' ', '_')
    return sanitized

def get_timestamp():
    """Get current timestamp in a filename-friendly format."""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def save_json_data(data, output_path, filename=None):
    """Save dictionary data as JSON file."""
    if filename is None:
        filename = f"data_{get_timestamp()}.json"
    
    filepath = os.path.join(output_path, sanitize_filename(filename))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    return filepath

def load_json_data(filepath):
    """Load JSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def print_progress(current, total, bar_length=50):
    """Display a progress bar."""
    percent = float(current) * 100 / total
    arrow = '-' * int(percent/100 * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    
    print(f'\rProgress: [{arrow}{spaces}] {percent:.2f}%', end='')
    
    if current == total:
        print()  # New line after completion

def extract_file_extension(filename):
    """Extract file extension from filename."""
    return os.path.splitext(filename)[1].lower()

def is_image_file(filename):
    """Check if file is an image based on extension."""
    ext = extract_file_extension(filename)
    return ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif']

def is_pdf_file(filename):
    """Check if file is a PDF based on extension."""
    ext = extract_file_extension(filename)
    return ext == '.pdf'

def is_text_file(filename):
    """Check if file is a text document based on extension."""
    ext = extract_file_extension(filename)
    return ext in ['.txt', '.doc', '.docx', '.rtf', '.md', '.html', '.htm']

def truncate_text(text, max_length=100, add_ellipsis=True):
    """Truncate text to maximum length."""
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length]
    if add_ellipsis:
        truncated += "..."
    
    return truncated

def word_count(text):
    """Count words in text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)
