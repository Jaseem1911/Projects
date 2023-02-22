# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iQsBAd_c4AOaV8Rs2nFVD8pQ63Aeqbm2
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from sklearn.preprocessing import StandardScaler
dataset=pd.read_csv('/content/drive/MyDrive/heart (1).csv')

# StandardScaler= StandardScaler()
# Columns_to_scale=['age','trestbps','chol','thalach','oldpeak']
# dataset[column_to_scale]=StandardScaler.fit_transform(dataset[columns_to_scale])
X=dataset.iloc[:,0:13]
y=dataset.iloc[:,13:14]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout

# Creating a pipeline
model=Sequential()

# 1st hidden layer with input layer
model.add(Dense(units=145,activation='relu',input_dim=13))

# 2nd hidden layer
model.add(Dense(units=120,activation='relu',))

# 3rd hidden layer
model.add(Dense(units=70,activation='relu',))

# output layer
model.add(Dense(units=1,activation='sigmoid'))

model.summary()
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model_his=model.fit(X_train,y_train,validation_split=0.30, batch_size=55,epochs=25,verbose=1)

y_pred=model.predict(X_test)
y_pred=(y_pred > 0.45)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)
print(score)

from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(y_test,y_pred)
print(cm)

print(classification_report(y_test,y_pred))

model.save('heart.h5')

model.predict(X_test)

