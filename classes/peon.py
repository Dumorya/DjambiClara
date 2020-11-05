import abc


class Peon(abc.ABC):

    """A peon is made from moves, image, position, color and inherits from Peon"""

    def __init__(self, is_alive, color, position):
        self._is_alive = is_alive
        self._color = color
        self._position = position

    @abc.abstractmethod
    def available_moves(self):
        pass

    @property
    def position(self):
        return self._position

    @property
    def color(self):
        return self._color

    @abc.abstractmethod
    def action_after_move(self):
        pass

    @abc.abstractmethod
    def image(self):
        pass
