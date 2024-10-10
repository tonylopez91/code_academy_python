from random import choice, randint
from fictional_names.name_generator import generate_name
from configs import configs

class Weapon:
  __name: str
  __damage: int
  __type: str
  __is_special: bool
  __special_effect = {
    'name': '',
    'damage': 0
  }

  def __init__(self, type) -> None:
    (min, max) = configs.weapons_damage_range
    self.__type = type
    self.__name = generate_name(style='orc', library=True)
    self.__damage = randint(min, max)
    self.set_special_effect()

  def action(self) -> tuple:# -> Any:
    raise NotImplementedError
  
  def get_name(self):
    return self.__name
  
  def get_type(self):
    return self.__type
    
  def get_damage(self):
    return self.__damage + self.__special_effect.get('damage', 0)
  
  def get_especial_effect(self):
    return self.__special_effect if self.__is_special else None
  
  def set_special_effect(self):
    if choice([True, False]):
      (min, max) = configs.special_effect_damage_range

      self.__is_special = True
      self.__special_effect['name'] = generate_name(style='aztec')
      self.__special_effect['damage'] = randint(min, max)
     
