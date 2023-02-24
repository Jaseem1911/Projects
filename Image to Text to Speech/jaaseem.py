from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from PIL import Image
from pytesseract import pytesseract
from translate import Translator
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('image_to_text_to_speech.html')
@app.route('/predict', methods=['POST'])

def predict():
    name=(request.values['file'])
    lang=(request.values['lang'])
    path="static/uploads/"+name
    
    # Define path to tesseract.exe
    path_to_tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #define path to image
    path_to_image=path
    # Point tesseract_cmd to tesseract.exe
    pytesseract.tesseract_cmd=path_to_tesseract
    # Open image with PIL
    img=Image.open(path_to_image)
    #Extract text from image
    text=pytesseract.image_to_string(img)
    translator= Translator(to_lang=lang)
    translation = translator.translate(text)
    print(text)
    # print(translation)
    return render_template('image_to_text_to_speech.html',translate=translation,prediction_text=text)
if __name__=='__main__':
    app.run(port=8000)
