from aiogram import Router
from aiogram.enums.poll_type import PollType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, PollAnswer, ReplyKeyboardRemove

import generator
from app import database as db
from app import kb

r = Router()
spells = [
    "Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights",
    "Druidcraft", "Eldritch Blast", "Encode Thoughts",
]


class Form(StatesGroup):
    creation_mode = State()
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
    await state.set_state(Form.creation_mode)


@r.message(Form.creation_mode)
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
        await message.answer(
            "Please choose if you want to go random or configured:",
            reply_markup=kb.creation_mode(),
        )


@r.message(Form.race)
async def handle_race(message: Message, state: FSMContext) -> None:
    if message.text not in generator.race_feats:
        await message.answer(
            "Your input is not supported. Please select the race of your character:",
            reply_markup=kb.select_race(),
        )
        return
    await state.update_data(answer_race=message.text)
    await message.answer("Select the class of your character:", reply_markup=kb.select_class())
    await state.set_state(Form.char_class)


@r.message(Form.char_class)
async def handle_class(message: Message, state: FSMContext) -> None:
    if message.text not in generator.class_characteristics:
        await message.answer(
            "Your input is not supported. Please the class of your character:",
            reply_markup=kb.select_class(),
        )
        return
    char_class = message.text
    await state.update_data(answer_class=char_class)
    await message.answer("Select the subclass of your character:", reply_markup=kb.select_subclass(char_class))
    await state.set_state(Form.subclass)


@r.message(Form.subclass)
async def handle_subclass(message: Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    char_class = user_data.get("answer_class")

    if not char_class:
        await message.answer(
            "Error: class is not selected. Please select the class (or restart the bot if this keeps happening):",
            reply_markup=kb.select_class()
        )
        await state.set_state(Form.char_class)
        return

    if message.text not in generator.subclass_dict[char_class]:
        await message.answer(
            "Your input is not supported. Please select the subclass of your character:",
            reply_markup=kb.select_subclass(char_class)
        )
        return

    bot = message.bot
    await state.update_data(answer_subclass=message.text)

    await bot.send_poll(
        chat_id=message.chat.id,
        question="Select spells for your character to cast:",
        options=spells,
        is_anonymous=False,
        allows_multiple_answers=True,
        type=PollType.REGULAR,
        reply_markup=ReplyKeyboardRemove(),
    )

    await state.set_state(Form.spells)


@r.poll_answer(Form.spells)
async def handle_spells(poll_answer: PollAnswer, state: FSMContext) -> None:
    await state.update_data(answer_spells=(spells[i] for i in poll_answer.option_ids))

    data = await state.get_data()
    summary = (f"Form completed!\n\nYour character:"
               f"\n1. Race: {data['answer_race']}.\n2. Class: {data['answer_class']}."
               f"\n3. Subclass: {data['answer_subclass']}.\n4. Spells: {', '.join(data['answer_spells'])}.")

    await poll_answer.bot.send_message(poll_answer.user.id, summary)
    await state.clear()


@r.message()
async def answer(message: Message) -> None:
    await message.answer("Sorry, I can't get it")
