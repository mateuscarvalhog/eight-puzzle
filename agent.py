from queue import PriorityQueue
# .put((md_value, state))
# .get() retorna tupla

class Agent:
    # objective_state = [][] CONSTANTE?
    # priority_queue = PriorityQueue()

    def __init__(self, initial_state):
        self.current_state = initial_state
        self.add_node(initial_state)

    def play(self):
        # execucao geral do agente: List<PuzzleState>
        print("play")
    
    def generate_new_states(self):
        # gera novos estados a partir do atual: List<PuzzleState>
        print("generate_new_states")

    def add_node(self, state):
        # self.nodes = TODO melhorar nome e implementar hash
        # node_already_exists = any(node.is_equal(new_node) for node in self.nodes)
        print("add_node")