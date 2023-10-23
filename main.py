import tkinter as tk
from PIL import ImageTk, Image
import time

from Constants.generalConstants import LIST_ACTIONS
from Constants.generalConstants import INFO_ENTITIES
from Constants.generalConstants import INFO_ENTITIES_IMAGES
from Models.State import State
from Models.Problem import Problem

game_board = [
    [1, 1, 3, 1, 1, 1, 1, 1],
    [1, 2, 5, 5, 2, 5, 5, 1],
    [4, 5, 1, 1, 1, 5, 5, 0],
    [1, 5, 1, 5, 5, 5, 1, 1],
    [1, 2, 1, 3, 1, 1, 1, 1],
]
ALL_STEPS = {}
# Needs to be replaced


initial_state = State(0, 3, [])
goal_state = State(2, 0, [])
problem = Problem(initial_state, goal_state, LIST_ACTIONS, game_board)


root = tk.Tk()
root.title("Board")
cells = []

for i in range(len(game_board)):
    row = []
    for j in range(len(game_board[i])):
        cell_value = game_board[i][j]
        original_image = Image.open(INFO_ENTITIES_IMAGES[cell_value])
        resized_image = original_image.resize((100, 100))
        img = ImageTk.PhotoImage(resized_image)
        cell_label = tk.Label(
            root,
            borderwidth=1,
            relief="solid",
            background="white",
            image=img,
            anchor="center",
            compound="center",
        )
        cell_label.image = img
        cell_label.grid(row=i, column=j)
        row.append(cell_label)
    cells.append(row)

def update_board(new_board):
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            cell_value = new_board[i][j]
            original_image = Image.open(INFO_ENTITIES_IMAGES[cell_value])
            resized_image = original_image.resize((100, 100))
            img = ImageTk.PhotoImage(resized_image)
            cell_label = tk.Label(
                root,
                borderwidth=1,
                relief="solid",
                background="white",
                image=img,
                anchor="center",
                compound="center",
            )
            cell_label.image = img
            cell_label.grid(row=i, column=j)

step = 0
def update_step():
    global step
    if step < len(ALL_STEPS):
        update_board(ALL_STEPS[step])
        step += 1
        root.after(1000, update_step)

def start_travel():
    global step
    step = 0 
    update_step() 



update_button = tk.Button(root, text="Empezar", command=start_travel)
update_button.grid(row=len(game_board), columnspan=len(game_board[0]))

root.mainloop()
