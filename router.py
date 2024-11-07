import random

from aiogram import Router
from aiogram.enums.poll_type import PollType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile, Message, PollAnswer, ReplyKeyboardRemove

import generator
from app import database as db
from app import kb
from app import llm

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
    background = State()
    spells = State()
    llm = State()
    quenta = State()
    portrait = State()


@r.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Welcome to D&D Assistant!\n\n"
        "Would you like to get your character completely random — or would you like to configure them?",
        reply_markup=kb.creation_mode()
    )
    await state.set_state(Form.creation_mode)


@r.message(Form.creation_mode)
async def handle_creation_mode(message: Message, state: FSMContext) -> None:
    if message.text == "Random":
        # generate random parameters
        character = generator.random_generation()

        # fill the form with generated data
        await state.update_data(
            answer_race=character["Race"],
            answer_class=character["Class"],
            answer_gender=character["Gender"],
            answer_age=character["Age"],
        )

        # compose the message
        summary = f"Form completed!\n\nYour character:"
        cnt = 1
        for key, value in character.items():
            summary += f"\n{cnt}. {key}: {value}."
            cnt += 1

        # send the message
        await message.answer(summary, reply_markup=ReplyKeyboardRemove())
        await message.answer(
            "Now you can generate a quenta or a portrait for your character, or quit",
            reply_markup=kb.use_llm()
        )

        # clear the FSM
        #await state.clear()
        await state.set_state(Form.llm)
    elif message.text == "Guided":
        await message.answer("Select the race of your character:", reply_markup=kb.select_race())
        await state.set_state(Form.race)
    else:
        await message.answer(
            "Please choose if you want to go random or configured:",
            reply_markup=kb.creation_mode(),
        )


@r.message(Form.race)
async def handle_race(message: Message, state: FSMContext) -> None:
    bot = message.bot

    if message.text not in generator.race_feats and message.text.lower() != "random":
        await message.answer(
            "Your input is not supported. Please select the race of your character:",
            reply_markup=kb.select_race(),
        )
        return

    reply = ""

    if message.text.lower() == 'random':
        await bot.send_dice(message.chat.id, emoji='🎲')
        selected_race = random.choice(list(generator.race_feats))
        reply = f"You character's race is {selected_race}\n"
    else:
        selected_race = message.text

    await state.update_data(answer_race=selected_race)
    await message.answer(reply + "Select the class of your character:", reply_markup=kb.select_class())
    await state.set_state(Form.char_class)


@r.message(Form.char_class)
async def handle_class(message: Message, state: FSMContext) -> None:
    bot = message.bot

    if message.text not in generator.class_characteristics and message.text.lower() != "random":
        await message.answer(
            "Your input is not supported. Please the class of your character:",
            reply_markup=kb.select_class(),
        )
        return

    reply = ""

    if message.text.lower() == "random":
        await bot.send_dice(message.chat.id, emoji="🎲")
        selected_class = random.choice(list(generator.class_characteristics))
        reply = f"You character's class is {selected_class}\n"
    else:
        selected_class = message.text

    await state.update_data(answer_class=selected_class)
    await message.answer(reply + "Select the subclass of your character:",
                         reply_markup=kb.select_subclass(selected_class))
    await state.set_state(Form.subclass)


@r.message(Form.subclass)
async def handle_subclass(message: Message, state: FSMContext) -> None:
    bot = message.bot

    user_data = await state.get_data()
    char_class = user_data.get("answer_class")
    char_race = user_data.get("answer_race")

    if not char_race:
        await message.answer(
            "Error: race is not selected. Please select the race (or restart the bot if this keeps happening):",
            reply_markup=kb.select_race()
        )
        await state.set_state(Form.race)
        return

    if not char_class or char_class not in generator.subclass_dict:
        await message.answer(
            "Error: class is not selected. Please select the class (or restart the bot if this keeps happening):",
            reply_markup=kb.select_class()
        )
        await state.set_state(Form.char_class)
        return

    if message.text not in generator.subclass_dict[char_class] and message.text.lower() != "random":
        await message.answer(
            "Your input is not supported. Please select the subclass of your character:",
            reply_markup=kb.select_subclass(char_class)
        )
        return

    reply = ""

    if message.text.lower() == "random":
        await bot.send_dice(message.chat.id, emoji="🎲")
        selected_subclass = random.choice(generator.subclass_dict[char_class])
        reply = f"You character's subclass is {selected_subclass}\n"
    else:
        selected_subclass = message.text

    await state.update_data(answer_subclass=selected_subclass)
    possible_backgrounds = generator.get_character_background(char_race, char_class)
    await state.update_data(possible_backgrounds=possible_backgrounds)
    await message.answer(reply + "Select your character's background:",
                         reply_markup=kb.select_background(possible_backgrounds))
    await state.set_state(Form.background)


