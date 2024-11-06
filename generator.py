import random

# Dictionary mapping D&D classes to their main and secondary characteristics
class_characteristics = {
    "Barbarian": {"main": "Strength", "secondary": "Constitution"},
    "Bard": {"main": "Charisma", "secondary": "Dexterity"},
    "Cleric": {"main": "Wisdom", "secondary": "Constitution"},
    "Druid": {"main": "Wisdom", "secondary": "Dexterity"},
    "Fighter": {"main": "Strength", "secondary": "Constitution"},
    "Monk": {"main": "Dexterity", "secondary": "Wisdom"},
    "Paladin": {"main": "Strength", "secondary": "Charisma"},
    "Ranger": {"main": "Dexterity", "secondary": "Wisdom"},
    "Rogue": {"main": "Dexterity", "secondary": "Intelligence"},
    "Sorcerer": {"main": "Charisma", "secondary": "Constitution"},
    "Warlock": {"main": "Charisma", "secondary": "Wisdom"},
    "Wizard": {"main": "Intelligence", "secondary": "Wisdom"},
}

race_feats = {
    "Dwarf": {"main": "Constitution", "secondary": None},
    "Elf": {"main": "Dexterity", "secondary": None},
    "Halfling": {"main": "Dexterity", "secondary": None},
    "Human": {"main": None, "secondary": None}, #all +1
    "Aasimar": {"main": "Charisma", "secondary": None},
    "Dragonborn": {"main": "Strength", "secondary": "Charisma"},
    "Gnome": {"main": "Intelligence", "secondary": None},
    "Goliath": {"main": "Strength", "secondary": "Constitution"},
    "Orc": {"main": "Strength", "secondary": "Constitution"},
    "Tiefling": {"main": "Charisma", "secondary": "Intelligence"},
    "Aarakocra": {"main": "Dexterity", "secondary": "Wisdom"},
    "Bugbear": {"main": "Strength", "secondary": "Dexterity"},
    "Centaur": {"main": "Strength", "secondary": "Wisdom"},
    "Air Genasi": {"main": "Dexterity", "secondary": "Wisdom"},
    "Changeling": {"main": "Charisma", "secondary": None},
    "Earth Genasi": {"main": "Constitution", "secondary": "Strength"},
    "Deep Gnome": {"main": "Intelligence", "secondary": "Dexterity"},
    "Duergar": {"main": "Strength", "secondary": "Constitution"},
    "Eladrin": {"main": "Dexterity", "secondary": "Charisma"},
    "Firbolg": {"main": "Wisdom", "secondary": "Strength"},
    "Fairy": {"main": "Charisma", "secondary": None},
    "Fire Genasi": {"main": "Intelligence", "secondary": "Charisma"},
    "Githyanki": {"main": "Strength", "secondary": "Intelligence"},
    "Githzerai": {"main": "Wisdom", "secondary": "Intelligence"},
    "Goblin": {"main": "Dexterity", "secondary": "Constitution"},
    "Hobgoblin": {"main": "Strength", "secondary": "Intelligence"},
    "Haregon": {"main": "Dexterity", "secondary": "Constitution"},
    "Kenku": {"main": "Dexterity", "secondary": "Wisdom"},
    "Kobold": {"main": "Dexterity", "secondary": "Intelligence"},
    "Lizardfolk": {"main": "Constitution", "secondary": "Wisdom"},
    "Minotaur": {"main": "Strength", "secondary": "Constitution"},
    "Satyr": {"main": "Charisma", "secondary": "Dexterity"},
    "Sea Elf": {"main": "Dexterity", "secondary": "Wisdom"},
    "Shadar-kai": {"main": "Dexterity", "secondary": "Charisma"},
    "Shifter": {"main": "Dexterity", "secondary": "Strength"},
    "Tabaxi": {"main": "Dexterity", "secondary": "Charisma"},
    "Tortle": {"main": "Constitution", "secondary": None},
    "Triton": {"main": "Constitution", "secondary": "Charisma"},
    "Water Genasi": {"main": "Wisdom", "secondary": "Constitution"},
    "Yuan-ti": {"main": "Charisma", "secondary": "Intelligence"},
    "Kender": {"main": "Dexterity", "secondary": "Charisma"},
    "Astral Elf": {"main": "Dexterity", "secondary": "Intelligence"},
    "Autognome": {"main": "Constitution", "secondary": "Intelligence"},
    "Giff": {"main": "Strength", "secondary": "Constitution"},
    "Hadozee": {"main": "Dexterity", "secondary": "Strength"},
    "Plasmoid": {"main": "Constitution", "secondary": None},
    "Thri-kreen": {"main": "Dexterity", "secondary": "Wisdom"},
    "Owlin": {"main": "Wisdom", "secondary": "Dexterity"},
    "Lineages": {"main": None, "secondary": None},  # Comment: Multiple characteristics
    "Leonin": {"main": "Strength", "secondary": "Constitution"},
    "Satyr": {"main": "Charisma", "secondary": "Dexterity"},
    "Kalashtar": {"main": "Wisdom", "secondary": "Charisma"},
    "Warforged": {"main": "Constitution", "secondary": "Strength"},
    "Verdan": {"main": "Charisma", "secondary": "Constitution"},
    "Loxodon": {"main": "Constitution", "secondary": "Strength"},
    "Minotaur": {"main": "Strength", "secondary": "Constitution"},
    "Simic Hybrid": {"main": "Constitution", "secondary": "Intelligence"},
    "Vedalken": {"main": "Intelligence", "secondary": "Wisdom"},
    "Feral Tiefling": {"main": "Dexterity", "secondary": "Charisma"},
    "Locathah": {"main": "Wisdom", "secondary": "Constitution"},
    "Grung": {"main": "Dexterity", "secondary": "Constitution"},
    "Gith": {"main": "Intelligence", "secondary": "Wisdom"},
    "Half-Elf": {"main": "Charisma", "secondary": None}, #choose +1
    "Half-Orc": {"main": "Strength", "secondary": "Constitution"},
    "Bearfolk": {"main": "Strength", "secondary": "Constitution"},
    "Darakhul": {"main": "Constitution", "secondary": "Charisma"},
    "Erina": {"main": "Charisma", "secondary": "Dexterity"},
    "Quickstep": {"main": "Dexterity", "secondary": "Charisma"},
    "Ratatosk": {"main": "Dexterity", "secondary": "Wisdom"},
    "Ravenfolk": {"main": "Wisdom", "secondary": "Dexterity"},
    "Satarre": {"main": "Charisma", "secondary": "Intelligence"},
    "Shade": {"main": "Dexterity", "secondary": "Charisma"},
    "Shadow Goblin": {"main": "Dexterity", "secondary": "Charisma"},
    "Naga": {"main": "Wisdom", "secondary": "Intelligence"},
    "Fairy": {"main": "Charisma", "secondary": None},
    "Nymph": {"main": "Charisma", "secondary": "Wisdom"},
    "Siren": {"main": "Charisma", "secondary": "Dexterity"},
    "Ravenfolk": {"main": "Wisdom", "secondary": "Dexterity"},
    "Medusa": {"main": "Charisma", "secondary": "Dexterity"},
    "Mindflayer": {"main": "Intelligence", "secondary": "Charisma"},
    "Awakened": {"main": "Intelligence", "secondary": "Wisdom"},
}

