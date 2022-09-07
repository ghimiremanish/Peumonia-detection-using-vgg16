from flask import render_template, request, jsonify
from app import app
import os
# import numpy as np
import datetime
# from keras.models import load_model
# from keras.preprocessing import image
# from PIL import Image
# from werkzeug.utils import secure_filename

# MODEL_PATH = 'models/model.h5'

#Load your trained model
# model = load_model(MODEL_PATH)

# def model_predict(img_path, model):
#    img = image.load_img(img_path, target_size=(64, 64)) #target_size must agree with what the trained model expects!!

   # Preprocessing the image
   # img = image.img_to_array(img)
   # img = np.expand_dims(img, axis=0)
   # preds = model.predict(img)
   # return preds

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

# @app.route('/predict', methods=['POST'])
# def predict():
   # Get the file from post request
   # f = request.files['image']

   # # Save the file to ./uploads
   # basepath = os.path.dirname(__file__)
   # file_path = os.path.join(
   #    basepath, 'uploads', secure_filename(str(datetime.datetime.today())+f.filename))
   # f.save(file_path)

   # # Make prediction
   # # preds = model_predict(file_path, model)

   # data = ''

   # if preds == 0:
   #    data = 'Normal'
   # else:
   #    data = 'Pneumonia'

   # tasks = [
   #    {
   #       'result':data
   #    }
   # ]
   # return jsonify(tasks)
