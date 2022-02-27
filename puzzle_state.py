class PuzzleState:

    def __init__(self, matrix, parent = None):
        self.matrix = matrix
        self.parent = parent

    def is_equal(self, objective_state):
        # compara o objeto ao estado objetivo: boolean
        print("is_equal")
    
    def calculate_manhattan_distance(self, objective_state):
        # calcula o valor da heuristica para fila de prioridades: List<PuzzleState>
        print("calculate_manhattan_distance")