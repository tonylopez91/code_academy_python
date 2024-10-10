from model.characters.heroes.hero import Hero
from model.weapons.magic_weapon import Magical


class Mage(Hero):
    def __init__(self, name: str, life: int, attack: int, weapon: Magical, outfit_defense: int = 0) -> None:
        super().__init__(name, life, attack, weapon, outfit_defense)

        if not isinstance(self.get_weapon(), Magical):
            raise Exception("Mages can only use magic weapons")

    def get_name(self) -> str:
        return f"Mage {super().get_name()}"
