class Character:
    def __init__(self, name, max_health,attack_power, defense):
        self.__name = name
        self.__max_health = max_health
        self.__current_health = max_health
        self.__attack_power = attack_power
        self.__defense = defense
        self.__is_alive = True

    def __str__(self):
        return f"{self.name} - HP: {self.max_health}/{self.current_health} | ATK: {self.attack_power} | DEF: {self.defense}"


    @property
    def name(self):
        return self.__name
    @property
    def max_health(self):
        return self.__max_health
    @property
    def current_health(self):
        return self.__current_health
    @property
    def attack_power(self):
        return self.__attack_power
    @property
    def defense(self):
        return self.__defense
    @property
    def is_alive(self):
        return self.__is_alive


hero = Character("Brave Knight", 100, 15, 5)
print(hero)
