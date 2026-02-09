class Item:
    def __init__(self, name, description, value):
        self.__name = name
        self.__description = description
        self.__value = value
    def __str__(self):
        return f"{self.name} - {self.description} (Value: {self.value}g)"
    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def value (self):
        return self.__value

class Weapon(Item):
    def __init__(self, name, description, value, attack_bonus):
        super().__init__(name,description,value)
        self.__attack_bonus = attack_bonus
    def __str__(self):
        return f"{self.name} - ATK +{self.attack_bonus} ({self.description})"
    @property
    def attack_bonus(self):
        return self.__attack_bonus

class Potion(Item):
    def __init__(self, name, description, value, heal_amount):
        super().__init__(name,description,value)
        self.__heal_amount = heal_amount
    def __str__(self):
        return f"{self.name} - Heals +{self.heal_amount} ({self.description})"
    @property
    def heal_amount(self):
        return self.__heal_amount

