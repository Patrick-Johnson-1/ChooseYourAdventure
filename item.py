class Item:
    def __init__(self, name, description, value):
        self.__name = name
        self.__description = description
        self.__value = value

    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def value (self):
        return self.__value
