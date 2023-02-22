from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
from keras import models
from tensorflow import keras

app=Flask(__name__)
model = keras.models.load_model('heart.h5')
#model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('ann.html')
@app.route('/predict', methods=['POST'])
def predict():
    age=float(request.values['age'])
    Sex=float(request.values['Sex'])
    cp=float(request.values['cp'])
    trestbps=float(request.values['trestbps'])
    chol=float(request.values['chol'])
    fbs=float(request.values['fbs'])
    restecg=float(request.values['restecg'])
    thalach=float(request.values['thalach'])
    exang=float(request.values['exang'])
    oldpeak=float(request.values['oldpeak'])
    slope=float(request.values['slope'])
    ca=float(request.values['ca'])
    thal=float(request.values['thal'])

    data=np.array([[age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    my_prediction=model.predict(data)

    if my_prediction > 0.45:
        prediction = 'Severe'
        print(prediction)
        return render_template('result2.html')
    else:
        prediction= 'Normal'
        print(prediction)
        return render_template('result.html')
    
    
    # result = model.predict(data)
    # print(result)
   
    
if __name__=='__main__':
    app.run(port=8000)