from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def greeting():
    
#    return "<h1 style='color:green'>Hello World!</h1>"


@app.route("/", methods=['GET', 'POST'])
def process_img():
    form = Upload_Pics_Form()
    if form.validate_on_submit():
        if form.pic.data:
            images_to_process = save_pictures(form.pic.data)
            processed_images = process_images(images_to_process) 
        return render_template('index.html', images=processed_images)
    elif request.method == 'GET' and not form.pic.data:
      return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(host='0.0.0.0')


    