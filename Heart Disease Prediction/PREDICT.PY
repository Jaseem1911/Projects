import numpy as np
from tensorflow.keras.models import load_model

class heart_disease_predictor:
    def __init__(self,attributes):
        self.attributes=attributes

    def prediction(self):
        # load model
        model=load_model('heart.h5')

        #model.summary()
        attributes=self.attributes

        result=model.predict(attributes)
        print(result)
        if result < 2.45:
            prediction = 'Severe'
            print(prediction)
        else:
            prediction= 'Normal'
            print(prediction)
val=[[71,0,1,160,302,0,1,162,0,0.4,2,2,2]]

a=heart_disease_predictor(val)
a.prediction()