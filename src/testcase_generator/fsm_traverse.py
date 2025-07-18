import json
import logging

logger = logging.getLogger(__name__)

# Depth-first search, record the traversed state transitions
# Termination condition: A cycle is formed (the current state has appeared in the path), record the current path


class FSMTraverser:
    def __init__(self, fsm_data):
        self.states = fsm_data['states']
        self.events = fsm_data['events']
        self.transitions = fsm_data['transitions']
        logger.info(f"Reading FSM data: {len(self.states)} states, {len(self.events)} events, {len(self.transitions)} transitions")

        # Build the state transition graph
        self.transition_map = self._build_transition_map()

    def _build_transition_map(self):
        """Build the state transition mapping table"""
        transition_map = {}

        for transition in self.transitions:
            from_state = transition['from_state']
            event = transition['event']
            to_state = transition['to_state']

            if from_state not in transition_map:
                transition_map[from_state] = []

            transition_map[from_state].append({
                'event': event,
                'to_state': to_state,
                'actions': transition['actions'],
                'constraints': transition['constraints'],
                'is_global': 1 if from_state == '*' else 0
            })

        # Handle wildcard '*' transitions
        if '*' in transition_map:
            wildcard_transitions = transition_map['*']
            for state in self.states:
                if state != '*' and state in transition_map:
                    transition_map[state].extend(wildcard_transitions)
                elif state != '*':
                    transition_map[state] = wildcard_transitions.copy()

            del transition_map['*']

        return transition_map

    def traverse(self, initial_state='Down'):
        """
        Traverse the FSM and generate paths that cover all state transitions
        Args:
            initial_state (str): The initial state
        Returns:
            paths (list): A list of all paths containing normal state transitions
            paths_exd (list): A list of extended paths for recording paths containing global back edges
        """
        paths = []
        paths_exd = []  # Extended paths for recording global back edge exploration
        covered_transitions = set()  # Covered transitions (from_state, event, to_state)
        # Termination condition: A cycle is formed (the current state has appeared in the path), or the current node has no transitions, record the current path

        def dfs(current_state, path_history):
            logger.info(f"Current state: {current_state}, Path history: {path_history}")
            # Check if a cycle is formed
            # Here, we need to analyze the path history to determine if the transitions on the current state path have been covered by previous paths. If all are covered, skip saving (return directly).
            # We also need to determine if the last transition is global. If all previous ones are covered and the last one is global, it belongs to the exd path; otherwise, it belongs to the normal path.
            if path_history:
                if current_state in [step['from_state'] for step in path_history]:  # Cycle detection
                    # Simplify the path representation
                    path_str = ", ".join([f"{step['from_state']} --{step['event']}--> {step['to_state']}" for step in path_history])
                    if (len([1 for step in path_history if (step['from_state'], step['event'], step['to_state']) in covered_transitions]) == len(path_history)):  # Check if covered by previous paths
                        logger.info(f"⚠️Cycle detected, skip covered path: {path_str}")
                        return
                    logger.info(len([1 for step in path_history[:-1] if (step['from_state'], step['event'], step['to_state']) in covered_transitions]))
                    logger.info(len(path_history[:-1]))
                    if path_history[-1]['is_global'] == 1 and (len([1 for step in path_history[:-1] if (step['from_state'], step['event'], step['to_state']) in covered_transitions]) == len(path_history[:-1]) or len(path_history) == 1):
                        # If it is a global back edge and does not contain unexplored non-global back edges, save the path to the extended path list
                        paths_exd.append(path_history)
                        logger.info(f"⚠️Cycle detected, save exd path {len(paths_exd)}: {path_str}")
                    else:
                        paths.append(path_history)
                        logger.info(f"⚠️Cycle detected, save path {len(paths)}: {path_str}")
                    # Mark the transitions on the path as covered
                    for step in path_history:
                        covered_transitions.add((step['from_state'], step['event'], step['to_state']))
                    return

            # Get all possible transitions for the current state
            transitions = self.transition_map.get(current_state, [])

            # If there are no transitions, save the current path
            if not transitions and path_history:
                if (len([1 for step in path_history if (step['from_state'], step['event'], step['to_state']) in covered_transitions]) == len(path_history)):
                    logger.info(f"⚠️No transitions, skip covered path: {path_history}")
                    return
                if path_history[-1]['is_global'] == 1 and (len([1 for step in path_history[:-1] if (step['from_state'], step['event'], step['to_state']) in covered_transitions]) == len(path_history[:-1]) or len(path_history) == 1):
                    paths_exd.append(path_history)
                else:
                    paths.append(path_history)
                # Simplify the path representation
                path_str = " -> ".join([f"{step['from_state']} --{step['event']}--> {step['to_state']}" for step in path_history])
                logger.info(f"⚠️No transitions, save path: {path_str}")
                return

            # Create new paths for each possible transition
            for transition in transitions:
                event = transition['event']
                to_state = transition['to_state']

                # Build a new path (avoid reference issues)
                new_path = path_history + [{
                    'from_state': current_state,
                    'event': event,
                    'to_state': to_state,
                    'actions': transition['actions'],
                    'constraints': transition['constraints'],
                    'is_global': transition['is_global']
                }]

                # Mark the transition as covered
                # covered_transitions.add((current_state, event))

                # Recursively traverse the next state
                dfs(to_state, new_path)

        # Start the depth-first search
        dfs(initial_state, [])

        return paths, paths_exd

    def print_paths(self, paths):
        """Print the generated paths"""
        for i, path in enumerate(paths, 1):
            logger.info(f"Path {i}:")
            if not path:
                logger.info("  [Initial state]")
                continue

            logger.info(f"  Start at: {path[0]['from_state']}")
            for step in path:
                logger.info(f"  On event '{step['event']}' transition to '{step['to_state']}'")
                if step['actions']:
                    logger.info("    Actions:")
                    for action in step['actions']:
                        logger.info(f"      - {action}")
                logger.info(f"  State at: {step['to_state']}")

    def calculate_coverage(self, paths):
        """Calculate the coverage rate"""

        # Calculate the coverage rate based on the existence of transitions
        transition_coverage = {}
        for transition in self.transitions:
            from_state = transition['from_state']
            event = transition['event']
            to_state = transition['to_state']
            if from_state != '*':
                transition_coverage[f"{from_state}--{event}-->{to_state}"] = 0  # Initialize to 0, indicating not covered
            else:
                # Handle wildcard '*' transitions
                for state in self.states:
                    if state != '*':
                        transition_coverage[f"{state}--{event}-->{to_state}"] = 0

        for path in paths:
            for step in path:
                from_state = step['from_state']
                event = step['event']
                to_state = step['to_state']
                transition_key = f"{from_state}--{event}-->{to_state}"
                if transition_key in transition_coverage:
                    transition_coverage[transition_key] += 1

        # Calculate the coverage rate
        total_transitions = len(transition_coverage)
        logger.info(f"Transition coverage status: {transition_coverage}")
        covered_transitions = sum(1 for count in transition_coverage.values() if count > 0)
        coverage = covered_transitions / total_transitions if total_transitions > 0 else 0
        return coverage

