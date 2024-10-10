from model.characters.heroes.hero import Hero
from model.weapons.physical_weapon import Physical


class Warrior(Hero):

    def __init__(self, name: str, life: int, attack: int, weapon: Physical, outfit_defense: int = 0) -> None:
        super().__init__(name, life, attack, weapon, outfit_defense)

        if (not isinstance(self.get_weapon(), Physical)):
            raise Exception("Warriors can only use physical weapons")

    def get_name(self) -> str:
        return f"Warrior {super().get_name()}"
