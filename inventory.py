from item import Weapon, Potion
class Inventory:
    def __init__(self, max_size=10):
        self.__items = []
        self.__max_size = max_size

    def add_item(self, item):
        if len(self.__items) < self.__max_size:
            self.__items.append(item)
            return True
        else:
            return False

    def remove_item(self, item_name):
            for item in self.__items:
                if item.name == item_name:
                    self.__items.remove(item)
                return item
            else:
                return None

    def get_item(self, item_name):
        for item in self.__items:
            if item.name == item_name:
                return item
        return None

    def is_full(self):
        return len(self.__items) == self.__max_size

    def get_items(self):
        return self.__items.copy()

    def get_potions(self):
        potions = []
        for item in self.__items:
            if isinstance(item, Potion):
                potions.append(item)
        return potions

    def get_weapons(self):
        weapons = []
        for item in self.__items:
            if isinstance(item, Weapon):
                weapons.append(item)
        return weapons

