from __future__ import annotations
from typing import List, Callable
from position import Position
from copy import deepcopy

class PuzzleState:
    NUM_OF_ROWS = 3
    NUM_OF_COLUMNS = 3

    def __init__(self, matrix: List[List[int]], parent = None):
        self.matrix = matrix
        self.parent = parent

    def __repr__(self): 
        value_to_string: Callable[[], str] = lambda value: ' ' if value == None else str(value)

        str_puzzle_state = ''
        for line in self.matrix:
            str_puzzle_state += ' | '.join(map(value_to_string, line)) + '\n'

        return str_puzzle_state

    def move_blank(self, target_position: Position) -> PuzzleState:
        blank_position = self.get_blank_position()

        move_in_two_dimensions = blank_position.row != target_position.row and blank_position.column != target_position.column
        move_more_than_one_position = abs(blank_position.row - target_position.row) > 1 or abs(blank_position.column - target_position.column) > 1

        if move_in_two_dimensions or move_more_than_one_position:
            raise Exception('Invalid movement!')

        new_matrix = deepcopy(self.matrix)
        new_matrix[blank_position.row][blank_position.column] = self.matrix[target_position.row][target_position.column]
        new_matrix[target_position.row][target_position.column] = None

        return PuzzleState(new_matrix, parent = self)

    def is_equal(self, state: PuzzleState) -> bool:
        """Check if self puzzle state and another puzzle state are identical"""
        for row in range(PuzzleState.NUM_OF_ROWS):
            for column in range(PuzzleState.NUM_OF_COLUMNS):
                if (self.matrix[row][column] != state.matrix[row][column]):
                    return False
        return True

    def get_element_position(self, given_element) -> Position:
        """Get row and column of given element."""
        list_has_given_element = lambda some_list: any(element is given_element for element in some_list)
        row_with_given_element = next(iter(filter(list_has_given_element, self.matrix)), None)
        row_index = self.matrix.index(row_with_given_element)
        column_index = row_with_given_element.index(given_element)

        return Position(row_index, column_index)
    
    def get_blank_position(self) -> Position:
        """Get row and column of the blank piece."""
        return self.get_element_position(None)

    def calculate_manhattan_distance(self, objective_state: PuzzleState) -> int:
        """Calculate the Manhattan Distance heuristic value. Used by the priority queue"""
        manhattan_distance = 0
        
        for row in range(PuzzleState.NUM_OF_ROWS):
            for column in range(PuzzleState.NUM_OF_COLUMNS):
                element = self.matrix[row][column]
                if element is not None:
                    objective_position = objective_state.get_element_position(element)

                    manhattan_distance += abs(row - objective_position.row)
                    manhattan_distance += abs(column - objective_position.column)
        
        return manhattan_distance