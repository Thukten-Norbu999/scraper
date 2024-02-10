import os, random
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


from scrapper import ScraperB


new = ScraperB(False)



def shoot(name):
    if (os.path.exists(f"{UPLOAD_FOLDER}{name}")):
        li = new.getdata(f'{UPLOAD_FOLDER}{name}')
        vals = []
        if not(new.individual):
            for i in range(len(li)):
                vals.append(new.scrape(li[i][0], li[i][1]))
        new.create_output(vals, name+"output")
    else:
        return "DOCUMENT NOT FOUND"
app = Flask(__name__)
UPLOAD_FOLDER = './BHSEC/Uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/',methods=["POST","GET"])
def files():
    if request.method == "POST":
        output_type = request.form.get('output_type')
        data_file = request.files['data_file']
        if data_file:
            new.individual = False
            filename = data_file.filename
            data_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if (os.path.exists(f"{UPLOAD_FOLDER}{filename}")):
                shoot(filename)
        
            return "<h1>Thank You for using our service</h1>"


        
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True, port=6969)