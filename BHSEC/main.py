import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = './BHSEC/Uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/',methods=["POST","GET"])
def files():
    if request.method == "POST":
        output_type = request.form.get('output_type')
        data_file = request.files['data_file']
        if data_file:
            filename = data_file.filename
            data_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "<h1>Thank You for using our service</h1>"


        
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True, port=6969)