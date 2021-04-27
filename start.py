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
    return {
  "payload": {
    "google": {
      "expectUserResponse": true,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "Here's an example of a basic card."
            }
          },
          {
            "basicCard": {
              "title": "Title: this is a title",
              "subtitle": "This is a subtitle",
              "formattedText": "This is a basic card.  Text in a basic card can include \"quotes\" and\n    most other unicode characters including emojis.  Basic cards also support\n    some markdown formatting like *emphasis* or _italics_, **strong** or\n    __bold__, and ***bold itallic*** or ___strong emphasis___ as well as other\n    things like line  \nbreaks",
              "image": {
                "url": "https://storage.googleapis.com/actionsresources/logo_assistant_2x_64dp.png",
                "accessibilityText": "Image alternate text"
              },
              "buttons": [
                {
                  "title": "This is a button",
                  "openUrlAction": {
                    "url": "https://assistant.google.com/"
                  }
                }
              ],
              "imageDisplayOptions": "CROPPED"
            }
          },
          {
            "simpleResponse": {
              "textToSpeech": "Which response would you like to see next?"
            }
          }
        ]
      }
    }
  }
}


if __name__ == "__main__":
    app.run(debug=True)	

