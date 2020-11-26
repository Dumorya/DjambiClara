import tkinter as tk
from PIL import Image, ImageTk

from classes.necromobile import Necromobile
from classes.peon import Peon


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
        self._active_cell = None

        # intitialize empty board
        for i in range(self._nb_rows):
            self._cells.append([])
            for j in range(self._nb_columns):
                cell = BoardCell(None, self, self._cells[i]).create_button(self._master)
                self._cells[i].append(cell)
                cell.grid(row=i, column=j)


        # add peons in board
        for peon in self._peons:
            row_index, col_index = peon.position
            boardcell = BoardCell(peon, self, [row_index-1, col_index-1])
            self._cells[row_index-1][col_index-1] = boardcell
            cell = boardcell.create_button(self._master)
            cell.grid(row=row_index-1, column=col_index-1)

    def move_peon(self, boardcell):
        # TODO: get position of cell when it's empty (not working with peon's position bt cell's position)
        boardcell.position = boardcell._peon.position

    def set_active(self, boardcell):
        # TODO: implement the case where we want to change our peon

        if self._active_cell is None:
            # take the peon
            self._active_cell = boardcell
        else:
            # place the peon
            self.move_peon(self._active_cell)
            self._active_cell = None


class BoardCell:

    """This generates cells from a board, in which there are peons"""

    def __init__(self, peon, board, position):
        self._peon = peon
        self._board = board
        self._position = position

    def press_button(self):
        self._board.set_active(self)

    def create_button(self, master):
        if self._peon:
            image = Image.open(self._peon.image)
            image = image.resize((60, 60), Image.ANTIALIAS)
            image_elem = ImageTk.PhotoImage(image)
            button = tk.Button(
                master,
                image=image_elem,
                bg=self._peon.color,
                command=self.press_button)
            button.image = image_elem
        else:
            image = Image.open('assets/icons/blank.png')
            image_elem = ImageTk.PhotoImage(image)
            button = tk.Button(
                master,
                image=image_elem,
                command=self.press_button)
            button.image = image_elem

        return button
