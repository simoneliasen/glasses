from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
import os
import cv2
import numpy as np


#Load cascade xml
face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")

# Specifying upload folder and varous app settings
UPLOAD_FOLDER = 'images/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
    return render_template('upload.html')
	
@app.route('/result', methods = ['GET', 'POST'])
def upload_files():
    # Uploads file (user input)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        # Saves file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Loads file into OpenCv enviroment via saved file
        img = cv2.imread(f"images/{file.filename}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imwrite('static/newimage.png',img)
        cv2.destroyAllWindows()
        return render_template('result.html')
		
if __name__ == '__main__':
    app.run(debug = True)




    
