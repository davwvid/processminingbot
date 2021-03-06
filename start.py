import os
import pandas
import pm4py
from flask import Flask, request, flash, make_response, jsonify, render_template
from werkzeug.utils import secure_filename

from json_response import text_response, fileupload_response, image_response
from processmining import mining

app = Flask('ProcessMiningBot', static_url_path='/assets', static_folder='assets')			

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():

  request_data = request.get_json()

  tag = request_data["fulfillmentInfo"]["tag"]
  number = request_data["sessionInfo"]["parameters"]["number"]
  algorithm = request_data["sessionInfo"]["parameters"]["algorithm"]
  visualization = request_data["sessionInfo"]["parameters"]["visualization"]

  if tag == "startmining":
    mining(number, algorithm, visualization)
    return make_response(jsonify(text_response("success")))

  return make_response(jsonify(text_response("error")))

if __name__ == "__main__":
    app.run(debug=True)	