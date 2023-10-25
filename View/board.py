import tkinter as tk
from PIL import ImageTk, Image
import copy


class GameBoardApp:
    def __init__(
        self, root, game_board, game_positions, info_entities_images, info_entities
    ):
        self.root = root
        self.game_board = game_board
        self.info_entities_images = info_entities_images
        self.info_entities = info_entities
        self.game_positions = game_positions
        self.cells = []
        self.step = 0

        self.create_game_board()

    def create_game_board(self):
        image_size = 100
        if len(self.game_board) > 6:
            image_size = 50
        for i in range(len(self.game_board)):
            row = []
            for j in range(len(self.game_board[i])):
                cell_value = self.game_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((image_size, image_size))
                img = ImageTk.PhotoImage(resized_image)
                cell_label = tk.Label(
                    self.root,
                    borderwidth=0,
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

        update_button = tk.Button(self.root, text="Cerebro!", command=self.start_travel)
        update_button.configure(bg="green", fg="white")

        button_font = ("Helvetica", 12)
        update_button.configure(font=button_font)

        update_button.configure(relief="raised")
        update_button.grid(row=len(self.game_board), columnspan=len(self.game_board[0]))

    def update_board(self, new_board):
        image_size = 100
        if len(self.game_board) > 6:
            image_size = 50
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                cell_value = new_board[i][j]
                original_image = Image.open(self.info_entities_images[cell_value])
                resized_image = original_image.resize((image_size, image_size))
                img = ImageTk.PhotoImage(resized_image)
                cell_label = tk.Label(
                    self.root,
                    borderwidth=0,
                    relief="solid",
                    background="white",
                    image=img,
                    anchor="center",
                    compound="center",
                )
                cell_label.image = img
                cell_label.grid(row=i, column=j)

    def update_step(self):
        if self.step < len(self.game_positions):
            new_board = copy.deepcopy(self.game_board)
            positions = self.game_positions
            time = 250
            new_position = positions[self.step]
            current_value = new_board[new_position[0]][new_position[1]]

            value_mapping = {2: (6, 2), 3: (7, 3), 4: (8, 4)}
            if self.step > 0:
                new_board[positions[0][0]][positions[0][1]] = 1
            if current_value in value_mapping:
                new_value, condition_value = value_mapping[current_value]
                new_board[new_position[0]][new_position[1]] = new_value
                time = 1000
                if self.step - 1 and not any(
                    new_board[positions[self.step - 1][0]][positions[self.step - 1][1]]
                    == val
                    for val in (condition_value, 3, 4)
                ):
                    new_board[positions[self.step - 1][0]][
                        positions[self.step - 1][1]
                    ] = 1
            if current_value == 1:
                new_board[new_position[0]][new_position[1]] = 0
                if self.step - 1 and not any(
                    new_board[positions[self.step - 1][0]][positions[self.step - 1][1]]
                    == val
                    for val in (2, 3, 4)
                ):
                    new_board[positions[self.step - 1][0]][
                        positions[self.step - 1][1]
                    ] = 1
                    
            self.update_board(new_board)
            self.step += 1
            self.root.after(time, self.update_step)

    def start_travel(self):
        self.step = 0
        self.update_step()
