import abc


class Peon(abc.ABC):

    def __init__(self, is_alive, color, position):
        self.__is_alive = is_alive
        self.__color = color
        self.__position = position
        self.__image = ''

    @abc.abstractmethod
    def available_moves(self):
        pass

    @abc.abstractmethod
    def position(self):
        pass

    @abc.abstractmethod
    def action_after_move(self):
        pass



