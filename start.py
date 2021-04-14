import pandas
import pm4py
from flask import Flask, request, make_response, jsonify, render_template

app = Flask(__name__)			

@app.route('/')
@app.route('/home')
def home():
    return "Hallo World"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():
    return make_response(jsonify(results()))

@app.route('/upload')
def upload_file():
   return render_template("upload.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

def results():
    result = "This is a result"
    return {
  "fulfillmentMessages": [
    {
      "card": {
        "title": "card title",
        "subtitle": "card text",
        "imageUri": "https://www.promatis.ch/wp-content/uploads/sites/14/2018/07/Celonis_Process_Mining.jpg",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://www.promatis.ch/2018/06/22/process-mining-erkennen-und-verstehen-bedeutet-verbessern/"
          }
        ]
      }
    }
  ]
}


if __name__ == "__main__":
    app.run()	

