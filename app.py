from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
from inference import predict
import glob
app = Flask(__name__)
Bootstrap(app)

app.config["UPLOAD_PATH"] = 'static'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dir = app.config["UPLOAD_PATH"]
        for zippath in glob.iglob(os.path.join(dir, '*.png')):
            os.remove(zippath)
        #text = request.form['text']
        # remove static directory if it exists
        #for zippath in glob.glob(os.path.join(dir, '*.png')):
         #       os.remove(zippath)
        text = request.form['text']        
        name, img, path = predict(text)
        #result = { 'mol_name':name,'mol_path':img,'pathway_path':path}
        img.save(os.path.join('static', 'molecule1.png'))
        path.save(os.path.join('static', 'pathway1.png'))

        result = {
            
        'mol_name': name,
         #'mol_path': 'kya',
        'mol_path': os.path.join('static', 'molecule1.png'),
        'pathway_path': os.path.join('static', 'pathway1.png')
        }
        return render_template('show.html', result=result)
    return render_template('index.html')  # by default it will look in templates folder
if __name__ == '__main__':
    app.run(debug=True)
