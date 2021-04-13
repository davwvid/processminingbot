import pandas
import pm4py
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)			

@app.route('/')
@app.route('/home')
def home():
    return "Hallo World"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():
    return make_response(jsonify(results()))

def results():
    result = "This is a result"
    return {
  "fulfillmentMessages": [
    {
      "card": {
        "title": "card title",
        "subtitle": "card text",
        "imageUri": "https://example.com/images/example.png",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://example.com/path/for/end-user/to/follow"
          }
        ]
      }
    }
  ]
}


if __name__ == "__main__":
    app.run()	