background_feats = {
    "Acolyte": {"main": "Wisdom", "secondary": "Charisma"},
    "Charlatan": {"main": "Dexterity", "secondary": "Intelligence"},
    "Criminal": {"main": "Dexterity", "secondary": "Charisma"},
    "Entertainer": {"main": "Charisma", "secondary": "Dexterity"},
    "Folk Hero": {"main": "Strength", "secondary": "Charisma"},
    "Guild Artisan": {"main": "Intelligence", "secondary": "Charisma"},
    "Hermit": {"main": "Wisdom", "secondary": "Intelligence"},
    "Noble": {"main": "Charisma", "secondary": "Intelligence"},
    "Outlander": {"main": "Strength", "secondary": "Wisdom"},
    "Sage": {"main": "Intelligence", "secondary": "Wisdom"},
    "Sailor": {"main": "Strength", "secondary": "Dexterity"},
    "Soldier": {"main": "Strength", "secondary": "Constitution"},
    "Urchin": {"main": "Dexterity", "secondary": "Wisdom"},
    "Inheritor": {"main": None, "secondary": None},  # Comment: Multiple characteristics
    "Feylost": {"main": "Charisma", "secondary": "Wisdom"},
    "City Watch": {"main": "Wisdom", "secondary": "Charisma"},
    "Far Traveler": {"main": "Charisma", "secondary": "Intelligence"},
    "Noble": {"main": "Charisma", "secondary": "Intelligence"},
    "Mercenary Veteran": {"main": "Strength", "secondary": "Constitution"},
    "Haunted One": {"main": "Wisdom", "secondary": "Charisma"},
    "Recluse": {"main": "Intelligence", "secondary": "Wisdom"},
    "Urban Bounty Hunter": {"main": "Dexterity", "secondary": "Charisma"},
}

