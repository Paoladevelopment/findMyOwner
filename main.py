from View.board import GameBoardApp
import tkinter as tk
from Constants.generalConstants import INFO_ENTITIES_IMAGES

game_board = [
    [1, 1, 3, 1, 1, 1, 1, 1],
    [1, 2, 5, 5, 2, 5, 5, 1],
    [4, 5, 1, 1, 1, 5, 5, 0],
    [1, 5, 1, 5, 5, 5, 1, 1],
    [1, 2, 1, 3, 1, 1, 1, 1],
]

ALL_STEPS = {}

root = tk.Tk()
root.title("New Board")

app = GameBoardApp(root, game_board, INFO_ENTITIES_IMAGES)

root.mainloop()