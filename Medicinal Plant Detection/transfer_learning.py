from tensorflow.keras.preprocessing import image
from tensorflow import keras
import numpy as np
import pandas as pd
# testing the model
model = keras.models.load_model('heart.h5')
def testing_image(image_directory):
    test_image = image.load_img(image_directory, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    result = model.predict(x= test_image)
    print(result)
    if np.argmax(result)  == 0:        
      prediction = 'Fenugreek'
    elif np.argmax(result)  == 1:
      prediction = 'Guava'
    elif np.argmax(result)  == 2:
      prediction ='Jackfruit'  
    elif np.argmax(result)  == 3:
      prediction = 'Jasmine'
    elif np.argmax(result)  == 4:
      prediction ='Lemon'
    elif np.argmax(result)  == 5:
      prediction = 'Mango'
    elif np.argmax(result)  == 6:
      prediction ='Rasna'  
    elif np.argmax(result)  == 7:
      prediction = 'Sandalwood'
    elif np.argmax(result)  == 8:
      prediction ='Tulsi'
    return prediction
print(testing_image('AH-S-002.jpg'))