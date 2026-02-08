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