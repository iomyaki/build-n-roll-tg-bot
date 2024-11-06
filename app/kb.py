from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

spells = (
    "Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights",
    "Druidcraft", "Eldritch Blast", "Encode Thoughts",
)


def creation_mode() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Random"),
                KeyboardButton(text="Configured"),
            ],
        ],
        resize_keyboard=True
    )


def select_race() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Dwarf"),
                KeyboardButton(text="Elf"),
            ],
            [
                KeyboardButton(text="Halfling"),
                KeyboardButton(text="Human"),
            ],
        ],
        resize_keyboard=True
    )


def select_class() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Fighter"),
                KeyboardButton(text="Rogue"),
            ],
            [
                KeyboardButton(text="Sorcerer"),
                KeyboardButton(text="Wizard"),
            ],
        ],
        resize_keyboard=True
    )


def select_subclass_fighter() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Arcane Archer"),
                KeyboardButton(text="Battle Master"),
            ],
            [
                KeyboardButton(text="Cavalier"),
                KeyboardButton(text="Champion"),
            ],
        ],
        resize_keyboard=True
    )


def select_subclass_rogue() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Arcane Trickster"),
                KeyboardButton(text="Assassin"),
            ],
            [
                KeyboardButton(text="Inquisitive"),
                KeyboardButton(text="Mastermind"),
            ],
        ],
        resize_keyboard=True
    )


def select_subclass_sorcerer() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Aberrant Mind"),
                KeyboardButton(text="Clockwork Soul"),
            ],
            [
                KeyboardButton(text="Divine Soul"),
                KeyboardButton(text="Draconic Bloodline"),
            ],
        ],
        resize_keyboard=True
    )


def select_subclass_wizard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Bladesinging"),
                KeyboardButton(text="Chronurgy"),
            ],
            [
                KeyboardButton(text="Graviturgy"),
                KeyboardButton(text="Order of Scribes"),
            ],
        ],
        resize_keyboard=True
    )


"""def select_spells(selected_spells: set[str]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{'✅ ' if spell in selected_spells else ''}{spell}",
                    callback_data=f"toggle_{spell}",
                )
                for spell in spells
            ],
            [
                InlineKeyboardButton(
                    text="Submit",
                    callback_data="submit",
                )
            ],
        ],
    )
"""