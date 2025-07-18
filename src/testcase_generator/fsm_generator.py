from src.testcase_generator.llm_agents import FSMExtractor
from graphviz import Digraph
from transitions import Machine
from itertools import islice
import json

import logging

logger = logging.getLogger(__name__)

def extract_fsm(rfc_fsm_text_filepath):

    # rfc_fsm_text_filepath = "data/raw_documents/RFC_FSMs/rfc_2328_10.txt"
    with open(rfc_fsm_text_filepath, "r") as f:
        rfc_fsm_text = f.read()
    fsm_extractor = FSMExtractor()
    fsm_json = fsm_extractor.extract_fsm(rfc_fsm_text)

    with open(rfc_fsm_text_filepath.replace(".txt", "_fsm.txt")) as f:
        fsm_text = f.read()
    while True:
        try:
            supplemented_fsm_json = fsm_extractor.supplement_fsm(fsm_text, fsm_json)
            if json.loads(supplemented_fsm_json):
                fsm_json = supplemented_fsm_json
            else:
                break
        except json.JSONDecodeError:
            logger.warning("FSM supplement failed")
            continue

    logger.info(fsm_json)
    return fsm_json
    
def visualize_fsm_with_wildcards(fsm_data, output_filename="fsm"):
    """ Visualize FSM with wildcards """
    dot = Digraph(comment='OSPF FSM (With Wildcards)')
    
    # Add state nodes
    for state in fsm_data["states"]:
        dot.node(state)

    # Add transition edges (special handling for wildcards)
    for trans in fsm_data["transitions"]:
        if trans["from_state"] == "*":
            # Global transitions are represented by red dashed lines
            for state in fsm_data["states"]:
                if state != trans["to_state"]:  # Avoid self-loop repetition
                    dot.edge(state, trans["to_state"], label=trans["event"], 
                            style="dashed", color="red")
        else:
            # Regular transitions
            dot.edge(trans["from_state"], trans["to_state"], 
                    # label=f"{trans['event']}\n{'/'.join(trans['actions'])}")
                    label=trans['event'])
    
    dot.render(output_filename, view=False, format="png")

    return dot


def simulate_fsm(fsm_data: dict):
    """ Simulate FSM using pytransitions and traverse paths """
    class OSPFNeighbor:
        pass

    # Initialize state machine
    neighbor = OSPFNeighbor()
    machine = Machine(
        model=neighbor,
        states=fsm_data["states"],
        initial="Down",
        auto_transitions=False
    )

    # Dynamically add transition rules
    for trans in fsm_data["transitions"]:
        machine.add_transition(
            trigger=trans["event"],
            source=trans["from_state"],
            dest=trans["to_state"],
            before=lambda: logger.info(f"Executing actions: {trans['actions']}")
        )

    # Depth-first traversal of all paths (limit depth to prevent infinite loops)
    def dfs_paths(state, path=None, max_depth=10):
        path = path or []
        if len(path) >= max_depth:
            yield path
            return
        for trans in fsm_data["transitions"]:
            if trans["from_state"] == state:
                yield from dfs_paths(trans["to_state"], path + [trans["event"]], max_depth)

    # Print the first 10 path examples
    logger.info("Possible state paths:")
    for i, path in enumerate(islice(dfs_paths("Down"), 10)):
        logger.info(f"Path {i+1}: Down -> {' -> '.join(path)}")

    return neighbor

from collections import deque

def traverse_transitions(fsm_data):
    """ Smart traversal algorithm for all state transitions """
    # Initialize data structures
    verified_transitions = set()  # Verified transitions (from_state, event)
    pending_queue = deque()       # Pending transitions queue
    state_history = {}            # Reachable paths record for each state

    # Start from the initial state
    initial_state = "Down"
    pending_queue.append((initial_state, []))  # (current state, historical path)
    state_history[initial_state] = [ [] ]      # Record all paths to reach this state

    while pending_queue:
        current_state, path = pending_queue.popleft()

        # Get possible transitions from the current state (filter verified ones)
        possible_transitions = [
            t for t in fsm_data["transitions"]
            if t["from_state"] in (current_state, "*")  # Include global rules
            and (t["from_state"], t["event"]) not in verified_transitions
        ]
        
        for trans in possible_transitions:
            # Build new path (avoid reference issues)
            new_path = path + [{
                "from_state": trans["from_state"],
                "to_state": trans["to_state"],
                "event": trans["event"],
                "actions": trans["actions"]
            }]
            
            # Loop detection: Check if the new state has appeared in the current path
            if trans["to_state"] in [step["to_state"] for step in new_path[:-1]]:
                print(f"⚠️ Loop detection skipped: {trans['from_state']}--{trans['event']}->{trans['to_state']}")
                continue

            # Mark this transition as verified
            verified_transitions.add((trans["from_state"], trans["event"]))

            # Record all paths to reach the new state (keep the shortest path)
            if trans["to_state"] not in state_history or len(new_path) < len(state_history[trans["to_state"]][0]):
                state_history[trans["to_state"]] = [new_path]
            elif len(new_path) == len(state_history[trans["to_state"]][0]):
                state_history[trans["to_state"]].append(new_path)

            # Smart queue insertion: Prioritize exploring new states/short paths
            pending_queue.appendleft((trans["to_state"], new_path))  # DFS priority
            # pending_queue.append((trans["to_state"], new_path))     # BFS alternative

    return state_history, verified_transitions
