import random

from configs.configs import weapon_materials
from model.weapons.weapon import Weapon


class Physical(Weapon):
    __material: str

    def __init__(self, type: str) -> None:
        super().__init__(type)
        self.__material = random.choice(weapon_materials)

    def get_material(self):
        return self.__material

    def action(self) -> tuple[int, str]:
        return (self.get_damage(), self.get_type())
