from typing import List, final
from position import Position
from puzzle_state import PuzzleState
from queue import PriorityQueue
# .put((md_value, state))
# .get() retorna tupla

class Agent:

    def __init__(self, initial_state: PuzzleState, objective_state: PuzzleState):
        self.initial_state = initial_state
        self.objective_state = objective_state

    def play_with_blind_search(self):
        # execucao geral do agente: List<PuzzleState>
        priority_queue = PriorityQueue()
        already_expanded_states = list()

        priority_queue.put((0, self.initial_state))
        already_expanded_states.append(self.initial_state)
        state_had_not_been_expanded = lambda state: all(not expanded_state.is_equal(state) for expanded_state in already_expanded_states)

        final_state = None

        while final_state is None and not priority_queue.empty():
            _, current_state = priority_queue.get()

            if current_state.is_equal(self.objective_state):
                final_state = current_state
            else:
                new_states = self.generate_new_states(current_state)
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
            
            return trace_route
    
    def generate_new_states(self, state: PuzzleState) -> List[PuzzleState]:
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

    def add_node(self, state: PuzzleState):
        priority_value = state.calculate_manhattan_distance(self.objective_state)
        # self.nodes = TODO melhorar nome e implementar hash
        # node_already_exists = any(node.is_equal(new_node) for node in self.nodes)
        print("add_node")
