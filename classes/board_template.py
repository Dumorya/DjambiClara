import tkinter as tk


class BoardTemplate(tk.Frame):

    def __init__(self, nb_rows, nb_columns, master=None):
        super().__init__(master)
        self.__master = master
        self.__nb_rows = nb_rows
        self.__nb_columns = nb_columns
        self.__create_grid()

        self.__cells = []

        for i in range(self.__nb_rows):
            for j in range(self.__nb_columns):
                self.__cells.append(None)

    def __create_grid(self):
        for r in range(self.__nb_rows):
            for c in range(self.__nb_columns):
                tk.Button().grid(row=r, column=c)
