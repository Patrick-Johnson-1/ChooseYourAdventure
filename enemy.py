from character import Character

class Enemy(Character):
    def __init__(self, name, max_health,attack_power, defense, xp_reward, gold_reward):
        super().__init__(name, max_health, attack_power, defense)
        self.__xp_reward = xp_reward
        self.__gold_reward = gold_reward
    @property
    def xp_reward(self):
        return self.__xp_reward
    @property
    def gold_reward(self):
        return self.__gold_reward

    @staticmethod
    def create_goblin(level = 1):
        return Enemy(
            name=f"Goblin (Lv.{level})",
            max_health=30 + (level * 10),
            attack_power=8 + (level * 2),
            defense=2 + level,
            xp_reward=20 * level,
            gold_reward=10 * level
        )

    @staticmethod
    def create_orc(level=1):
        return Enemy(
            name=f"Orc (Lv.{level})",
            max_health=50 + (level * 15),  # Stronger than Goblin
            attack_power=12 + (level * 3),
            defense=5 + (level * 2),
            xp_reward=40 * level,
            gold_reward=25 * level
        )

    @staticmethod
    def create_dragon(level=1):
        return Enemy(
            name=f"Dragon (Lv.{level})",
            max_health=150 + (level * 30),  # Boss-tier
            attack_power=25 + (level * 5),
            defense=10 + (level * 3),
            xp_reward=200 * level,
            gold_reward=100 * level
        )

    def get_rewards(self):
        return  self.xp_reward, self.gold_reward