from character import Character
from inventory import Inventory

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 5)
        self.__level = 1
        self.__experience = 0
        self.__gold = 0
        self.__inventory = Inventory()

    @property
    def level(self):
        return self.__level
    @property
    def experience(self):
        return self.__experience
    @property
    def gold(self):
        return self.__gold
    @property
    def inventory(self):
        return  self.__inventory
