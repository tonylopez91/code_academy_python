import random

from configs.configs import magic_element_list
from model.weapons.weapon import Weapon


class Magical(Weapon):
    __magic_element_type: str

    def __init__(self, weapon_type) -> None:
        super().__init__(weapon_type)
        self.__magic_element_type = random.choice(magic_element_list)

    def get_magic_element_type(self):
        return self.__magic_element_type

    def action(self) -> tuple[int, str]:
        return self.get_damage(), self.__magic_element_type