# Example usage
if __name__ == "__main__":

    logger.setLevel(logging.INFO)
    # Configure the logger for minimal output
    formatter = logging.Formatter("%(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Load FSM data (assuming the provided JSON data has been loaded)
    fsm_data = json.load(open('data/raw_documents/RFC_FSMs/rfc_2328_10.1/rfc_2328_10.1.json'))

    logger.info(len(fsm_data['states']))

    # Create an FSM traverser
    traverser = FSMTraverser(fsm_data)

    logger.info("State transition graph:")
    logger.info(json.dumps(traverser.transition_map, indent=2))
    logger.info(len(traverser.transition_map))

    # Traverse the FSM and generate all paths
    paths, paths_exd = traverser.traverse(initial_state=fsm_data['init_state'])
    logger.info(f"Number of generated normal paths: {len(paths)}")
    logger.info(f"Number of generated extended paths: {len(paths_exd)}")

    # Print the generated paths
    traverser.print_paths(paths)
    traverser.print_paths(paths_exd)

    # Calculate the coverage rate
    coverage = traverser.calculate_coverage(paths + paths_exd)
    logger.info(f"Coverage rate: {coverage:.2%}")

    # # Traverse the FSM and generate all paths (limit the depth to 5 to avoid infinite loops)
    # paths = traverser.get_transition_paths(max_depth=5)

    # # Print the generated paths
    # traverser.print_paths(paths)

    # You can also save the paths as a JSON file for subsequent test case generation
    with open('temp_fsm_paths.json', 'w') as f:
        json.dump(paths, f, indent=2)
    with open('temp_fsm_paths_exd.json', 'w') as f_exd:
        json.dump(paths_exd, f_exd, indent=2)


# /root/anaconda3/envs/nettest/bin/python /root/NetAutoTest/src/testcase_generator/fsm_traverse.py > fsm_traverse.log 2>&1 &