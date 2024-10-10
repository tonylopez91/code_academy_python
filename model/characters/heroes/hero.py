import random

from configs.configs import hand_actions
from model.characters.character import Character
from model.weapons.weapon import Weapon


class Hero(Character):
    __weapon: Weapon
    __outfit_defense: int

    def __init__(self, name: str, life: int, attack: int, weapon: Weapon, outfit_defense: int = 0) -> None:
        super().__init__(name, life, attack)
        self.__weapon = weapon
        self.__outfit_defense = outfit_defense

    def get_weapon(self):
        return self.__weapon

    def get_outfit_defense(self):
        return self.__outfit_defense

    def recieve_attack(self, damage_to_recieve):
        resting_life = self.get_life() + self.get_outfit_defense() - damage_to_recieve

        self.life = 0 if resting_life <= 0 else resting_life
        return self.get_life()

    def attack(self):
        action = random.choice(hand_actions)
        weapon = self.get_weapon()
        print(f'{self.get_name()} is {action} the {weapon.get_type()} {weapon.get_name()} \n')
        (damage, material) = weapon.action()

        return (damage + self.get_attack(), material)
