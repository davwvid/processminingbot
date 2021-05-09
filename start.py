import os
import pandas
import pm4py
from flask import Flask, request, flash, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

from json_response import text_response, fileupload_response, image_response

app = Flask('ProcessMiningBot', static_url_path='/assets', static_folder='assets')			

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():

  request_data = request.get_json()
  print(request)
  #tag = request_data["queryResult"]["intent"]["displayName"]

  if tag == "Experience - yes":
    mining()
    return make_response(jsonify(fileupload_response()))

  if tag == "DefaultSettings":
    return make_response(jsonify(image_response()))


  return make_response(jsonify(text_response("default")))

if __name__ == "__main__":
    app.run(debug=True)	