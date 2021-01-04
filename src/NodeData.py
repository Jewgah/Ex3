class Node_data:

    def __init__(self, key: int, pos: tuple):
        self.__key = key
        self.__pos = pos
        self.tag = 0
        self.info = ""
        self.weight = 0

    def getKey(self) -> int:
        return self.__key

    def getpos(self) -> tuple:
        return self.__pos

    def __str__(self):
        return "Node_Data(id: %s , pos: %s  )" % (
            self.__key, self.__pos)
