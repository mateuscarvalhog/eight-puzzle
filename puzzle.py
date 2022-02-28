from logging.config import valid_ident
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

        print("\nYour initial state:")
        print(self.initial_state)

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
        print("\n\nSolving puzzle with Breadth-First blind search method...")
        
        start_time = time.time()
        search_result = self.solver.play_with_blind_search()
        end_time = time.time()

        self.print_solving_steps(search_result.trace_route)
        print(f'Solved with blind search')
        print(f'Execution time: {end_time - start_time} s')
        print(search_result)
    
    def solve_with_heuristic_search(self):
        print("\n\nSolving puzzle with Manhattan Distance heuristic search method...")
        
        start_time = time.time()
        search_result = self.solver.play_with_heuristic_search()
        end_time = time.time()

        self.print_solving_steps(search_result.trace_route)
        print(f'Solved with heuristic search')
        print(f'Execution time: {end_time - start_time} s')
        print(search_result)

    def print_solving_steps(self, trace_route: List[PuzzleState]):
        clear_console = lambda: os.system('cls' if os.name=='nt' else 'clear')
        for state in trace_route:
            clear_console()
            print(state)
            time.sleep(.001)


def print_invalid_input(valid_inputs): # TODO TIPAR INT[]
    error = "Please select a valid option: "
    for i in range(len(valid_inputs)):
        error += str(valid_inputs[i])
        if (i < len(valid_inputs) - 1):
            error += " or "
    
    print(error)

def is_input_valid(input, valid_inputs): # TODO tipar params
    is_valid = False
    last_index = len(valid_inputs) - 1
    index = 0
    while (not is_valid and index <= last_index):
        if (valid_inputs[index] == input):
            is_valid = True
        index += 1
        
    return is_valid

def get_valid_option(first_try, valid_inputs):
    option = first_try
    while (not is_input_valid(option, valid_inputs)):
        print_invalid_input(valid_inputs)
        option = input()
    
    return option

def main():
    print("THE 8-PUZZLE SOLVER\n")

    game_option = 0
    while (game_option != "2"):
        game_option = get_valid_option(input("\nType the number of your action:\n1. New game\t2. Exit\n"), ["1", "2"])

        if (game_option == "1"):
            puzzle = Puzzle()
            
            search_option = get_valid_option(input("\nType the number of the search method:\n1. Blind search (Breadth-first)\t\t2. Heuristic search (Manhattan distance)\n"), ["1", "2"])
            if (search_option == "1"):
                puzzle.solve_with_blind_search()
            elif (search_option == "2"):
                puzzle.solve_with_heuristic_search()
        
    print("\n\nTHANK YOU FOR PLAYING THE 8-PUZZLE SOLVER!")

if __name__ == "__main__":
    main()