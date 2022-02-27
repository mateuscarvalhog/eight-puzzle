from puzzle_state import PuzzleState
try:
    from queue import PriorityQueue
except ImportError:
    from Queue import PriorityQueue  # python 2.x
# .put((md_value, state))
# .get() retorna tupla

class Agent:

    def __init__(self, initial_state, objective_state):
        self.current_state = initial_state
        self.objective_state = objective_state
        self.add_node(initial_state)

    def play(self):
        priority_queue = PriorityQueue()
        # execucao geral do agente: List<PuzzleState>
        print("play")
    
    def generate_new_states(self):
        # gera novos estados a partir do atual: List<PuzzleState>
        print("generate_new_states")

    def add_node(self, state: PuzzleState):
        priority_value = state.calculate_manhattan_distance(self.objective_state)
        # self.nodes = TODO melhorar nome e implementar hash
        # node_already_exists = any(node.is_equal(new_node) for node in self.nodes)
        print("add_node")