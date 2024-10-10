magic_element_list = (
    "Fire",
    "Water",
    "Earth",
    "Air",
    "Lightning",
    "Ice",
    "Light",
    "Darkness",
    "Arcane",
    "Nature",
    "Spirit",
    "Time",
    "Space",
    "Chaos",
    "Order",
    "Metal",
    "Sound",
    "Shadow",
    "Gravity",
    "Poison",
    "Blood",
    "Void",
    "Dream",
    "Illusion",
    "Necromancy",
    "Lunar",
    "Solar",
    "Storm",
    "Crystal",
    "Aether",
    "Steam",
    "Magnetism",
    "Plasma",
    "Energy",
    "Sand",
    "Thunder"
)
weapon_materials = (
    "Iron",
    "Gold",
    "Silver",
    "Copper",
    "Bronze",
    "Steel",
    "Mithril",
    "Adamantium",
    "Vibranium",
    "Orichalcum",
    "Platinum",
    "Titanium",
    "Lead",
    "Mercury",
    "Nickel",
    "Cobalt",
    "Electrum",
    "Tungsten",
    "Palladium",
    "Trillium",
    "Stygian Iron"
)

hand_weapons = (
    "Sword",
    "Dagger",
    "Axe",
    "Spear",
    "Mace",
    "Warhammer",
    "Longsword",
    "Katana",
    "Rapier",
    "Scimitar",
    "Halberd",
    "Claymore",
    "Flail",
    "Morningstar",
    "Trident",
    "Chakram",
    "Whip",
    "Nunchaku",
    "Kunai",
    "Glaive",
    "Quarterstaff",
    "Twin Blades",
    "Energy Blade",
    "Soul Reaver",
    "Bladed Gauntlet",
    "Dwarven War Axe",
    "Elven Bow",
    "Shadow Dagger",
    "Dragonfang Spear",
    "Void Blade"
)

magical_hand_weapons = (
    "Wand",
    "Staff",
    "Scepter",
    "Rod",
    "Orb",
    "Talisman",
    "Rune-carved Staff",
    "Crystal Wand",
    "Enchanted Cane",
    "Spellblade"
)

hand_actions = (
    "Swinging",
    "Thrusting",
    "Slashing",
    "Jabbing",
    "Hacking",
    "Striking",
    "Piercing",
    "Lunging",
    "Chopping",
    "Slicing"
)

magical_actions = (
    "Casting",
    "Channeling",
    "Summoning",
    "Enchanting",
    "Conjuring",
    "Divining",
    "Wielding",
    "Empowering",
    "Illuminating",
    "Transmuting"
)

villains_amount = 10

special_effect_damage_range = (5, 30)
weapons_damage_range = (70, 100)

characters_life_range = {
    'Warrior': (150, 200),
    'Mage': (100, 150),
    'Dragon': (250, 400),
    'Ogre': (150, 200),
}

characters_attack_range = {
    'Warrior': (15, 20),
    'Mage': (10, 15),
    'Dragon': (55, 70),
    'Ogre': (50, 65),
}

charaters_weapons = {
    'Warrior': hand_weapons,
    'Mage': magical_hand_weapons,
}

welcome_msg = """ 
Welcome, adventurer! 🌟

The realms are alive with magic, mystery, and danger.
As you step into this world of heroes and monsters, 
your choices will shape the fate of kingdoms. 

Gather your courage, sharpen your wits, and prepare 
for an epic journey where every decision matters.

Let the adventure begin! 
"""

hero_actions = {
    'Attack': 'attack',
    'Escape': 'escape'
}

