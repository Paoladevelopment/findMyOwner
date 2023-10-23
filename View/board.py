import tkinter as tk
from PIL import ImageTk, Image

from Constants.generalConstants import INFO_ENTITIES_IMAGES

class GameBoardApp:
    def __init__(self, root, game_board, info_entities_images):
        self.root = root
        self.game_board = game_board
        self.info_entities_images = info_entities_images

        self.cells = []
        self.step = 0

        self.create_game_board()

    def create_game_board(self):
        for i in range(len(self.game_board)):
            row = []
            for j in range(len(self.game_board[i])):
                cell_value = self.game_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((100, 100))
                img = ImageTk.PhotoImage(resized_image)
                cell_label = tk.Label(
                    self.root,
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
            self.cells.append(row)

        update_button = tk.Button(self.root, text="Start", command=self.start_travel)
        update_button.grid(row=len(self.game_board), columnspan=len(self.game_board[0]))

    def update_board(self, new_board):
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                cell_value = new_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((100, 100))
                img = ImageTk.PhotoImage(resized_image)
                cell_label = tk.Label(
                    self.root,
                    borderwidth=1,
                    relief="solid",
                    background="white",
                    image=img,
                    anchor="center",
                    compound="center",
                )
                cell_label.image = img
                cell_label.grid(row=i, column=j)

    def update_step(self):
        if self.step < len(self.ALL_STEPS):
            self.update_board(self.ALL_STEPS[self.step])
            self.step += 1
            self.root.after(1000, self.update_step)

    def start_travel(self):
        self.step = 0
        self.update_step()
