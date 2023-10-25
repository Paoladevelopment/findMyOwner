import tkinter as tk

from View.board import GameBoardApp
from Constants.generalConstants import INFO_ENTITIES_IMAGES, INFO_ENTITIES
from Constants.generalConstants import LIST_ACTIONS
from Constants.generalConstants import COSTS
from Models.State import State
from Models.Problem import Problem
from Search import cost_uniform_recursive as cu
from Helpers.gameHelpers import random_board


#Obtain the random board which contains the enviroment of the game, the initial position and the goal position
random_board = random_board()
game_board = random_board[0]

#Creates the corresponding state according to the initia position and the goal position
initial_state = State(random_board[1][0], random_board[1][1], [])
goal_state = State(random_board[2][0], random_board[2][1], [])

#Creates the problem for the current environment
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board, COSTS)

#The solution for the current environment
solution = cu.cost_uniform_recursive(problem)
cu.show_solution(solution)
print(cu.steps_solution(solution))

#Positions is a dictionary with the steps that the zombie should take to get to the brain. It is helpfull to display the sol in the gameboard
positions = cu.steps_solution(solution)

"""
game_board = [
     [1, 1, 3, 1, 1, 1, 1, 1],
     [1, 2, 5, 5, 2, 5, 5, 1],
     [4, 5, 1, 1, 1, 5, 5, 0],
     [1, 5, 1, 5, 5, 5, 1, 1],
     [1, 2, 1, 3, 1, 1, 1, 1],
]



initial_state = State(2, 7, [])
goal_state = State(2, 0, [])
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board, COSTS)
solution = cu.cost_uniform_recursive(problem)
cu.show_solution(solution)

positions = cu.steps_solution(solution)

"""

root = tk.Tk()
root.title("New Board")

app = GameBoardApp(root, game_board, positions, INFO_ENTITIES_IMAGES, INFO_ENTITIES)

root.mainloop()
