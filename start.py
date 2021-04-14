import os
import pandas
import pm4py
from flask import Flask, request, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)			
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def home():
    return "Hallo World"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():
    return make_response(jsonify(results()))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if file:
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))   
      return render_template("success.html")

  return render_template("upload.html")
   









def results():
    result = "This is a result"
    return {
  "fulfillmentMessages": [
    {
      "card": {
        "title": "Upload File",
        "buttons": [
          {
            "text": "Upload here",
            "postback": "https://processminingbot.herokuapp.com/upload"
          }
        ]
      }
    }
  ]
}


if __name__ == "__main__":
    app.run(debug=True)	

