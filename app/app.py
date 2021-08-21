from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config as cfg
import os

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

if __name__ == '__main__':
    app.run(debug=True)