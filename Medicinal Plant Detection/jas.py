
from app import app
from flask import Flask, render_template, request, redirect, url_for, flash

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"



import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Flatten,Dense,Conv3D,MaxPool3D
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.losses import SparseCategoricalCrossetropy
# # from keras.models import load_modelmodel=load_model('heart.h5')

from tensorflow.keras.preprocessing import image
import sys 
sys.path.append('..')
prediction=""

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/upload_pic',methods=['POST'])
def upload_pic(): 


    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url) 
    file=request.files['file']
    if file.filename=='':
        flash('No image selected for uploading')
        return redirect(request.url) 
    else:
        filename=secure_filename(file.filename) 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        y=('static/'+filename)
        print(y)

    def test(a):
        a="hello"
        print(a)
if __name__=='__main__':
    app.run(debug=True)