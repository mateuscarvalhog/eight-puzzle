from __future__ import annotations
from typing import List
from position import Position
from puzzle_state import PuzzleState
from priority_queue import PriorityQueue
from queue import SimpleQueue

class Agent:
    def __init__(self, initial_state: PuzzleState, objective_state: PuzzleState):
        self.initial_state = initial_state
        self.objective_state = objective_state

    def play_with_blind_search(self) -> SearchResult:
        # execucao geral do agente: List<PuzzleState>
        simple_queue = SimpleQueue()
        already_expanded_states = list()

        simple_queue.put(self.initial_state)
        already_expanded_states.append(self.initial_state)
        state_had_not_been_expanded = lambda state: all(not expanded_state.is_equal(state) for expanded_state in already_expanded_states)

        final_state = None

        while final_state is None and not simple_queue.empty():
            current_state = simple_queue.get()

            if current_state.is_equal(self.objective_state):
                final_state = current_state
            else:
                new_states = Agent.generate_new_states(current_state)
                new_unexpanded_states = list(filter(state_had_not_been_expanded, new_states))
                already_expanded_states.extend(new_unexpanded_states)

                for state in new_unexpanded_states:
                    simple_queue.put(state)

        if final_state is not None:
            trace_route = [final_state]

            current_state = final_state
            while current_state.parent is not None:
                trace_route.insert(0, current_state.parent)
                current_state = current_state.parent
            
            return SearchResult(len(already_expanded_states) - simple_queue.qsize(), trace_route)

        return SearchResult(len(already_expanded_states), trace_route)

    def play_with_heuristic_search(self) -> SearchResult:
        # execucao geral do agente: List<PuzzleState>
        priority_queue = PriorityQueue()
        already_expanded_states = list()

        priority_queue.put((0, self.initial_state))
        already_expanded_states.append(self.initial_state)
        state_had_not_been_expanded = lambda state: all(not expanded_state.is_equal(state) for expanded_state in already_expanded_states)

        final_state = None

        while final_state is None and not priority_queue.empty():
            current_state = priority_queue.get()

            if current_state.is_equal(self.objective_state):
                final_state = current_state
            else:
                new_states = Agent.generate_new_states(current_state)
                new_unexpanded_states = list(filter(state_had_not_been_expanded, new_states))
                already_expanded_states.extend(new_unexpanded_states)

                for state in new_unexpanded_states:
                    manhattan_distance = state.calculate_manhattan_distance(self.objective_state)
                    priority_queue.put((manhattan_distance, state))

        if final_state is not None:
            trace_route = [final_state]

            current_state = final_state
            while current_state.parent is not None:
                trace_route.insert(0, current_state.parent)
                current_state = current_state.parent
            
            return SearchResult(len(already_expanded_states) - priority_queue.size(), trace_route)

        return SearchResult(len(already_expanded_states), trace_route)
    
    def generate_new_states(state: PuzzleState) -> List[PuzzleState]:
        # gera novos estados a partir do atual: List<PuzzleState>
        blank_position = state.get_blank_position()

        blank_is_not_at = {
            'top': blank_position.row > 0,
            'bottom': blank_position.row < PuzzleState.NUM_OF_ROWS - 1,
            'left': blank_position.column > 0,
            'right': blank_position.column < PuzzleState.NUM_OF_COLUMNS - 1,
        }

        new_states: List[PuzzleState] = list()

        if blank_is_not_at['top']:
            target_position: Position = Position(blank_position.row - 1, blank_position.column)
            new_states.append(state.move_piece(blank_position, target_position))

        if blank_is_not_at['bottom']:
            target_position: Position = Position(blank_position.row + 1, blank_position.column)
            new_states.append(state.move_piece(blank_position, target_position))

        if blank_is_not_at['left']:
            target_position: Position = Position(blank_position.row, blank_position.column - 1)
            new_states.append(state.move_piece(blank_position, target_position))

        if blank_is_not_at['right']:
            target_position: Position = Position(blank_position.row, blank_position.column + 1)
            new_states.append(state.move_piece(blank_position, target_position))

        return new_states

class SearchResult:
    def __init__(self, number_of_visited_nodes: int, trace_route: List[PuzzleState] = []):
        self.number_of_visited_nodes = number_of_visited_nodes
        self.trace_route = trace_route

    def __repr__(self):
        str_to_return = f'Number of visited nodes: {self.number_of_visited_nodes}\n'
        str_to_return += f'Number of steps: {len(self.trace_route)}\n\n'
        str_to_return += '-'*20 + '\n'

        return str_to_return