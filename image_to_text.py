import pytesseract
import os
from PIL import Image


#Path to tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_text():
    img = Image.open("img.jpg")
    text = pytesseract.image_to_string(img)
    print(text) 


image_to_text()
