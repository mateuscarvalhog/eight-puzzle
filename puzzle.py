from position import Position
from puzzle_state import PuzzleState
from agent import Agent

class Puzzle:
    def __init__(self):
        self.initial_state = self.generate_initial_state()
        self.solution = self.solve()

    def generate_initial_state(self):
        return PuzzleState([[7, 3, 5], [2, 8, 6], [4, 1, None]])  # TODO mudar constante de estado inicial
    
    def solve(self):
        objective_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, None]])
        solver = Agent(self.initial_state, objective_state) # TODO mudar constante de estado objetivo
        return solver.play_with_blind_search()


def main():
    puzzle = Puzzle()
    # print(puzzle.solution)

if __name__ == "__main__":
    main()