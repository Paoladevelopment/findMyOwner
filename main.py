import tkinter as tk
import random

from View.board import GameBoardApp
from Constants.generalConstants import INFO_ENTITIES_IMAGES, INFO_ENTITIES
from Constants.generalConstants import LIST_ACTIONS
from Constants.generalConstants import COSTS
from Models.State import State
from Models.Problem import Problem
from Models.Node import Node
from Search import cost_uniform_recursive as cu

def random_board():
    probabilities = {
        1: 0.4,
        2: 0.15,
        3: 0.15,
        5: 0.3
    }

    game_board = []

    for _ in range(5):
        row = []
        for _ in range(8):
            entity = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
            row.append(entity)
        game_board.append(row)

    zero_position = (random.randint(0, 4), random.randint(0, 7))
    four_position = (random.randint(0, 4), random.randint(0, 7))
    
    while zero_position == four_position:
        four_position = (random.randint(0, 4), random.randint(0, 7))
    
    game_board[zero_position[0]][zero_position[1]] = 0
    game_board[four_position[0]][four_position[1]] = 4
  
    return game_board, zero_position, four_position



random_board = random_board()
game_board = random_board[0]
initial_state = State(random_board[1][0], random_board[1][1], [])
goal_state = State(random_board[2][0], random_board[2][1], [])

# game_board = [
#     [1, 1, 3, 1, 1, 1, 1, 1],
#     [1, 2, 5, 5, 2, 5, 5, 1],
#     [4, 5, 1, 1, 1, 5, 5, 0],
#     [1, 5, 1, 5, 5, 5, 1, 1],
#     [1, 2, 1, 3, 1, 1, 1, 1],
# ]



# initial_state = State(2, 7, [])
# goal_state = State(2, 0, [])
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board, COSTS)
solution = cu.cost_uniform_recursive(problem)
# print(solution.state.__str__())
cu.show_solution(solution)
print(cu.steps_solution(solution))

positions = cu.steps_solution(solution)

initial_state = State(2, 7, [])
goal_state = State(2, 0, [])
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board, COSTS)
solution = cu.cost_uniform_recursive(problem)
# print(solution.state.__str__())
cu.show_solution(solution)
print(cu.steps_solution(solution))

root = tk.Tk()
root.title("New Board")

app = GameBoardApp(root, game_board, positions, INFO_ENTITIES_IMAGES, INFO_ENTITIES)

root.mainloop()