subclass_dict = {
    "Barbarian": [
        "Berserker",
        "Totem Warrior",
        "Ancestral Guardian",
        "Storm Herald",
        "Zealot",
        "Beast",
    ],
    "Bard": [
        "Lore",
        "Valor",
        "Swords",
        "College of Whispers",
        "Glamour",
        "Creation",
    ],
    "Cleric": [
        "Life",
        "Light",
        "Nature",
        "War",
        "Trickery",
        "Knowledge",
        "Arcana",
        "Forge",
        "Grave",
    ],
    "Druid": [
        "Circle of the Moon",
        "Circle of the Land",
        "Circle of Spores",
        "Circle of Stars",
        "Circle of Wildfire",
    ],
    "Fighter": [
        "Champion",
        "Battle Master",
        "Eldritch Knight",
        "Arcane Archer",
        "Cavalier",
        "Samurai",
        "Rune Knight",
        "Echo Knight",
    ],
    "Monk": [
        "Way of the Open Hand",
        "Way of Shadow",
        "Way of the Four Elements",
        "Way of the Drunken Master",
        "Way of the Kensei",
        "Way of the Astral Self",
        "Way of the Sun Soul",
    ],
    "Paladin": [
        "Oath of Devotion",
        "Oath of the Ancients",
        "Oath of Vengeance",
        "Oath of Conquest",
        "Oath of Redemption",
        "Oath of Glory",
        "Oath of the Crown",
    ],
    "Ranger": [
        "Hunter",
        "Beast Master",
        "Gloom Stalker",
        "Horizon Walker",
        "Monster Slayer",
    ],
    "Rogue": [
        "Thief",
        "Assassin",
        "Arcane Trickster",
        "Inquisitive",
        "Mastermind",
        "Swashbuckler",
        "Phantom",
        "Soulknife",
    ],
    "Sorcerer": [
        "Draconic Bloodline",
        "Wild Magic",
        "Divine Soul",
        "Shadow Magic",
        "Storm Sorcery",
        "Aberrant Mind",
        "Clockwork Soul",
    ],
    "Warlock": [
        "The Archfey",
        "The Fiend",
        "The Great Old One",
        "The Celestial",
        "The Hexblade",
        "The Fathomless",
        "The Genie",
    ],
    "Wizard": [
        "School of Abjuration",
        "School of Conjuration",
        "School of Divination",
        "School of Enchantment",
        "School of Evocation",
        "School of Illusion",
        "School of Necromancy",
        "School of Transmutation",
        "School of War Magic",
    ],
}

def roll_ability_scores():
    """Roll 4d6 and drop the lowest die to generate an ability score."""
    scores = []
    for _ in range(6):
        roll = sorted([random.randint(1, 6) for _ in range(4)])
        score = sum(roll[1:])  # Drop the lowest die
        scores.append(score)
    return scores

def calculate_modifier(score):
    """Calculate the ability modifier from the ability score."""
    return (score - 10) // 2

def get_characteristics(character_class):
    """Return the main and secondary characteristics for the given character class."""
    return class_characteristics.get(character_class, None)

def get_race_feats(character_class):
    """Return the character race that is most associated with the given character class."""
    if character_class not in class_characteristics:
        return "Unknown character class"

    class_feats = class_characteristics[character_class]
    main_feat = class_feats["main"]
    secondary_feat = class_feats["secondary"]

    optimal_races = []

    for race, feats in race_feats.items():
        if feats["main"] == main_feat:
            optimal_races.append(race)
        elif feats["secondary"] == secondary_feat:
            optimal_races.append(race)

    if not optimal_races:
        return "No optimal race found for this class"

    return optimal_races

def get_character_class(character_race):
    """Return the character class that is most associated with the given character race."""
    if character_race not in race_feats:
        return "Unknown character race"

    race_feats_data = race_feats[character_race]
    main_feat = race_feats_data["main"]
    secondary_feat = race_feats_data["secondary"]

    optimal_classes = []

    for character_class, feats in class_characteristics.items():
        if feats["main"] == main_feat:
            optimal_classes.append(character_class)
        elif feats["secondary"] == secondary_feat:
            optimal_classes.append(character_class)

    if not optimal_classes:
        return "No optimal class found for this race"

    return optimal_classes

