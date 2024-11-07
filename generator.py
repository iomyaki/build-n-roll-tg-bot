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
    "Human": {"main": None, "secondary": None},  #all +1
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
    "Fire Genasi": {"main": "Intelligence", "secondary": "Charisma"},
    "Githyanki": {"main": "Strength", "secondary": "Intelligence"},
    "Githzerai": {"main": "Wisdom", "secondary": "Intelligence"},
    "Goblin": {"main": "Dexterity", "secondary": "Constitution"},
    "Hobgoblin": {"main": "Strength", "secondary": "Intelligence"},
    "Haregon": {"main": "Dexterity", "secondary": "Constitution"},
    "Kenku": {"main": "Dexterity", "secondary": "Wisdom"},
    "Kobold": {"main": "Dexterity", "secondary": "Intelligence"},
    "Lizardfolk": {"main": "Constitution", "secondary": "Wisdom"},
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
    "Half-Elf": {"main": "Charisma", "secondary": None},  #choose +1
    "Half-Orc": {"main": "Strength", "secondary": "Constitution"},
    "Bearfolk": {"main": "Strength", "secondary": "Constitution"},
    "Darakhul": {"main": "Constitution", "secondary": "Charisma"},
    "Erina": {"main": "Charisma", "secondary": "Dexterity"},
    "Quickstep": {"main": "Dexterity", "secondary": "Charisma"},
    "Ratatosk": {"main": "Dexterity", "secondary": "Wisdom"},
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


def get_optimal_race(character_class):
    """Return the character race that is most associated with the given character class."""
    if character_class not in class_characteristics:
        return "Unknown character class"

    class_feats = class_characteristics[character_class]
    main_feat = class_feats["main"]
    secondary_feat = class_feats["secondary"]

    best_races = []
    optimal_races = []

    for race, feats in race_feats.items():
        if feats["main"] == main_feat and feats["secondary"] == secondary_feat:
            best_races.append(race)
        if feats["main"] == main_feat:
            optimal_races.append(race)
        elif feats["secondary"] == secondary_feat:
            optimal_races.append(race)

    if not optimal_races and not best_races:
        return "No optimal race found for this class"

    if not best_races:
        return optimal_races
    return best_races


def get_character_class(character_race):
    """Return the character class that is most associated with the given character race."""
    if character_race not in race_feats:
        return "Unknown character race"

    race_feats_data = race_feats[character_race]
    main_feat = race_feats_data["main"]
    secondary_feat = race_feats_data["secondary"]

    best_classes = []
    optimal_classes = []

    for character_class, feats in class_characteristics.items():
        if feats["main"] == main_feat and feats["secondary"] == secondary_feat:
            best_classes.append(character_class)
        if feats["main"] == main_feat:
            optimal_classes.append(character_class)
        elif feats["secondary"] == secondary_feat:
            optimal_classes.append(character_class)

    if not optimal_classes and not best_classes:
        return "No optimal class found for this race"

    if not best_classes:
        return optimal_classes

    return best_classes


def get_character_background(character_race, character_class):
    """Return the character background that is most associated with the given character race and class."""

    if character_race not in race_feats:
        return "Unknown character race"

    if character_class not in class_characteristics:
        return "Unknown character class"

    race_feats_data = race_feats[character_race]
    class_feats_data = class_characteristics[character_class]

    race_main_feat = race_feats_data["main"]
    race_secondary_feat = race_feats_data["secondary"]
    class_main_feat = class_feats_data["main"]
    class_secondary_feat = class_feats_data["secondary"]

    best_backgrounds = []
    optimal_backgrounds = []

    for background, traits in background_feats.items():
        if traits["main"] == class_main_feat and traits["main"] == race_main_feat and traits[
            "secondary"] == class_secondary_feat and traits["secondary"] == race_secondary_feat:
            best_backgrounds.append(background)
        if (traits["main"] == class_main_feat or traits["main"] == race_main_feat) and (
                traits["secondary"] == class_secondary_feat or traits["secondary"] == race_secondary_feat):
            optimal_backgrounds.append(background)
        elif (traits["main"] != race_main_feat and traits["main"] != class_main_feat) and (
                traits["secondary"] == class_secondary_feat and traits["secondary"] == race_secondary_feat):
            optimal_backgrounds.append(background)

    if not optimal_backgrounds and not best_backgrounds:
        return "No optimal background found for this race and class"

    if not best_backgrounds:
        return optimal_backgrounds

    return best_backgrounds


