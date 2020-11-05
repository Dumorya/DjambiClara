from .peon import Peon


class Militant(Peon):

    """A militant is made from moves, image, position, color and inherits from Peon"""

    def __init__(self, is_alive, color, position):
        super().__init__(is_alive, color, position)
        self._is_alive = is_alive
        self._color = color
        self._position = position

    def available_moves(self):
        pass

    def action_after_move(self):
        pass

    @property
    def image(self):
        return "assets/icons/militant.png"
