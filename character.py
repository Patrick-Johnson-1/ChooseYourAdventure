class Character:
    def __init__(self, name, max_health,attack_power, defense):
        self.__name = name
        self.__max_health = max_health
        self.__current_health = max_health
        self.__attack_power = attack_power
        self.__defense = defense
        self.__is_alive = True


hero = Character("Brave Knight", 100, 15, 5)
print(hero)
