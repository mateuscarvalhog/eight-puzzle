from random import randint
from typing import List
from menu import Menu
from puzzle_state import PuzzleState
from agent import Agent
import time
import os

class Puzzle:
    def __init__(self):
        self.objective_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, None]])
        self.initial_state = self.generate_initial_state()
        self.solver = Agent(self.initial_state, self.objective_state)

    def generate_initial_state(self):
        number_of_iterations = randint(500, 1500)
        initial_state = self.objective_state

        for _ in range(number_of_iterations):
            new_states = Agent.generate_new_states(initial_state)
            random_index = randint(0, len(new_states) - 1)
            initial_state = new_states[random_index]

        return initial_state
    
    def set_initial_state(self, initial_state_str: str):
        matrix_of_initial_state = list()

        for index in range(len(initial_state_str)):
            row = int(index/PuzzleState.NUM_OF_COLUMNS)

            element = None if initial_state_str[index] == "0" else int(initial_state_str[index])

            if (row >= len(matrix_of_initial_state)):
                matrix_of_initial_state.append(list())

            matrix_of_initial_state[row].append(element)

        self.initial_state = PuzzleState(matrix_of_initial_state)

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

def main():
    search_menu = Menu([(1, 'Blind search (Breadth-first)'), (2, 'Heuristic search (Manhattan distance)')], 'Choose a search method')

    main_menu = Menu([(1, 'New random game'), (2, 'New custom game'), (0, 'Exit')], 'THE 8-PUZZLE SOLVER')
    main_menu.show(show_title = True)

    game_option = main_menu.wait_an_option()

    while game_option != 0:
        puzzle = Puzzle()

        if game_option == 2:
            initial_state = input("Enter game state, from top-left to right-bottom, 9 characters, e.g. \"1034526478\": ")
            puzzle.set_initial_state(initial_state)
        
        print("\nYour initial state:")
        print(puzzle.initial_state)

        search_menu.show()
        search_option = search_menu.wait_an_option()
        if (search_option == 1):
            puzzle.solve_with_blind_search()
        elif (search_option == 2):
            puzzle.solve_with_heuristic_search()


        game_option = main_menu.wait_an_option(show_menu = True, show_title = True)
        
    print("\n\nTHANK YOU FOR PLAYING THE 8-PUZZLE SOLVER!")

if __name__ == "__main__":
    main()