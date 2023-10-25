import tkinter as tk

from View.board import GameBoardApp
from Constants.generalConstants import INFO_ENTITIES_IMAGES, INFO_ENTITIES
from Constants.generalConstants import LIST_ACTIONS
from Constants.generalConstants import COSTS
from Models.State import State
from Models.Problem import Problem
from Models.Node import Node
from Search import cost_uniform_recursive as cu

game_board = [
    [1, 1, 3, 1, 1, 1, 1, 1],
    [1, 2, 5, 5, 2, 5, 5, 1],
    [4, 5, 1, 1, 1, 5, 5, 0],
    [1, 5, 1, 5, 5, 5, 1, 1],
    [1, 2, 1, 3, 1, 1, 1, 1],
]
positions = {
    0: [2, 7],
    1: [1, 7],
    2: [0, 7],
    3: [0, 6],
    4: [0, 5],
    5: [0, 4],
    6: [1, 4],
    7: [2, 4],
    8: [2, 3],
    9: [2, 2],
    10: [3, 2],
    11: [4, 2],
    12: [4, 1],
    13: [4, 0],
    14: [3, 0],
    15: [2, 0]
}

initial_state = State(2, 7, [])
goal_state = State(2, 0, [])
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board, COSTS)
solution = cu.cost_uniform_recursive(problem)
print(solution.state.__str__())
cu.show_solution(solution)
print(cu.steps_solution(solution))

root = tk.Tk()
root.title("New Board")

app = GameBoardApp(root, game_board, positions, INFO_ENTITIES_IMAGES, INFO_ENTITIES)

root.mainloop()
