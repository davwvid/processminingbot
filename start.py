import pandas
import pm4py
import flask
import os
import jsonify
import make_response
import request

app = flask.Flask(__name__)			

@app.route('/')
@app.route('/home')
def home():
    return "Hallo World"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook ():
    return make_response(jsonify(results()))

def results():
    return {'fulfillmentText': 'test'}


if __name__ == "__main__":
    app.run()	

    
def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';')
    num_events = len(event_log)
    num_cases = len(event_log.CaseID.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))


def import_xes(file_path):
    event_log = pm4py.read_xes(file_path)
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

def showBPMN(file_path):
    log = pm4py.read_xes(file_path)
    process_tree = pm4py.discover_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)
  