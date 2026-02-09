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

    def gain_experience(self, amount):
        self.__experience += amount
        level_up_xp = 100 * self.__level
        if self.__experience >= level_up_xp:
            self.level_up()

    def level_up(self):
        self.__level+=1
        self.__experience = 0
        self._Character__max_health += 20
        self._Character__attack_power += 5
        self._Character__defense += 3
        self._Character__current_health = self._Character__max_health
        return True