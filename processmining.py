import pm4py

if __name__ == '__main__':
    main()

def main():
    log = pm4py.csv('uploads\running-example.csv')
    process_tree = pm4py.discover_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)