@r.message(Form.background)
async def handle_background(message: Message, state: FSMContext) -> None:
    bot = message.bot

    user_data = await state.get_data()
    possible_backgrounds = user_data.get("possible_backgrounds")

    if message.text not in possible_backgrounds and message.text.lower() != "random":
        await message.answer(
            "Your input is not supported. Please select the background of your character:",
            reply_markup=kb.select_background(possible_backgrounds)
        )
        return

    if message.text.lower() == "random":
        await bot.send_dice(message.chat.id, emoji="🎲")
        selected_background = random.choice(possible_backgrounds)
        await message.answer(f"You character's subclass is {selected_background}")
    else:
        selected_background = message.text

    await state.update_data(answer_background=selected_background)

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

    # get character's parameters
    data = await state.get_data()
    character = generator.guided_generation(
        data["answer_race"],
        data["answer_class"],
        data["answer_subclass"],
        data["answer_background"],
    )

    # fill the form with generated data
    await state.update_data(
        answer_gender=character["Gender"],
        answer_age=character["Age"],
    )

    # compose the message
    summary = f"Form completed!\n\nYour character:"
    cnt = 1
    for key, value in character.items():
        summary += f"\n{cnt}. {key}: {value}."
        cnt += 1
    summary += f"\n{cnt}. Spells: {', '.join(data['answer_spells'])}."

    # send the message
    await poll_answer.bot.send_message(poll_answer.user.id, summary)
    await poll_answer.bot.send_message(
        poll_answer.user.id,
        "Now you can create a quenta and/or a portrait for your character, or quit",
        reply_markup=kb.use_llm()
    )

    await state.set_state(Form.llm)


@r.message(Form.llm)
async def handle_llm(message: Message, state: FSMContext) -> None:
    if message.text.lower() == "generate quenta":
        await message.answer(
            "Enter keywords to generate character's quenta (separated by comma):",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(Form.quenta)
    elif message.text.lower() == "generate portrait":
        await message.answer(
            "Enter keywords to generate character's portrait (separated by comma):",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(Form.portrait)
    elif message.text.lower() == "quit":
        await message.answer("Farewell! To use the bot again, type /start", reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return
    else:
        await message.answer(
            "Your input is not supported. Please select one of the options:",
            reply_markup=kb.use_llm()
        )
        return


@r.message(Form.quenta)
async def handle_quenta(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    quenta = llm.generate_quenta(
        data["answer_race"],
        data["answer_class"],
        data["answer_gender"],
        data["answer_age"],
        message.text,
    )
    await message.answer("Here's the story of your character:", reply_markup=ReplyKeyboardRemove())
    await message.answer(quenta, reply_markup=kb.use_llm())
    await state.set_state(Form.llm)


@r.message(Form.portrait)
async def handle_portrait(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    prompt = ("frameless, only one single image, one single character without others, detailed full face illustration, "
              f"close-up portrait, isolated on pure background, race {data['answer_race']}, "
              f"class {data['answer_class']}, gender {data['answer_gender']}, age {data['answer_age']}, "
              f"additional info: {message.text}")
    img = llm.generate_portrait(prompt, random.randint(0, 2000000000))
    await message.answer("Here's the portrait of your character:", reply_markup=ReplyKeyboardRemove())
    await message.bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile(path=img),
        reply_markup=kb.use_llm(),
    )
    await state.set_state(Form.llm)


@r.message()
async def answer(message: Message) -> None:
    await message.answer("Sorry, I can't get it")
