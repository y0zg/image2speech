## Image to Text-to-Speech Converter
This tool extracts text from images and converts it into speech. It leverages Tesseract for Optical Character Recognition (OCR) and Google Text-to-Speech (gTTS) for converting the extracted text into audio.

## Environment Setup
### Install Dependencies
1. Set up the virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Tesseract Setup
1. Install Tesseract:

macOS (Homebrew):
```bash
brew install tesseract
```

Linux (APT):
```bash
sudo apt install tesseract-ocr
```

Windows: Download and install from here https://github.com/tesseract-ocr/tesseract.

2. Download required Language Data: (In my case I use Ukrainian language) `ukr.traineddata` from here https://github.com/tesseract-ocr/tessdata/blob/main/ukr.traineddata and place it in the `tessdata` directory:

    - Linux: `/usr/share/tesseract-ocr/4.00/tessdata/` 
    - macOS: `/opt/homebrew/share/tessdata/`
    - Windows: `C:\Program Files\Tesseract-OCR\tessdata\` 

3. Set TESSDATA_PREFIX:

```bash
export TESSDATA_PREFIX=/path/to/tessdata_directory
```

### Running the Script
1. Place your images in a folder, e.g., `img/`.

2. Update the list of image files in the script or set the folder path.
 
3. Run the script:

```bash
python text2voice.py
```


### Important Notes
Ensure that Tesseract is installed and that the required language data is available.
The script was tested with image formats `.jpg` and `.png`.