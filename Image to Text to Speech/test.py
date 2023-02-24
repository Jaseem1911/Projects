from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from PIL import Image
from pytesseract import pytesseract
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('image_to_text_to_speech.html')
@app.route('/predict', methods=['POST'])

def predict():
    name=(request.values['lang'])
    # path="static/uploads/"+name
    print(name)
   
    return render_template('image_to_text_to_speech.html',prediction_text="text")
if __name__=='__main__':
    app.run(port=8000)
