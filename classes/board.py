import tkinter as tk
from PIL import Image, ImageTk


class Board(tk.Frame):
    """Creates a board which is the support of the game"""

    def __init__(self, nb_rows, nb_columns, peons, master=None):
        """creates board with empty cells then fills it with peons"""

        super().__init__(master)
        self._master = master
        self._nb_rows = nb_rows
        self._nb_columns = nb_columns
        self._peons = peons
        self._cells = []

        for i in range(self._nb_rows):
            self._cells.append([])
            for j in range(self._nb_columns):
                self._cells[i].append(None)

        for peon in self._peons:
            row_index, col_index = peon.position
            self._cells[row_index-1][col_index-1] = peon

        self._create_grid()

    def _create_grid(self):
        """creates grid with tk. Each cell is filled by a button"""
        for r in range(self._nb_rows):
            for c in range(self._nb_columns):
                boardcell = BoardCell(self._cells[r][c])
                cell = boardcell.create_button(self._master)
                cell.grid(row=r, column=c)


class BoardCell:

    """This generates cells from a board, in which there are peons"""

    def __init__(self, peon):
        self._peon = peon

    def create_button(self, master):
        if self._peon:
            image = Image.open(self._peon.image)
            image_elem = ImageTk.PhotoImage(image)
            button = tk.Button(master, image=image_elem, bg=self._peon.color)
            button.image = image_elem
        else:
            image = Image.open('assets/icons/blank.png')
            image_elem = ImageTk.PhotoImage(image)
            button = tk.Button(master, image=image_elem)
            button.image = image_elem

        return button