missions = missions = (
    {
        "mission": "The Ogre’s Dungeon",
        "monster": 'Ogre',
        "completed": False,
        "resume": "Confront the ogre in its dungeon and end the terror it brings to the villagers.",
        "narration": (
            "You’ve tracked the fearsome ogre to its lair, deep within the dungeon’s dark tunnels. "
            "Now, with weapon in hand, you prepare to face the beast that has terrorized the village."
        ),
        "actions": [
            {
                "action": "Attack the ogre with your weapon",
                "purpose": "attack",
                "narration": (
                    "You charge at the ogre, weapon raised. The monster roars and prepares to strike back."
                ),
                "actions": [
                    {
                        "action": "Strike at the ogre's head",
                        "result": "victory",
                        "damaged": True,
                        "narration": (
                            "With a swift blow, you land a hit on the ogre’s head. "
                            "The beast collapses with a final roar, and the dungeon falls silent."
                        )
                    },
                    {
                        "action": "The ogre strikes you with its club",
                        "damaged": True,
                        "result": "defeat",
                        "narration": (
                            "The ogre swings its club, striking you down. Darkness envelops you, and your journey ends."
                        )
                    },
                    {
                        "action": "You take damage and flee the dungeon",
                        "result": "escape",
                        "damaged": True,
                        "narration": (
                            "The ogre’s hit knocks you to the ground. Realizing you're outmatched, "
                            "you flee the dungeon, wounded but alive."
                        )
                    }
                ]
            },
            {
                "action": "Try to sneak around the ogre",
                "purpose": "escape",
                "narration": (
                    "You move cautiously, hoping to sneak past the ogre unnoticed."
                ),
                "actions": [
                    {
                        "action": "Find a hidden path deeper into the cave",
                        "result": "escape",
                        "damaged": False,
                        "narration": (
                            "You find a narrow passage leading deeper into the dungeon. "
                            "The ogre doesn't notice as you slip through and find a hidden treasure."
                        )
                    },
                    {
                        "action": "You take damage and flee the dungeon",
                        "result": "escape",
                        "damaged": True,
                        "narration": (
                            "The ogre’s hit knocks you to the ground. Realizing you're outmatched, "
                            "you flee the dungeon, wounded but alive."
                        )
                    }
                ]
            }
        ]
    },
    {
        "mission": "The Dragon’s Lair",
        "monster": "Dragon",
        "completed": False,
        "resume": "Venture into the dragon’s lair, seeking treasure or battle with the legendary beast.",
        "narration": (
            "After journeying through treacherous mountains, you stand at the mouth of the dragon’s fiery lair. "
            "The air is thick with the promise of both danger and untold riches."
        ),
        "actions": [
            {
                "action": "Engage the dragon in battle",
                "purpose": "attack",
                "narration": (
                    "With a cry of challenge, you confront the mighty dragon. Its fiery breath fills the air."
                ),
                "actions": [
                    {
                        "action": "Deliver a final blow to the dragon",
                        "result": "victory",
                        "damaged": True,
                        "narration": (
                            "With a final strike, the dragon falls, and the treasure is yours. "
                            "You emerge victorious, your name destined to be legend."
                        )
                    },
                    {
                        "action": "The dragon strikes you down",
                        "result": "defeat",
                        "damaged": True,
                        "narration": (
                            "The dragon’s flames overwhelm you. "
                            "With a final breath, you fall to the ground, your journey at its end."
                        )
                    },
                    {
                        "action": "You take damage and flee",
                        "result": "escape",
                        "damaged": True,
                        "narration": (
                            "Badly injured, you barely escape the lair, leaving the treasure behind. "
                            "The dragon’s roar follows you, but you survive to fight another day."
                        )
                    }
                ]
            },
            {
                "action": "Stealthily approach the treasure",
                "purpose": "escape",
                "narration": (
                    "You move quietly, approaching the treasure while the dragon sleeps."
                ),
                "actions": [
                    {
                        "action": "Take a small piece of treasure and escape",
                        "result": "escape",
                        "damaged": False,
                        "narration": (
                            "You pocket a small gem and sneak out, escaping with the treasure while the dragon remains unaware."
                        )
                    },
                    {
                        "action": "You take damage and flee",
                        "result": "escape",
                        "damaged": True,
                        "narration": (
                            "Badly injured, you barely escape the lair, leaving the treasure behind. "
                            "The dragon’s roar follows you, but you survive to fight another day."
                        )
                    }
                ]
            }
        ]
    }
)
