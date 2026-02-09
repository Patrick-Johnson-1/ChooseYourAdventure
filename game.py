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

    def player_turn(self, action):
        if action == "attack":
            damage = self.__player.attack(self.__current_enemy)
            message = f"You dealt {damage:.1f} damage!"
            return True, message
        elif action == "use_potion":
            pass
        elif action == "run":
            pass