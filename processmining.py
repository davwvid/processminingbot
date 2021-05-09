import pm4py


def mining(file, miner, view):
    
    if file == "1":
      log = pm4py.read_xes('assets\running-example.xes')
    else:
       log = pm4py.read_xes('assets\running-example-just-two.cases.xes')
    
    petri_net, initial_marking, final_marking = discoverProcess(miner, log)
    return visualizeProcess(view, petri_net, initial_marking, final_marking)

def discoverProcess(miner, log):

  if miner == "Alpha":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)

  if miner == "Alpha+":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_alpha_plus(log)

  if miner == "Heuristic":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_heuristics(log)

  if miner == "Inductive":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)

  return petri_net, initial_marking, final_marking

def visualizeProcess(view, petri_net, initial_marking, final_marking):

  if view == "Heuristics net":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)

  if view == "Petri net":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_alpha_plus(log)

  if view == "Process tree":
    petri_net, initial_marking, final_marking = pm4py.discover_petri_net_heuristics(log)

  if view == "BPMN":
    process = pm4py.view_petri_net(petri_net, initial_marking, final_marking, format='png')

  return process