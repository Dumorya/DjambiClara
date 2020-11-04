from abc import ABC


class Peon(ABC):

    def __init__(self, is_alive, color, position):
        self.__is_alive = is_alive
        self.__color = color
        self.__position = position

    def available_moves(self):
        pass

    def position(self):
        pass

    def action_after_move(self):
        pass



