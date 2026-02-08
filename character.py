import random

class Character:
    def __init__(self, name, max_health,attack_power, defense):
        self.__name = name
        self.__max_health = max_health
        self.__current_health = max_health
        self.__attack_power = attack_power
        self.__defense = defense
        self.__is_alive = True

    def __str__(self):
        return f"{self.name} - HP: {self.current_health}/{self.max_health} | ATK: {self.attack_power} | DEF: {self.defense}"
    def __repr__(self):
        return f"Character(name='{self.name}' , hp={self.current_health}/{self.max_health})"
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

    def take_damage(self, damage):
        self.__current_health -= damage
        if self.__current_health <= 0:
            self.__is_alive = False
            self.__current_health = 0
        return damage

    def heal(self, amount):
        self.__current_health += amount
        self.__current_health = min(self.__max_health, self.__current_health)
        return amount

    def attack(self, target):
        damage = self.attack_power * random.uniform(.80,1.2)
        damage = damage  - target.defense
        damage = max(0, damage)
        target.take_damage(damage)
        return damage

    def get_health_percentage(self):
        return self.__current_health / self.__max_health * 100

hero = Character("Brave Knight", 100, 15, 5)
print(hero)
