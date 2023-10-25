import random
from Constants.generalConstants import PROBABILITIES

def random_board():
    game_board = []
    for _ in range(5):
        row = []
        for _ in range(8):
            entity = get_entity()
            row.append(entity)
        game_board.append(row)

    positions = get_states()
    initial_position = positions[0]
    goal_position = positions[1]
    
    game_board[initial_position[0]][initial_position[1]] = 0
    game_board[goal_position[0]][goal_position[1]] = 4
  
    return game_board, initial_position, goal_position


def get_entity():
    return random.choices(list(PROBABILITIES.keys()), list(PROBABILITIES.values()))[0]

def get_states():
    initial_position = (random.randint(0, 4), random.randint(0, 7))
    goal_position =  (random.randint(0, 4), random.randint(0, 7))
    while initial_position == goal_position:
        goal_state = (random.randint(0, 4), random.randint(0, 7))
    return initial_position, goal_position