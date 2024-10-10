# Os alunos devem criar um RPG onde heróis enfrentam monstros em batalhas. Cada tipo de herói tem suas próprias habilidades e cada monstro reage de maneira diferente aos ataques.

# Conceitos:

# Herança: Uma classe Personagem que serve de base para Heroi e Monstro.
# Polimorfismo: Heróis e monstros têm habilidades e comportamentos diferentes ao atacar e defender.
# Instruções:

# Crie uma classe base Personagem com atributos: nome, vida e ataque.
# Crie uma classe Heroi com subclasses: Guerreiro e Mago, onde cada um ataca de maneira diferente (por exemplo, Guerreiro usa espada, Mago usa magia).
# Crie uma classe Monstro com subclasses: Ogro e Dragao, onde cada um tem uma resistência ou fraqueza diferente.
# Crie um sistema de batalha onde o herói enfrenta o monstro até que um dos dois perca toda a vida.

# character 
  # hero
    # warrior
    # mage
  # monster
    # ogre
    # dragon

# character -> name, life, attack
  # hero -> ofensive_weapons, outfit
    # warrior -> sword, armor
    # mage -> magic, magic_drobe
  # monster -> stamina, weakness
    # ogre -> 200, sun
    # dragon -> 400, swords


from service.game import Game

game = Game()