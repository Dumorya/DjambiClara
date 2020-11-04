class Board:

    def __init__(self, width, height):
        self.__cells = []

        for i in range(width):
            for j in range(height):
                self.__cells.append(None)

    def move(self, departure, arrival, ):
        pass