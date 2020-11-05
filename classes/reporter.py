from .peon import Peon


class Reporter(Peon):

    def __init__(self, is_alive, color, position):
        super().__init__(is_alive, color, position)
        self.__is_alive = is_alive
        self.__color = color
        self.__position = position
        self.__image = 'assets/icons/reporter.png'

    def available_moves(self):
        pass

    def position(self):
        pass

    def action_after_move(self):
        pass




