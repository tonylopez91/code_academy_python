import sys
import time
from random import choice, randint

import questionary
from fictional_names.name_generator import generate_name, styles

from configs import configs
from model.characters import Warrior, Mage, Dragon, Ogre, Hero, Monster
from model.weapons import Physical, Magical


# This class should be split into more specific bits, 
# the mission could have been turned into a model 
# and most of the prompt logic could be moved
# to a specific service


class Game:
    __hero: Hero
    __heroes = {
        'Warrior': (Warrior, Physical),
        'Mage': (Mage, Magical)
    }
    __are_missions_left = True
    __monster_list: list[Monster] = []

    def __init__(self) -> None:
        self.prompt_welcome()
        self.generate_villains()

        self.prompt_hero_creation()
        self.prompt_set_missions()

    def generate_hero(self, hero_class, hero_name, weapon_type):
        (hero_init, weapon_init) = self.__heroes[hero_class]

        damage = choice(configs.characters_attack_range[hero_class])
        life = choice(configs.characters_life_range[hero_class])
        weapon = weapon_init(weapon_type)

        self.__hero = hero_init(hero_name, life, damage, weapon)

    def generate_villains(self):
        monsters = {
            'Dragon': Dragon,
            'Ogre': Ogre,
        }

        for i in range(configs.villains_amount):
            monster_type = choice(list(monsters.keys()))
            name = generate_name(style='greek', library=True)
            life = choice(configs.characters_life_range[monster_type])
            attack = choice(configs.characters_attack_range[monster_type])
            weakness = choice(configs.magic_element_list + configs.hand_weapons)
            weakness_damage = randint(10, 20)
            self.__monster_list.append(monsters[monster_type](name, life, attack, weakness, weakness_damage))

    def generate_hero_name(self, style):
        names = []
        for i in range(10):
            names.append(generate_name(style=style, library=True))
        return names

    def get_monsters(self):
        return self.__monster_list

    def get_hero(self):
        return self.__hero

    def prompt_welcome(self):
        print(configs.welcome_msg)

    def prompt_hero_creation(self):
        give_name_options = ['Yes', 'Generate one for me']
        give_name = questionary.select('Do you want to give your hero a name:', choices=give_name_options).ask()
        select_name_type = questionary.select('Select the style for the name of your hero:', styles)
        ask_name = questionary.text('Type your Hero name')

        if give_name == give_name_options[0]:
            hero_name = ask_name.ask()
        else:
            name_type = select_name_type.ask()
            hero_name = questionary.select('Select a name for your hero:', self.generate_hero_name(name_type)).ask()

        hero_class = questionary.select('Select a class for your hero:', list(self.__heroes.keys())).ask()

        weapon_type = questionary.select('Select your weapon:', list(configs.charaters_weapons[hero_class])).ask()
        self.generate_hero(hero_class, hero_name, weapon_type)

    def prompt_set_missions(self):
        while self.__are_missions_left:
            missions = [mission['mission'] for mission in configs.missions if mission['completed'] == False]

            mission_selected = questionary.select("Select a mission to start:", choices=missions + ['Quit']).ask()

            if mission_selected == 'Quit':
                self.dramatic_print('Thanks for playing :), See you soon!!')
                self.__are_missions_left = False
                break

            mission = [mission for mission in configs.missions if mission['mission'] == mission_selected].pop()
            mission_monster = [monster for monster in self.get_monsters() if
                               monster.get_type() == mission['monster']].pop()

            self.dramatic_print(mission['narration'])

            mission_actions = [actions['action'] for actions in mission['actions']]
            (is_hero_alive, is_monster_alive) = self.are_characters_alive(mission_monster)
            has_been_battle = False

            action = {}

            while is_hero_alive and is_monster_alive:

                action_selected = questionary.select("What will you do:", choices=mission_actions).ask()

                action = [m for m in mission['actions'] if m['action'] == action_selected].pop()

                if action['purpose'] == configs.hero_actions['Escape']:
                    escape = [purpose for purpose in action['actions'] if
                              purpose['result'] == action['purpose'] and purpose['damaged'] == has_been_battle].pop()
                    self.dramatic_print(escape['narration'])
                    break

                has_been_battle = True
                self.dramatic_print(action['narration'])
                self.hero_fight_monster(mission_monster)
                self.monster_fight_hero(mission_monster)

                (is_hero_alive, is_monster_alive) = self.are_characters_alive(mission_monster)

            if not is_monster_alive:
                mission['completed'] = True
                result = [acts for acts in action['actions'] if acts['result'] == 'victory'].pop()
                self.dramatic_print(result['narration'])

            if not is_hero_alive:
                result = [acts for acts in action['actions'] if acts['result'] == 'defeat'].pop()
                self.dramatic_print(result['narration'])
                self.dramatic_print('Better luck next time !!')

        self.dramatic_print('All missions are completed')
        return 0

    def dramatic_print(self, txt):
        for letter in txt:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n')

    def are_characters_alive(self, current_monster: Monster):
        hero_life = self.get_hero().get_life()
        monster_life = current_monster.get_life()
        return hero_life > 0, monster_life > 0

    def hero_fight_monster(self, monster_to_fight: Monster):
        hero = self.get_hero()
        self.dramatic_print(
            f'{hero.get_name()} will strike {monster_to_fight.get_name()} with your mighty weapon {hero.get_weapon().get_name()}')

        (damage, material) = hero.attack()
        monster_to_fight.receive_attack(damage, material)
        self.dramatic_print(
            f'You manage to dealt {damage} points to {monster_to_fight.get_name()} now its life drops to: {monster_to_fight.get_life()} ')

    def monster_fight_hero(self, monster: Monster):
        hero = self.get_hero()
        self.dramatic_print(f'{monster.get_name()} is attacking {hero.get_name()}')

        (damage,) = monster.attack()
        hero.receive_attack(damage)
        self.dramatic_print(
            f'{monster.get_name()} has strike you down with {damage} points now your life drops to: {hero.get_life()} ')
