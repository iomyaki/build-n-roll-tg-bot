from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import generator


def creation_mode() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Random"),
                KeyboardButton(text="Guided"),
            ],
        ],
        resize_keyboard=True
    )


def build_keyboard(buttons_in_row: int, iterable: dict or set or list) -> list[list[KeyboardButton]]:
    cnt = 0
    keyboard = []
    row = []
    for element in iterable:
        row.append(KeyboardButton(text=element))
        cnt += 1

        if cnt % buttons_in_row == 0:
            keyboard.append(row)
            row = []
    if len(row) != 0:
        keyboard.append(row)

    return keyboard


def select_race() -> ReplyKeyboardMarkup:
    keyboard = build_keyboard(5, generator.race_feats)
    keyboard.append([KeyboardButton(text="Random")])
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def select_class() -> ReplyKeyboardMarkup:
    keyboard = build_keyboard(3, generator.class_characteristics)
    keyboard.append([KeyboardButton(text="Random")])
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def select_subclass(char_class) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=build_keyboard(5, generator.subclass_dict[char_class]),
        resize_keyboard=True,
    )
