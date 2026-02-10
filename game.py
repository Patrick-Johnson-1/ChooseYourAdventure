from player import Player
from enemy import Enemy
from inventory import Inventory
from item import Weapon, Potion
import random
import json

class Game:
    def __init__(self, player_name):
        self.__player = Player(player_name)
        self.__current_enemy = None
        self.__in_combat = False
        self.__game_running = True
    def start_combat(self, enemy):
        self.__current_enemy = enemy
        self.__in_combat = True
    def rest(self):
        heal_amount = int(self.__player.max_health*.30)
        self.__player.heal(heal_amount)
        return f"You rest and recover {heal_amount} HP"
    def explore(self):
        rand = random.random()
        if rand <= 0.40:
            enemy = Game.create_random_enemy(self.__player.level)
            self.start_combat(enemy)
            return f"You encountered a {enemy.name}!"
        elif rand <= 0.70:  # 30% chance (0.40 to 0.70)
            gold_found = random.randint(10, 30)
            self.__player.add_gold(gold_found)
            return f"You found {gold_found} gold!"
        else:
            items = [
                Potion("Small Potion", "Restores 30 HP", 15, 30),
                Potion("Large Potion", "Restores 70 HP", 40, 70),
                Weapon("Iron Sword", "A sturdy blade", 50, 12)
            ]
            item = random.choice(items)
            self.__player.inventory.add_item(item)
            return f"You found a {item.name}!"

    def end_combat(self):
        if not self.__player.is_alive:
            self.__game_running = False
            return "GAME_OVER"
        if not self.__current_enemy.is_alive:
            xp, gold = self.__current_enemy.get_rewards()
            self.__player.gain_experience(xp)
            self.__player.add_gold(gold)
            self.__in_combat = False
            self.__current_enemy = None
            return f"Victory! Gained {xp} XP and {gold} gold!"


    def player_turn(self, action):
        if action == "attack":
            damage = self.__player.attack(self.__current_enemy)
            message = f"You dealt {damage:.1f} damage!"
            return True, message
        elif action == "use_potion":
            pass
        elif action == "run":
            pass

    @staticmethod
    def create_random_enemy(player_level):
        rand = random.random()
        if rand >= .90:
            return Enemy.create_dragon(level=player_level)
        elif  .75 <= rand <=.89:
            return Enemy.create_orc(level=player_level)
        else:
            return Enemy.create_goblin(level=player_level)


