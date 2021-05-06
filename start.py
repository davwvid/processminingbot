import os
import pandas
import pm4py
from flask import Flask, request, flash, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

from json_response import text_response, fileupload_response, image_response

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
  tag = request_data["queryResult"]["intent"]["displayName"]

  if tag == "Experience - yes":
    mining()
    return make_response(jsonify(fileupload_response()))

  if tag == "DefaultSettings":
    return make_response(jsonify(image_response()))


  return make_response(jsonify(text_response("default")))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))   
      return render_template("success.html")

  return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)	

def mining():
    log = pm4py.read_xes('uploads\running-example.csv')
    process_tree = pm4py.discover_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)