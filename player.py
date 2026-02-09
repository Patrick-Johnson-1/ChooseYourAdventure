from character import Character
from inventory import Inventory

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 5)
        self.__level = 1
        self.__experience = 0
        self.__gold = 0
        self.__inventory = "PlaceHolder"

