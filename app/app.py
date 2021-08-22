from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import prop as cfg
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import json
from firebase import firebase

app = Flask(__name__)

# Initialize Google Cloud Configs for Vision AI
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cfg.paths["google_api_name"]
client = vision.ImageAnnotatorClient()
app.config['IMAGE_UPLOADS'] = cfg.paths["image_path"]

# Initialize Firestore
firebase = firebase.FirebaseApplication(cfg.paths["firebase_url"],None)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']

            print('Processing Image')

            image.save(os.path.join(app.config['IMAGE_UPLOADS'], 'Notes.JPG'))

            print('Image saved')

            print(request.url)
            return redirect(request.url)

    return render_template('upload_image.html')

@app.route('/home', methods=['GET', 'POST'])
def send_request():

    # file_name = 'Notes.JPG'
    # folder_path = cfg.paths["image_path"]

    # with io.open(os.path.join(folder_path,file_name),'rb') as image_file:
    #     content = image_file.read()
    
    # image = types.Image(content=content)

    # response = client.text_detection(image=image)
    # texts = response.text_annotations

    # response = jsonify({'text': response.full_text_annotation.text.split('\n')})
    # response.headers.add('Access-Control-Allow-Origin','*')
    # return response
    return jsonify({'text': 'temp'})


@app.route('/test', methods=['POST'])
def json_response():
    res = request.data
    my_json = json.loads(res)
    # print(type(my_json))
    print(my_json)

    data = {
        'Title': my_json['title'],
        'Notes': my_json['notes']
    }

    print(data['Title'])
    print(data['Notes'])

    result = firebase.post('/Notes', data)
    # print(result)
    return {}

if __name__ == '__main__':
    app.run(debug=True)