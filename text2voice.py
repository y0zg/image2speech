from PIL import Image
import pytesseract
from gtts import gTTS
import os

def extract_text_from_images(image_paths):
    full_text = ""
    
    for image_path in image_paths:
        try:
            img = Image.open(image_path).convert('RGB')
            text = pytesseract.image_to_string(img, lang='ukr')
            full_text += text + "\n"
        except (IOError, SyntaxError, TypeError) as e:
            print(f"Error processing image {image_path}: {e}")
    
    return full_text

def text_to_speech(text, output_audio_path):
    tts = gTTS(text, lang='uk')
    tts.save(output_audio_path)
    print(f"Audio saved to {output_audio_path}")

image_folder = 'img/'
output_audio_path = 'output_audio.mp3'

# List of image files in the desired order
## TODO: refactor
image_files = ['PXL_20240914_115518618~2.jpg',
               'PXL_20240914_115530708~2.jpg', 
               'PXL_20240914_115540457~2.jpg',
               'PXL_20240914_115554186~2.jpg', 
               'PXL_20240914_115607745~2.jpg', 
               'PXL_20240914_115626587~2.jpg',
               'PXL_20240914_115634159~2.jpg',
               'PXL_20240914_115655802~2.jpg',
               'PXL_20240914_115703191~2.jpg',
               'PXL_20240914_115713447~2.jpg',
               'PXL_20240914_115722112~2.jpg',
               'PXL_20240914_115802320~2.jpg',
               'PXL_20240914_115811127.MP~2.jpg',
               'PXL_20240914_115820952~2.jpg'  ]
image_paths = [os.path.join(image_folder, file) for file in image_files]

extracted_text = extract_text_from_images(image_paths)
print("Extracted Text: \n", extracted_text)

text_to_speech(extracted_text, output_audio_path)
