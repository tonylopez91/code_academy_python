from model.weapons.weapon import Weapon
from model.characters.villains.monster import Monster

class Dragon(Monster):
  def __init__(self, name: str, life: int, attack: int, weakness: str, weakness_damage: int, resistance: int = 100) -> None:
    super().__init__(name, life, attack, weakness, weakness_damage, resistance)
    self.__type = 'Dragon'
  
  def get_type(self):
    return self.__type

  def get_name(self) -> str:
    return f"{self.get_type()} {super().get_name()}"
  
