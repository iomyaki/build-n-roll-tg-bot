import logging

from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, PollAnswer
from aiogram.enums.poll_type import PollType

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app import database as db
from app import kb

import generator

r = Router()
spells = [
    "Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights",
    "Druidcraft", "Eldritch Blast", "Encode Thoughts",
]
poll_answers = {}


class Form(StatesGroup):
    random_or_configured = State()
    race = State()
    char_class = State()
    subclass = State()
    spells = State()


@r.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        f"Hello! Would you like to get your character completely random — or would you like to configure them?",
        reply_markup=kb.creation_mode()
    )

    await state.set_state(Form.random_or_configured)


@r.message(Form.random_or_configured)
async def random_form(message: Message, state: FSMContext) -> None:
    if message.text == "Random":
        await message.answer(
            "Your character form is ready! *sends character form*",
            reply_markup=ReplyKeyboardRemove(),
        )
        # TODO: generate random char here
        await state.clear()
    elif message.text == "Configured":
        await message.answer("Select the race of your character:", reply_markup=kb.select_race())
        await state.set_state(Form.race)
    else:
        await message.answer("Plese choose if you want to go random or configured", reply_markup=kb.creation_mode())


@r.message(Form.race)
async def handle_race(message: Message, state: FSMContext) -> None:
    if message.text not in generator.race_feats:
        await message.answer("That is not supported. Please select the race of your character:", reply_markup=kb.select_race())
        return
    await state.update_data(answer_race=message.text)
    await message.answer("Select the class of your character:", reply_markup=kb.select_class())
    await state.set_state(Form.char_class)


@r.message(Form.char_class)
async def handle_class(message: Message, state: FSMContext) -> None:
    if message.text not in generator.class_characteristics:
        await message.answer("That is not supported. Please select the class of your character:", reply_markup=kb.select_class())
        return
    char_class = message.text
    bot_message = "Select the subclass of your character:"
    await state.update_data(answer_class=char_class)
    await message.answer(bot_message, reply_markup=kb.select_subclass(char_class))
    await state.set_state(Form.subclass)


@r.message(Form.subclass)
async def handle_subclass(message: Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    char_class = user_data.get('answer_class')

    if not char_class:
        await message.answer("Error -- class is not selected. Please select the class (or restart the bot if this keeps happening):", reply_markup=kb.select_class())
        await state.set_state(Form.char_class)
        return

    if message.text not in generator.subclass_dict[char_class]:
        await message.answer("That is not supported. Please select the subclass of your character:", reply_markup=kb.select_subclass(char_class))
        return

    bot = message.bot
    await state.update_data(answer_subclass=message.text)

    poll_message = await bot.send_poll(
        chat_id=message.chat.id,
        question="Select spells for your character to cast:",
        options=spells,
        is_anonymous=False,
        allows_multiple_answers=True,
        type=PollType.REGULAR,
        reply_markup=ReplyKeyboardRemove(),
    )

    poll_answers[poll_message.poll.id] = {}

    await state.set_state(Form.spells)


@r.poll_answer(Form.spells)
async def handle_spells(poll_answer: PollAnswer, state: FSMContext) -> None:
    bot = poll_answer.bot
    poll_id = poll_answer.poll_id
    user_id = poll_answer.user.id
    selected_options = poll_answer.option_ids

    options = spells
    selected_text = [options[i] for i in selected_options]

    poll_answers[poll_id][user_id] = selected_text

    data = await state.get_data()
    summary = (f"Form completed!\n\nYour character:"
               f"\n1. Race: {data['answer_race']}.\n2. Class: {
                   data['answer_class']}."
               f"\n3. Subclass: {data['answer_subclass']}.\n4. Spells: {', '.join(selected_text)}.")

    await bot.send_message(user_id, summary)

    await state.clear()


@r.message()
async def answer(message: Message) -> None:
    await message.answer("Sorry, I can't get it")