def get_character_background(character_race, character_class):
    """Return the character background that is most associated with the given character race and class."""

    if character_race not in race_feats:
        return "Unknown character race"

    if character_class not in class_characteristics:
        return "Unknown character class"

    race_feats_data = race_feats[character_race]
    class_feats_data = class_characteristics[character_class]

    main_feat = race_feats_data["main"]
    secondary_feat = race_feats_data["secondary"]

    optimal_backgrounds = []

    for background, traits in background_feats.items():
        if traits["main"] == main_feat or traits["secondary"] == main_feat:
            optimal_backgrounds.append(background)
        elif traits["main"] == secondary_feat or traits["secondary"] == secondary_feat:
            optimal_backgrounds.append(background)

    if not optimal_backgrounds:
        return "No optimal background found for this race and class"

    return optimal_backgrounds

def generate_character_attributes(character_class):
    """Generate random gender, age, and subclass for a character."""

    # List of genders
    genders = ["Male", "Female", "Not stated"]

    # Generate a random gender
    gender = random.choice(genders)

    # Generate a random age (example ranges, can be adjusted based on race/class)
    age = random.randint(18, 100)  # Assuming characters can be between 18 and 100 years old

    # Personality traits (examples, can be expanded)
    personality_traits = [
        "Lawful Good", "Neutral Good", "Chaotic Good",
        "Lawful Neutral", "True Neutral", "Chaotic Neutral",
        "Lawful Evil", "Neutral Evil", "Chaotic Evil",
    ]

    # Generate a random personality trait
    personality_trait = random.choice(personality_traits)

    # Check if the provided class is valid and get its subclasses
    if character_class not in subclass_dict:
        return "Unknown character class"

    # Choose a random subclass from the provided class
    subclass = random.choice(subclass_dict[character_class])

    return {
        "Gender": gender,
        "Age": age,
        "Subclass": subclass,
        "Personality Trait": personality_trait
    }

def get_random_class():
    """Randomly select a character class from the predefined classes."""
    classes = list(subclass_dict.keys())
    return random.choice(classes)

def random_genaration():
    # Get user input
    #character_class = input("Enter your D&D character class: ").strip().title()

    #Generate random class
    character_class = get_random_class()

    # Get characteristics
    characteristics = get_characteristics(character_class)
    main_characteristics = characteristics["main"]
    secondary_characteristics = characteristics["secondary"]

    # Output results
    if characteristics:
        print(f"Class: {character_class}")
        print(f"Main Characteristic: {characteristics['main']}")
        print(f"Secondary Characteristic: {characteristics['secondary']}")

        #Generate random subclass, age and gender
        for key, value in generate_character_attributes(character_class).items():
            print(f"{key}: {value}")

        # Roll ability scores
        scores = roll_ability_scores()
        ability_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        # Sort scores to find the highest and second highest
        sorted_scores = sorted(scores)
        main_score = sorted_scores[-1]
        secondary_score = sorted_scores[-2]
        print("\nRolled Scores:")
        print(*sorted_scores)

        # Assign the highest and second highest scores to main and secondary characteristics
        main_index = ability_names.index(main_characteristics)
        secondary_index = ability_names.index(secondary_characteristics)

        # Create a new scores list with main and secondary scores assigned
        assigned_scores = [0] * 6
        assigned_scores[main_index] = main_score
        assigned_scores[secondary_index] = secondary_score

        # Fill in the remaining scores randomly
        remaining_scores = sorted_scores[:-2]
        random.shuffle(remaining_scores)

        # Assign remaining scores to the rest of the ability scores
        for i in range(6):
            if assigned_scores[i] == 0:
                assigned_scores[i] = remaining_scores.pop(0)

        print("\nAssigned Ability Scores:")
        for name, score in zip(ability_names, assigned_scores):
            print(f"{name}: {score} (Modifier: {calculate_modifier(score)})")

    else:
        print("Invalid class name. Please enter a valid D&D character class.")
    return

def guided_generation():
    return

def main():
    print("Welcome to the D&D Character Generator!")
    print("Please choose generation mode: random(1) or guided(2)")
    mode = int(input())
    if mode == 1:
        random_genaration()
    elif mode == 2:
        guided_generation()
    else:
        print("Please choose correct mode!")

if __name__ == "__main__":
    main()
