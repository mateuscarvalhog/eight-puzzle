from random import randint
from typing import List
from puzzle_state import PuzzleState
from agent import Agent
import time
import os

class Puzzle:
    def __init__(self):
        self.objective_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, None]])
        # self.objective_state = PuzzleState([[1, 2, 3], [8, None, 4], [7, 6, 5]])
        self.initial_state = self.generate_initial_state()
        self.solver = Agent(self.initial_state, self.objective_state)

        print(self.initial_state)

        # self.solve_with_blind_search()
        # self.solve_with_heuristic_search()

    def generate_initial_state(self):
        number_of_iterations = randint(500, 1500)
        initial_state = self.objective_state

        for _ in range(number_of_iterations):
            new_states = Agent.generate_new_states(initial_state)
            random_index = randint(0, len(new_states) - 1)
            initial_state = new_states[random_index]

        return initial_state
        # return PuzzleState([[1, None, 3], [5, 2, 6], [4, 7, 8]])  # TODO mudar constante de estado inicial
        # return PuzzleState([[4, 8, 1], [7, 3, 5], [None, 6, 2]])  # TODO mudar constante de estado inicial
    
    def solve_with_blind_search(self):
        start_time = time.time()
        search_result = self.solver.play_with_blind_search()
        end_time = time.time()

        self.print_solve_steps(search_result.trace_route)
        print(f'Solved with blind search');
        print(f'Execution time: {end_time - start_time} s')
        print(search_result)
    
    def solve_with_heuristic_search(self):
        start_time = time.time()
        search_result = self.solver.play_with_heuristic_search()
        end_time = time.time()

        self.print_solve_steps(search_result.trace_route)
        print(f'Solved with heuristic search');
        print(f'Execution time: {end_time - start_time} s')
        print(search_result)

    def print_solve_steps(self, trace_route: List[PuzzleState]):
        clear_console = lambda: os.system('cls' if os.name=='nt' else 'clear')
        for state in trace_route:
            clear_console()
            print(state)
            time.sleep(.001)


def main():
    puzzle = Puzzle()
    # print(puzzle.solution)

if __name__ == "__main__":
    main()