import tkinter as tk

class Application(tk.Frame):

    def __init__(self, nb_rows, nb_columns, master=None):
        super().__init__(master)
        self.master = master
        self.nb_rows = nb_rows
        self.nb_columns = nb_columns
        self.create_grid()

    def create_grid(self):
        for r in range(self.nb_rows):
            for c in range(self.nb_columns):
                tk.Button().grid(row=r, column=c)