from flask import render_template, request, jsonify, flash
from app import app
import os
import numpy as np
import datetime
from keras.models import load_model
from PIL import Image
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array

MODEL_PATH = 'app/models/model.h5'

#Load your trained model
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
   print("Predict model enterd==========>")
   img = load_img(img_path, target_size=(64, 64)) #target_size must agree with what the trained model expects!!
   print("loaded img==========>")
   # Preprocessing the image
   img = img_to_array(img)
   print("Image to Array==========>")
   img = np.expand_dims(img, axis=0)
   print("NP==========>")
   preds = model.predict(img)
   print("Predict==========>")
   return preds

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
   print("Predict function==========>")
   # check if the post request has the file part
   if 'file' not in request.files:
      return "Please Attache Image File"
   else:
      print("File Found==========>")
      f = request.files['file']
      # Save the file to ./uploads
      basepath = os.path.dirname(__file__)
      file_path = os.path.join(
         basepath, 'uploads', secure_filename(str(datetime.datetime.today())+f.filename))
      f.save(file_path)
      print("image saved==========>")
      # Make prediction
      preds = model_predict(file_path, model)

      print("Predict done==========>")
      data = ''
      if preds == 0:
         data = 'Normal'
      else:
         data = 'Pneumonia'

      tasks = [
         {
            'result':data
         }
      ]
      return jsonify(tasks)