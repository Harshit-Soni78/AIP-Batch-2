import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import os
import threading
import sys
import argparse

import pytesseract
from PIL import Image
import text_processing
import legal_analysis
import translation
#import barcode_scanner
import plagiarism
#import recommendations

class DocumentAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Analyzer Tool")
        self.root.geometry("900x700")
        
        self.input_file = ""
        self.output_dir = "./output"
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # File selection section
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
        file_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(file_frame, text="Input Document:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.input_path_var = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.input_path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_input).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(file_frame, text="Output Directory:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.output_path_var = tk.StringVar(value=self.output_dir)
        ttk.Entry(file_frame, textvariable=self.output_path_var, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)
        
        # Analysis options section
        options_frame = ttk.LabelFrame(main_frame, text="Analysis Options", padding="10")
        options_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create variables for checkboxes
        self.ocr_var = tk.BooleanVar(value=False)
        self.summarize_var = tk.BooleanVar(value=False)
        self.legal_var = tk.BooleanVar(value=False)
        self.sentiment_var = tk.BooleanVar(value=False)
        self.barcode_var = tk.BooleanVar(value=False)
        self.plagiarism_var = tk.BooleanVar(value=False)
        self.recommend_var = tk.BooleanVar(value=False)
        
        # First row of options
        ttk.Checkbutton(options_frame, text="OCR (Extract Text)", variable=self.ocr_var).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Summarize", variable=self.summarize_var).grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Legal Analysis", variable=self.legal_var).grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Second row of options
        ttk.Checkbutton(options_frame, text="Sentiment Analysis", variable=self.sentiment_var).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Scan Barcodes/QR", variable=self.barcode_var).grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Check Plagiarism", variable=self.plagiarism_var).grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Third row with translation and recommendation
        ttk.Checkbutton(options_frame, text="Generate Recommendations", variable=self.recommend_var).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(options_frame, text="Translate to:").grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.translate_var = tk.StringVar()
        translate_combo = ttk.Combobox(options_frame, textvariable=self.translate_var, width=15)
        translate_combo['values'] = ('', 'english', 'spanish', 'french', 'german', 'chinese', 'japanese', 'russian')
        translate_combo.current(0)
        translate_combo.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=5, pady=10)
        
        ttk.Button(button_frame, text="Run Analysis", command=self.run_analysis, style="Accent.TButton").pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Clear Output", command=self.clear_output).pack(side=tk.RIGHT, padx=5)
        
        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Output Log", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configure a custom style for the run button
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 10, "bold"))
        
        # Redirect stdout to the text widget
        self.redirect_stdout()
    
    def redirect_stdout(self):
        """Redirect stdout to the text widget"""
        class TextRedirector:
            def __init__(self, text_widget):
                self.text_widget = text_widget
                self.buffer = ""
                
            def write(self, string):
                self.buffer += string
                self.text_widget.insert(tk.END, string)
                self.text_widget.see(tk.END)
                
            def flush(self):
                pass
        
        sys.stdout = TextRedirector(self.output_text)
    
    def browse_input(self):
        """Open file dialog to select input file"""
        filename = filedialog.askopenfilename(
            title="Select Input Document",
            filetypes=[
                ("All Supported Files", "*.pdf *.jpg *.jpeg *.png *.txt *.doc *.docx"),
                ("PDF Files", "*.pdf"),
                ("Image Files", "*.jpg *.jpeg *.png"),
                ("Text Files", "*.txt"),
                ("Word Documents", "*.doc *.docx"),
                ("All Files", "*.*")
            ]
        )
        if filename:
            self.input_path_var.set(filename)
            self.input_file = filename
    
    def browse_output(self):
        """Open directory dialog to select output directory"""
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_path_var.set(directory)
            self.output_dir = directory
    
    def clear_output(self):
        """Clear the output text widget"""
        self.output_text.delete(1.0, tk.END)
    
    def run_analysis(self):
        """Run the document analysis based on selected options"""
        if not self.input_path_var.get():
            self.output_text.insert(tk.END, "Error: No input file selected!\n")
            return
        
        # Disable the run button during analysis
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button) and widget['text'] == "Run Analysis":
                widget.configure(state=tk.DISABLED)
        
        self.status_var.set("Processing...")
        
        # Start analysis in a separate thread to keep GUI responsive
        analysis_thread = threading.Thread(target=self.perform_analysis)
        analysis_thread.daemon = True
        analysis_thread.start()
    
    def perform_analysis(self):
        """Perform the actual document analysis"""
        try:
            # Create output directory if it doesn't exist
            output_dir = self.output_path_var.get()
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            input_file = self.input_path_var.get()
            
            # Process the document based on selected options
            text_content = None
            
            # Extract text using OCR if needed
            if self.ocr_var.get() or not input_file.lower().endswith(('.txt', '.doc', '.docx')):
                print("Performing OCR and smart scanning...")
                text_content = ocr.process_document(input_file)
                with open(os.path.join(output_dir, 'extracted_text.txt'), 'w', encoding='utf-8') as f:
                    f.write(text_content)
                print("Text extraction complete. Saved to", os.path.join(output_dir, 'extracted_text.txt'))
            else:
                # Read text directly from text documents
                with open(input_file, 'r', encoding='utf-8') as f:
                    text_content = f.read()
                print("Text loaded from document.")
            
            if not text_content:
                print("Failed to extract text from the document.")
                return
            
            # Perform requested analyses
            if self.summarize_var.get():
                print("Generating summary...")
                summary = text_processing.generate_summary(text_content)
                with open(os.path.join(output_dir, 'summary.txt'), 'w', encoding='utf-8') as f:
                    f.write(summary)
                print("Summary saved to", os.path.join(output_dir, 'summary.txt'))
            
            if self.legal_var.get():
                print("Analyzing legal clauses...")
                legal_issues = legal_analysis.detect_hidden_clauses(text_content)
                with open(os.path.join(output_dir, 'legal_analysis.txt'), 'w', encoding='utf-8') as f:
                    f.write(legal_issues)
                print("Legal analysis saved to", os.path.join(output_dir, 'legal_analysis.txt'))
            
            if self.translate_var.get():
                target_language = self.translate_var.get()
                print(f"Translating document to {target_language}...")
                translated_text = translation.translate_text(text_content, target_language=target_language)
                with open(os.path.join(output_dir, f'translated_{target_language}.txt'), 'w', encoding='utf-8') as f:
                    f.write(translated_text)
                print(f"Translation saved to {os.path.join(output_dir, f'translated_{target_language}.txt')}")
            
            if self.sentiment_var.get():
                print("Analyzing sentiment and tone...")
                sentiment_analysis = text_processing.analyze_sentiment(text_content)
                with open(os.path.join(output_dir, 'sentiment_analysis.txt'), 'w', encoding='utf-8') as f:
                    f.write(sentiment_analysis)
                print("Sentiment analysis saved to", os.path.join(output_dir, 'sentiment_analysis.txt'))
            
            if self.barcode_var.get():
                print("Scanning for barcodes and QR codes...")
                barcode_data = barcode_scanner.scan_codes(input_file)
                with open(os.path.join(output_dir, 'barcode_data.txt'), 'w', encoding='utf-8') as f:
                    f.write(barcode_data)
                print("Barcode/QR code data saved to", os.path.join(output_dir, 'barcode_data.txt'))
            
            if self.plagiarism_var.get():
                print("Checking for plagiarism...")
                plagiarism_report = plagiarism.check_plagiarism(text_content)
                with open(os.path.join(output_dir, 'plagiarism_report.txt'), 'w', encoding='utf-8') as f:
                    f.write(plagiarism_report)
                print("Plagiarism report saved to", os.path.join(output_dir, 'plagiarism_report.txt'))
            
            if self.recommend_var.get():
                print("Generating recommendations...")
                recommendations_text = recommendations.generate_recommendations(text_content)
                with open(os.path.join(output_dir, 'recommendations.txt'), 'w', encoding='utf-8') as f:
                    f.write(recommendations_text)
                print("Recommendations saved to", os.path.join(output_dir, 'recommendations.txt'))
            
            print("Document analysis complete!")
            
            # Update status
            self.root.after(0, lambda: self.status_var.set("Analysis completed"))
            
        except Exception as e:
            print(f"Error during analysis: {str(e)}")
            self.root.after(0, lambda: self.status_var.set("Error occurred"))
        
        # Re-enable the run button
        self.root.after(0, self.enable_run_button)
    
    def enable_run_button(self):
        """Re-enable the run button after analysis is complete"""
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Frame):
                        for button in child.winfo_children():
                            if isinstance(button, ttk.Button) and button['text'] == "Run Analysis":
                                button.configure(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = DocumentAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()