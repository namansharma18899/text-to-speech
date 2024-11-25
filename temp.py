#!/usr/bin/env python3

from PIL import Image
import pytesseract
from gtts import gTTS
import os

class ImageToAudioConverter:
    def __init__(self):
        # Verify Tesseract installation
        try:
            pytesseract.get_tesseract_version()
            print("Tesseract is properly installed")
        except:
            raise Exception("Tesseract is not installed. Please run: sudo apt-get install tesseract-ocr")

    def convert(self, image_path, output_path='output.mp3', language='eng'):
        """
        Convert image to text and then to audio
        
        Args:
            image_path (str): Path to input image
            output_path (str): Path for output audio file
            language (str): Language code (e.g., 'eng' for English)
        """
        try:
            # Check if image exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found: {image_path}")

            # Read image
            print(f"Processing image: {image_path}")
            image = Image.open(image_path)

            # Convert image to text
            print("Extracting text...")
            text = pytesseract.image_to_string(image, lang=language)
            
            if not text.strip():
                raise ValueError("No text was extracted from the image")
            
            print("\nExtracted text:")
            print("-" * 50)
            print(text)
            print("-" * 50)

            # Convert text to speech
            print("\nConverting text to speech...")
            tts = gTTS(text=text, lang=language[:2])  # gTTS uses 2-letter codes
            
            # Save audio file
            tts.save(output_path)
            print(f"Audio saved to: {output_path}")
            
            # Make the output file readable by all users
            os.chmod(output_path, 0o644)
            
            return True

        except Exception as e:
            print(f"Error: {str(e)}")
            return False

def main():
    # Create converter instance
    converter = ImageToAudioConverter()
    
    # Get input from user
    image_path = input("Enter the path to your image file: ")
    output_path = input("Enter the desired output audio path (or press Enter for 'output.mp3'): ")
    
    if not output_path:
        output_path = 'output.mp3'
    
    # Convert image to audio
    converter.convert(image_path, output_path)

if __name__ == "__main__":
    main()