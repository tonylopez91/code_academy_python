class Character:
    base_attack: int
    name: str
    life: int

    def __init__(self, name: str, life: int, attack: int) -> None:
        self.name = name
        self.life = life
        self.base_attack = attack

    def get_name(self) -> str:
        return self.name

    def get_life(self) -> int:
        return self.life

    def get_attack(self) -> int:
        return self.base_attack

    def is_alive(self) -> bool:
        return self.life > 0

    def attack(self) -> tuple:
        raise NotImplementedError

    def receive_attack(self, damage_to_recieve):
        raise NotImplementedError
