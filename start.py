import pandas
import pm4py
import flask
import os
import jsonify
import make_response

app = flask.Flask(__name__)			

@app.route('/')
@app.route('/home')
def home():
    return "Hallo World"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():
    return "test"
    #return make_response(jsonify(results()))

def results():

    result = "This is a result"

    return {'fulfillmentText': result}


if __name__ == "__main__":
    app.run()	

    