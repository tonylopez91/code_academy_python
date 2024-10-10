from model.characters.character import Character

class Monster(Character):
  __type = 'Monster'
  __resistance: int
  __weakness: str
  __weakness_damage: int

  def __init__(self, name: str, life: int, attack: int, weakness: str , weakness_damage: int, resistance: int = 0) -> None:
    super().__init__(name, life, attack)
    self.life = life + resistance
    self.__resistance = resistance
    self.__weakness = weakness
    self.__weakness_damage = weakness_damage

  def get_type(self):
    return self.__type

  def get_resistance(self):
    return self.__resistance
  
  def get_weakness(self):
    return self.__weakness
  
  def get_weakness_damage(self):
    return self.__weakness_damage
  
  def recieve_attack(self, damage_to_recieve, weapon):
    weakness_value = 0 if self.get_weakness() != weapon else (self.get_weakness_damage() / 100) * (self.get_resistance() + self.get_life())

    resting_life = self.get_life() - damage_to_recieve - weakness_value
    
    self.life = 0 if resting_life <= 0 else resting_life
    return self.get_life()

  def attack(self):
    return (self.get_attack(),)