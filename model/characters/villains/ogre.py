from model.characters.villains.monster import Monster


class Ogre(Monster):
    def __init__(self, name: str, life: int, attack: int, weakness: str, weakness_damage: int,
                 resistance: int = 250) -> None:
        super().__init__(name, life, attack, weakness, weakness_damage, resistance)
        self.__type = 'Ogre'

    def get_type(self):
        return self.__type

    def get_name(self) -> str:
        return f"{self.get_type()} {super().get_name()}"
