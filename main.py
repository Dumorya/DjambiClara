# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.assassin import Assassin
from classes.chef import Chef
from classes.diplomate import Diplomate
from classes.militant import Militant
from classes.necromobile import Necromobile
from classes.reporter import Reporter
from front.board_template import Application
import tkinter as tk



if __name__ == '__main__':
    print("Go")

nb_rows = 9
nb_columns = 9

root = tk.Tk()
app = Application(nb_rows, nb_columns, master=root)
app.mainloop()

# MILITANTS #
militant_green1 = Militant(True, "green", [1, 3])
militant_green2 = Militant(True, "green", [2, 3])
militant_green3 = Militant(True, "green", [3, 1])
militant_green4 = Militant(True, "green", [3, 2])

militant_yellow1 = Militant(True, "yellow", [1, 7])
militant_yellow2 = Militant(True, "yellow", [2, 7])
militant_yellow3 = Militant(True, "yellow", [3, 8])
militant_yellow4 = Militant(True, "yellow", [3, 9])

militant_blue1 = Militant(True, "blue", [7, 8])
militant_blue2 = Militant(True, "blue", [7, 9])
militant_blue3 = Militant(True, "blue", [8, 7])
militant_blue4 = Militant(True, "blue", [9, 7])

militant_red1 = Militant(True, "red", [7, 1])
militant_red2 = Militant(True, "red", [7, 2])
militant_red3 = Militant(True, "red", [8, 3])
militant_red4 = Militant(True, "red", [9, 3])


# CHIEFS #
chief_green = Chef(True, "green", [1, 1])

chief_yellow = Chef(True, "yellow", [1, 9])

chief_blue = Chef(True, "blue", [9, 1])

chief_red = Chef(True, "red", [9, 9])


# ASSASSINS #
assassin_green = Assassin(True, "green", [1, 2])

assassin_yellow = Assassin(True, "yellow", [1, 8])

assassin_blue = Assassin(True, "blue", [9, 8])

assassin_red = Assassin(True, "red", [9, 2])


# REPORTERS #
reporter_green = Reporter(True, "green", [2, 2])

reporter_yellow = Reporter(True, "yellow", [2, 9])

reporter_blue = Reporter(True, "blue", [8, 9])

reporter_red = Reporter(True, "red", [8, 1])


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