# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:01:01 2023

@author: jasee
"""

from PIL import Image
from pytesseract import pytesseract
# Define path to tesseract.exe
path_to_tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#define path to image
path_to_image=r'C:\Users\jasee\OneDrive\Desktop\image to text\best.png'
# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd=path_to_tesseract
# Open image with PIL
img=Image.open(path_to_image)
#Extract text from image
text=pytesseract.image_to_string(img)
print(text)
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak(text)