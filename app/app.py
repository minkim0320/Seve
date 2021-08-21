from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config as cfg
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cfg.paths["google_api_name"]

client = vision.ImageAnnotatorClient()

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = cfg.paths["image_path"]

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']

            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))

            print('Image saved')

            return redirect(request.url)

    return render_template('upload_image.html')

@app.route('/home', methods=['GET', 'POST'])
def send_request():

    file_name = 'design-screenshot.png'
    folder_path = cfg.paths["image_path"]

    with io.open(os.path.join(folder_path,file_name),'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # print(response)

    df = pd.DataFrame(columns=['locale','description'])
    for text in texts:
        df = df.append(
            dict(locale=text.locale,description=text.description),
            ignore_index=True
        )
    print(df)
    return render_template('upload_image.html')

@app.route('/test', methods=['GET'])
def json_response():
    hackathons = {
        "Hackthe6ix": "2021"
    }
    return hackathons


if __name__ == '__main__':
    app.run(debug=True)