def generate_character_attributes(character_class):
    """Generate random gender, age, and subclass for a character."""

    # List of genders
    genders = ("Male", "Female", "Not stated")

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


def get_random_race():
    """Randomly select a character race from the predefined races."""
    races = list(race_feats.keys())
    return random.choice(races)


def add_race_and_background_bonuses(assigned_scores, character_race, character_background):
    """Add racial and background bonuses to the character's ability scores."""

    # Define the mapping of ability names to their respective indices in the list
    ability_indices = {
        "Strength": 0,
        "Dexterity": 1,
        "Constitution": 2,
        "Intelligence": 3,
        "Wisdom": 4,
        "Charisma": 5
    }

    # Add race bonuses
    if character_race in race_feats:
        main_ability = race_feats[character_race]["main"]
        secondary_ability = race_feats[character_race]["secondary"]

        # Apply bonuses (assuming +2 for main and +1 for secondary)
        if main_ability != None:
            assigned_scores[ability_indices[main_ability]] += 2
        if secondary_ability != None:
            assigned_scores[ability_indices[secondary_ability]] += 1

    # Add background bonuses
    if character_background in background_feats:
        main_ability = background_feats[character_background]["main"]
        secondary_ability = background_feats[character_background]["secondary"]

        # Apply bonuses (assuming +2 for main and +1 for secondary)
        if main_ability != None:
            assigned_scores[ability_indices[main_ability]] += 2
        if secondary_ability != None:
            assigned_scores[ability_indices[secondary_ability]] += 1

    return assigned_scores


def random_generation():
    character = {}

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
        #print(f"\nClass: {character_class}")  # CLASS
        character["Class"] = character_class
        #print(f"Main Characteristic: {main_characteristics}")  # MAIN CHARACTERISTIC
        character["Main Characteristic"] = main_characteristics
        #print(f"Secondary Characteristic: {secondary_characteristics}")  # SECONDARY CHARACTERISTIC
        character["Secondary Characteristic"] = secondary_characteristics

        # Generate optimal race for class
        optimal_race = get_optimal_race(character_class)
        random.shuffle(optimal_race)
        character_race = optimal_race[0]
        #print(f"Race: {character_race}")  # RACE
        character["Race"] = character_race

        # Generate random subclass, age and gender
        for key, value in generate_character_attributes(character_class).items():
            #print(f"{key}: {value}")  # GENDER, AGE, SUBCLASS, PERSONALITY TRAIT
            character[key] = value

        # Generate optimal background for race and class
        optimal_background = get_character_background(character_race, character_class)
        random.shuffle(optimal_background)
        character_background = optimal_background[0]
        #print(f"Background: {character_background}")  # BACKGROUND
        character["Background"] = character_background

        # Roll ability scores
        scores = roll_ability_scores()
        ability_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        # Sort scores to find the highest and second highest
        sorted_scores = sorted(scores)
        main_score = sorted_scores[-1]
        secondary_score = sorted_scores[-2]
        #print("\nRolled Scores:")
        #print(*sorted_scores)

        # Assign the highest and second-highest scores to main and secondary characteristics
        main_index = ability_names.index(main_characteristics)
        secondary_index = ability_names.index(secondary_characteristics)

        # Create a new scores list with main and secondary scores assigned
        assigned_scores = [0 for _ in range(6)]
        assigned_scores[main_index] = main_score
        assigned_scores[secondary_index] = secondary_score

        # Fill in the remaining scores randomly
        remaining_scores = sorted_scores[:-2]
        random.shuffle(remaining_scores)

        # Assign remaining scores to the rest of the ability scores
        for i in range(6):
            if assigned_scores[i] == 0:
                assigned_scores[i] = remaining_scores.pop(0)

        # Add race and background bonuses
        assigned_scores = add_race_and_background_bonuses(assigned_scores, character_race, character_background)

        # Control that each of assigned scores not more than 20

        #print("\nAssigned Ability Scores:")
        for name, score in zip(ability_names, assigned_scores):
            #print(f"{name}: {score} (Modifier: {calculate_modifier(score)})")  # STATS
            character[name] = f"{score} (modifier: {calculate_modifier(score)})"

    else:
        print("Failed trying to generate character.")

    return character


