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

    def enemy_turn(self):
        damage = self.__current_enemy.attack(self.__player)
        return f"{self.__current_enemy.name} dealt {damage:.1f} damage!"



    def player_turn(self, action):
        if action == "attack":
            damage = self.__player.attack(self.__current_enemy)
            message = f"You dealt {damage:.1f} damage!"
            return True, message
        elif action == "use_potion":
            potions = self.__player.inventory.get_potions()
            if len(potions) == 0:
                return (False, "No potions available!")

            potion = potions[0]  # Use first potion
            self.__player.inventory.remove_item(potion.name)
            self.__player.heal(potion.heal_amount)
            return (True, f"Used {potion.name}! Healed {potion.heal_amount} HP")
        elif action == "run":
            if random.random() < 0.5:  # 50% chance
                self.end_combat()
                self.__in_combat = False
                self.__current_enemy = None
                return (True, "You escaped!")
            else:
                return (False, "Failed to escape!")

    def save_game(self, filename):
        """Save game state to JSON file"""
        data = {
            "player_name": self.__player.name,
            "level": self.__player.level,
            "experience": self.__player.experience,
            "gold": self.__player.gold,
            "current_health": self.__player.current_health,
            "max_health": self.__player.max_health,
            "attack_power": self.__player.attack_power,
            "defense": self.__player.defense,
            "inventory": []
        }

        # Save inventory items
        for item in self.__player.inventory.get_items():
            if isinstance(item, Weapon):
                data["inventory"].append({
                    "type": "weapon",
                    "name": item.name,
                    "description": item.description,
                    "value": item.value,
                    "attack_bonus": item.attack_bonus
                })
            elif isinstance(item, Potion):
                data["inventory"].append({
                    "type": "potion",
                    "name": item.name,
                    "description": item.description,
                    "value": item.value,
                    "heal_amount": item.heal_amount
                })

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_game(self, filename):
        """Load game state from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)

        # Create new player
        self.__player = Player(data["player_name"])

        # Restore stats using name mangling
        self.__player._Player__level = data["level"]
        self.__player._Player__experience = data["experience"]
        self.__player._Player__gold = data["gold"]
        self.__player._Character__current_health = data["current_health"]
        self.__player._Character__max_health = data["max_health"]
        self.__player._Character__attack_power = data["attack_power"]
        self.__player._Character__defense = data["defense"]

        # Restore inventory
        for item_data in data["inventory"]:
            if item_data["type"] == "weapon":
                item = Weapon(
                    item_data["name"],
                    item_data["description"],
                    item_data["value"],
                    item_data["attack_bonus"]
                )
            elif item_data["type"] == "potion":
                item = Potion(
                    item_data["name"],
                    item_data["description"],
                    item_data["value"],
                    item_data["heal_amount"]
                )
            self.__player.inventory.add_item(item)
    @staticmethod
    def create_random_enemy(player_level):
        rand = random.random()
        if rand >= .90:
            return Enemy.create_dragon(level=player_level)
        elif  .75 <= rand <=.89:
            return Enemy.create_orc(level=player_level)
        else:
            return Enemy.create_goblin(level=player_level)


