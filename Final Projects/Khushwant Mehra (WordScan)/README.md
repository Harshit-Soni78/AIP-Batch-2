# WordScan

WordScan is a Python-based application designed to process document photos by enhancing the text within them. It extracts text from images and provides concise summaries, making it easier to understand and analyze the content.

## Features

- **Text Enhancement**: Improves the clarity and readability of text within document photos.
- **Text Extraction**: Utilizes Optical Character Recognition (OCR) to extract text from images.
- **Summarization**: Generates concise summaries of the extracted text for quick comprehension.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/This-is-khushwant/WordScan.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd WordScan
   ```

3. **Install Dependencies**:

   Ensure you have Python installed on your system. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Document Photo**:

   Ensure that corners of Document Photo are clearly visible.
   You can browse the directory your image is stored in from the webpage itself

2. **Run the Application**:

   Execute the main script to process the image:

   ```bash
   python WordScan.py
   ```
   
   localhost server would be generated in the terminal. Copy and paste it in your browser
   
3. **View Results**:

   The enhanced image will be saved in the `processed` directory, and the extracted text along with its summary will be displayed in the console.

## Project Structure

- `WordScan.py`: The main script that orchestrates the processing of images.
- `image_processor.py`: Handles image enhancement functions.
- `text_extractor.py`: Contains functions for OCR to extract text from images.
- `text_summarizer.py`: Provides text summarization functionalities.
- `uploads/`: Directory to store input images.
- `processed/`: Directory where processed images are saved.
- `templates/`: Contains HTML templates.

## Acknowledgments

Special thanks to all contributors and the open-source community for their invaluable resources and support.

