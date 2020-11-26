# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.assassin import Assassin
from classes.chief import Chief
from classes.diplomate import Diplomate
from classes.militant import Militant
from classes.necromobile import Necromobile
from classes.reporter import Reporter
from classes.board import Board
import tkinter as tk

"""Main file in which all peons are implemented and the front is launched"""

if __name__ == '__main__':
    print("Djambi")

nb_rows = 9
nb_columns = 9

# Position are like followed : [row, column]

# MILITANTS #
militant_green1 = Militant(True, "green", [1, 3])
militant_green2 = Militant(True, "green", [2, 3])
militant_green3 = Militant(True, "green", [3, 1])
militant_green4 = Militant(True, "green", [3, 2])

militant_yellow1 = Militant(True, "yellow", [1, 7])
militant_yellow2 = Militant(True, "yellow", [2, 7])
militant_yellow3 = Militant(True, "yellow", [3, 8])
militant_yellow4 = Militant(True, "yellow", [3, 9])

militant_blue1 = Militant(True, "blue", [7, 1])
militant_blue2 = Militant(True, "blue", [7, 2])
militant_blue3 = Militant(True, "blue", [8, 3])
militant_blue4 = Militant(True, "blue", [9, 3])

militant_red1 = Militant(True, "red", [7, 8])
militant_red2 = Militant(True, "red", [7, 9])
militant_red3 = Militant(True, "red", [8, 7])
militant_red4 = Militant(True, "red", [9, 7])

# CHIEFS #
chief_green = Chief(True, "green", [1, 1])

chief_yellow = Chief(True, "yellow", [1, 9])

chief_blue = Chief(True, "blue", [9, 1])

chief_red = Chief(True, "red", [9, 9])

# ASSASSINS #
assassin_green = Assassin(True, "green", [1, 2])

assassin_yellow = Assassin(True, "yellow", [1, 8])

assassin_blue = Assassin(True, "blue", [9, 2])

assassin_red = Assassin(True, "red", [9, 8])

# REPORTERS #
reporter_green = Reporter(True, "green", [2, 1])

reporter_yellow = Reporter(True, "yellow", [2, 9])

reporter_blue = Reporter(True, "blue", [8, 1])

reporter_red = Reporter(True, "red", [8, 9])

# NECROMOBILES #
necromobile_green = Necromobile(True, "green", [3, 3])

necromobile_yellow = Necromobile(True, "yellow", [3, 7])

necromobile_blue = Necromobile(True, "blue", [7, 3])

necromobile_red = Necromobile(True, "red", [7, 7])

# DIPLOMATES #
diplomate_green = Diplomate(True, "green", [2, 2])

diplomate_yellow = Diplomate(True, "yellow", [2, 8])

diplomate_blue = Diplomate(True, "blue", [8, 2])

diplomate_red = Diplomate(True, "red", [8, 8])

peons = [militant_blue1, militant_red1, militant_green1, militant_yellow1,
         militant_blue2, militant_red2, militant_green2, militant_yellow2,
         militant_blue3, militant_red3, militant_green3, militant_yellow3,
         militant_blue4, militant_red4, militant_green4, militant_yellow4,
         chief_red, chief_blue, chief_green, chief_yellow,
         diplomate_blue, diplomate_red, diplomate_green, diplomate_yellow,
         necromobile_blue, necromobile_green, necromobile_yellow, necromobile_red,
         reporter_blue, reporter_green, reporter_yellow, reporter_red,
         assassin_blue, assassin_green, assassin_red, assassin_yellow]

root = tk.Tk()
app = Board(nb_rows, nb_columns, peons, master=root)
app.mainloop()

