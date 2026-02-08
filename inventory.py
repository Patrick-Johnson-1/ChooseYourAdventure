class Inventory:
    def __init__(self, max_size=10):
        self.__items = []
        self.__max_size = max_size

    def add_item(self, item):
        if len(self.__items) < 10:
            self.__items.append(self.__items)
            return True
        else:
            return False
    def remove_item(self, item_name):
        if item_name in self.__items:
            self.__items.remove(item_name)
            return self.__items.remove(item_name)
        else:
            return None
