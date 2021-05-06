import os
import pandas
import pm4py
from flask import Flask, request, flash, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv', 'xes'}

app = Flask(__name__)			
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():

  request_data = request.get_json()
  print(request_data.request_data['fulfillmentInfo']['tag'])

  return make_response(jsonify(results()))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))   
      return render_template("success.html")

  return render_template("upload.html")

def results():
    result = "This is a result"
    return   {"fulfillment_messages": [{
    "payload": {
      "richContent": [
    [
      {
        "type": "button",
        "icon": {},
        "text": "Upload",
        "link": "https://processminingbot.herokuapp.com/upload",
        "event": {
          "name": "",
          "languageCode": "",
          "parameters": {}
        }
      }
    ]
  ]
    }
  }]}


if __name__ == "__main__":
    app.run(debug=True)	

