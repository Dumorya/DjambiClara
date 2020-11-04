# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.board import Board
from classes.militant import Militant
from front.board_template import Application
import tkinter as tk



if __name__ == '__main__':
    print("Go")

nb_rows = 9
nb_columns = 9

root = tk.Tk()
app = Application(nb_rows, nb_columns, master=root)
app.mainloop()
board1 = Board(nb_rows, nb_columns)

militant1 = Militant(True, "yellow", [1, 7])
militant2 = Militant(True, "blue", [4, 6])
militant3 = Militant(True, "green", [1, 6])
militant4 = Militant(True, "red", [4, 6])


