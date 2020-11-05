import tkinter as tk
from PIL import Image, ImageTk


class Board(tk.Frame):

    def __init__(self, nb_rows, nb_columns, peons, master=None):
        super().__init__(master)
        self._master = master
        self._nb_rows = nb_rows
        self._nb_columns = nb_columns
        self._peons = peons
        self._create_grid()

        self._cells = []

        for i in range(self._nb_rows):
            self._cells.append([])
            for j in range(self._nb_columns):
                self._cells[i].append(None)

        for peon in self._peons:
            row_index, col_index = peon.position
            self._cells[row_index-1][col_index-1] = peon

    def _create_grid(self):
        for r in range(self._nb_rows):
            for c in range(self._nb_columns):
                boardcell = BoardCell(self._peons)
                cell = boardcell.create_cell(self._master)
                cell.grid(row=r, column=c)


class BoardCell:

    def __init__(self, peons=[]):
        self._peons = peons

    def create_cell(self, master):
        cell = ''
        if len(self._peons) > 0:
            for i in range(len(self._peons)):
                image = Image.open(self._peons[i].image())
                image_elem = ImageTk.PhotoImage(image)
                cell = tk.Button(master, image=image_elem)
                cell.image = image_elem
        else:
            image = Image.open('assets/icons/blank.png')
            image_elem = ImageTk.PhotoImage(image)
            cell = tk.Button(master, image=image_elem)
            cell.image = image_elem

        return cell
