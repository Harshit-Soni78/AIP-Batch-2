import subprocess
import sys

def install_packages():
    # All packages including commented ones
    packages = [
        # OCR and image processing
        "opencv-python==4.8.0.76",
        "pytesseract==0.3.10",
        "pdf2image==1.16.3",
        "Pillow==10.0.0",
        
        # NLP and text processing
        "transformers==4.30.2",
        "torch==2.0.1",  # Uncommented
        "spacy==3.6.0",  # Uncommented
        "nltk==3.8.1",
        "langid==1.1.6",
        
        # Translation
        "googletrans==4.0.0-rc1",
        "deep-translator==1.11.1",
        
        # Legal analysis
        "textblob==0.17.1",
        
        # Barcode/QR scanning
        "pyzbar==0.1.9",
        
        # Plagiarism detection
        "scikit-learn==1.3.0",  # Uncommented
        "python-Levenshtein==0.21.0",  # Uncommented
    ]
    
    # First upgrade pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    # Install packages with special handling for problematic ones
    for package in packages:
        try:
            if package.startswith("tokenizers") or package.startswith("spacy"):
                # Use pre-built wheels for packages needing Rust
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--only-binary=:all:", package])
            elif package.startswith("scikit-learn") or package.startswith("python-Levenshtein"):
                # Use conda-forge for better compatibility
                try:
                    subprocess.check_call(["conda", "install", "-c", "conda-forge", package.split("==")[0]])
                except:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            print("Trying alternative installation method...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-deps", package])
                print(f"Installed {package} without dependencies")
            except:
                print(f"Could not install {package} with any method")

if __name__ == "__main__":
    install_packages()
    print("Installation process completed!")