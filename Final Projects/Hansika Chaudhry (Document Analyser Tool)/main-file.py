import argparse
import os
from modulefinder import ocr, text_processing, legal_analysis, translation, barcode_scanner, plagiarism, recommendations

def parse_args():
    parser = argparse.ArgumentParser(description='Document Analyzer Tool')
    parser.add_argument('--input', '-i', required=True, help='Path to input document/image')
    parser.add_argument('--output', '-o', help='Path to output directory', default='./output')
    parser.add_argument('--ocr', action='store_true', help='Perform OCR on image/PDF')
    parser.add_argument('--summarize', action='store_true', help='Generate text summary')
    parser.add_argument('--legal', action='store_true', help='Perform legal clause detection')
    parser.add_argument('--translate', help='Translate document to specified language (e.g., "english")')
    parser.add_argument('--sentiment', action='store_true', help='Perform sentiment analysis')
    parser.add_argument('--barcode', action='store_true', help='Scan for barcodes/QR codes')
    parser.add_argument('--plagiarism', action='store_true', help='Check for plagiarism')
    parser.add_argument('--recommend', action='store_true', help='Generate recommendations')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    
    # Process the document based on arguments
    text_content = None
    
    # Extract text using OCR if needed
    if args.ocr or not args.input.lower().endswith(('.txt', '.doc', '.docx')):
        print("Performing OCR and smart scanning...")
        text_content = ocr.process_document(args.input)
        with open(os.path.join(args.output, 'extracted_text.txt'), 'w', encoding='utf-8') as f:
            f.write(text_content)
    else:
        # Read text directly from text documents
        with open(args.input, 'r', encoding='utf-8') as f:
            text_content = f.read()
    
    if not text_content:
        print("Failed to extract text from the document.")
        return
    
    # Perform requested analyses
    if args.summarize:
        print("Generating summary...")
        summary = text_processing.generate_summary(text_content)
        with open(os.path.join(args.output, 'summary.txt'), 'w', encoding='utf-8') as f:
            f.write(summary)
        print("Summary saved to", os.path.join(args.output, 'summary.txt'))
    
    if args.legal:
        print("Analyzing legal clauses...")
        legal_issues = legal_analysis.detect_hidden_clauses(text_content)
        with open(os.path.join(args.output, 'legal_analysis.txt'), 'w', encoding='utf-8') as f:
            f.write(legal_issues)
        print("Legal analysis saved to", os.path.join(args.output, 'legal_analysis.txt'))
    
    if args.translate:
        print(f"Translating document to {args.translate}...")
        translated_text = translation.translate_text(text_content, target_language=args.translate)
        with open(os.path.join(args.output, f'translated_{args.translate}.txt'), 'w', encoding='utf-8') as f:
            f.write(translated_text)
        print(f"Translation saved to {os.path.join(args.output, f'translated_{args.translate}.txt')}")
    
    if args.sentiment:
        print("Analyzing sentiment and tone...")
        sentiment_analysis = text_processing.analyze_sentiment(text_content)
        with open(os.path.join(args.output, 'sentiment_analysis.txt'), 'w', encoding='utf-8') as f:
            f.write(sentiment_analysis)
        print("Sentiment analysis saved to", os.path.join(args.output, 'sentiment_analysis.txt'))
    
    if args.barcode:
        print("Scanning for barcodes and QR codes...")
        barcode_data = barcode_scanner.scan_codes(args.input)
        with open(os.path.join(args.output, 'barcode_data.txt'), 'w', encoding='utf-8') as f:
            f.write(barcode_data)
        print("Barcode/QR code data saved to", os.path.join(args.output, 'barcode_data.txt'))
    
    if args.plagiarism:
        print("Checking for plagiarism...")
        plagiarism_report = plagiarism.check_plagiarism(text_content)
        with open(os.path.join(args.output, 'plagiarism_report.txt'), 'w', encoding='utf-8') as f:
            f.write(plagiarism_report)
        print("Plagiarism report saved to", os.path.join(args.output, 'plagiarism_report.txt'))
    
    if args.recommend:
        print("Generating recommendations...")
        recommendations_text = recommendations.generate_recommendations(text_content)
        with open(os.path.join(args.output, 'recommendations.txt'), 'w', encoding='utf-8') as f:
            f.write(recommendations_text)
        print("Recommendations saved to", os.path.join(args.output, 'recommendations.txt'))
    
    print("Document analysis complete!")

if __name__ == "__main__":
    main()
