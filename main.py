# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.board import Board
from classes.militant import Militant
from front.board_template import Application
import tkinter as tk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

nb_rows = 9
nb_columns = 9

root = tk.Tk()
app = Application(nb_rows, nb_columns, master=root)
app.mainloop()
board1 = Board(nb_rows, nb_columns)
militant1 = Militant(True, "yellow", [4, 6])


