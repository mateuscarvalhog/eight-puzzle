from puzzle_state import PuzzleState
from agent import Agent

class Puzzle:

    def __init__(self):
        self.initial_state = self.generate_initial_state()
        self.solution = self.solve()

    def generate_initial_state(self):
        return PuzzleState([[1, 2, 3], [4, 5, 6], [7, None, 8]])  # TODO mudar constante de estado inicial
    
    def solve(self):
        solver = Agent(self.initial_state, [[1, 2, 3], [4, 5, 6], [7, 8, None]]) # TODO mudar constante de estado objetivo
        return []


def main():
    puzzle = Puzzle()
    # print(puzzle.solution)

if __name__ == "__main__":
    main()