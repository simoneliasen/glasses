from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)


	
		

# @app.route("/", methods=['GET', 'POST'])
# def process_img():
#     form = Upload_Pics_Form()
#     if form.validate_on_submit():
#         if form.pic.data:
#             images_to_process = save_pictures(form.pic.data)
#             processed_images = process_images(images_to_process) 
#         return render_template('index.html', images=processed_images)
#     elif request.method == 'GET' and not form.pic.data:
#       return render_template('index.html', form=form)





    