def guided_generation(character_race, character_class, character_subclass, character_background):
    # Get all input information
    """print("\nPlease choose your race - if you don't want to choose just type None")
    character_race = str(input())
    print("Please choose your class - if you don't want to choose just type None")
    character_class = str(input())
    print("Choose your subclass - if you don't want to choose just type None")
    character_subclass = str(input())
    print("Please choose your background - if you don't want to choose just type None")
    character_background = str(input())"""

    character = {}

    #Generate additional information
    if character_race.lower() == "random" and character_class.lower() == "random":
        character_race = get_random_race()
    elif character_race.lower() == "random" and character_class.lower() != "random":
        optimal_race = get_optimal_race(character_class)
        random.shuffle(optimal_race)
        character_race = optimal_race[0]
    elif character_race.lower() != "random" and character_class.lower() == "random":
        optimal_class = get_character_class(character_race)
        random.shuffle(optimal_class)
        character_class = optimal_class[0]

    if character_background.lower() == "random":
        optimal_background = get_character_background(character_race, character_class)
        random.shuffle(optimal_background)
        character_background = optimal_background[0]

    if character_subclass.lower() == "random":
        character_subclass = random.choice(subclass_dict[character_class])

    #print("\nYour Character:")

    # Get characteristics
    characteristics = get_characteristics(character_class)
    main_characteristics = characteristics["main"]
    secondary_characteristics = characteristics["secondary"]

    # Output results
    if characteristics:
        #print(f"\nClass: {character_class}")
        character["Class"] = character_class
        #print(f"Main Characteristic: {characteristics['main']}")
        character["Main Characteristic"] = characteristics["main"]
        #print(f"Secondary Characteristic: {characteristics['secondary']}")
        character["Secondary Characteristic"] = characteristics["secondary"]

        #print(f"\nRace: {character_race}")
        character["Race"] = character_race

        for key, value in generate_character_attributes(character_class).items():
            if key == "Subclass":
                #print(f"{key}: {character_subclass}")
                character[key] = character_subclass
            else:
                #print(f"{key}: {value}")
                character[key] = value

        #print(f"Background: {character_background}")
        character["Background"] = character_background

        # Roll ability scores
        scores = roll_ability_scores()
        ability_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        # Sort scores to find the highest and second highest
        sorted_scores = sorted(scores)
        main_score = sorted_scores[-1]
        secondary_score = sorted_scores[-2]
        #print("\nRolled Scores:")
        #print(*sorted_scores)

        # Assign the highest and second-highest scores to main and secondary characteristics
        main_index = ability_names.index(main_characteristics)
        secondary_index = ability_names.index(secondary_characteristics)

        # Create a new scores list with main and secondary scores assigned
        assigned_scores = [0 for _ in range(6)]
        assigned_scores[main_index] = main_score
        assigned_scores[secondary_index] = secondary_score

        # Fill in the remaining scores randomly
        remaining_scores = sorted_scores[:-2]
        random.shuffle(remaining_scores)

        # Assign remaining scores to the rest of the ability scores
        for i in range(6):
            if assigned_scores[i] == 0:
                assigned_scores[i] = remaining_scores.pop(0)

        # Add race and background bonuses
        assigned_scores = add_race_and_background_bonuses(assigned_scores, character_race, character_background)

        # Control that each of assigned scores not more than 20

        #print("\nAssigned Ability Scores:")
        for name, score in zip(ability_names, assigned_scores):
            #print(f"{name}: {score} (Modifier: {calculate_modifier(score)})")
            character[name] = f"{score} (modifier: {calculate_modifier(score)})"

    else:
        print("Failed trying to generate character.")

    return character


"""def main():
    print("Welcome to the D&D Character Generator!")
    print("Please choose generation mode: random(1) or guided(2)")
    mode = int(input())
    if mode == 1:
        print(random_generation())
    elif mode == 2:
        guided_generation()
    else:
        print("Please choose correct mode!")


if __name__ == "__main__":
    main()"""
