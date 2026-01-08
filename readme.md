# D&D Assistant TG bot 🎲

The "D&D Assistant" Telegram bot brings you the joy of gaming. Not enough time to create a character and only 10 minutes left before the session? Yet again, your GM asks you not to create a fifth human fighter in the party? The "D&D Assistant" is here to help!

The bot is avaiable **[here](https://t.me/dnd_ai_assistant_bot)**.

## Adventure Description

"D&D Assistant" is a solution for character generation in *Dungeons & Dragons*. Our project allows you, via a Telegram bot, to generate a full-fledged, ready-to-play character sheet according to your chosen criteria. The user can either generate a completely random character or fill in some fields on the character sheet and have the rest generated so that they fit with what's already been chosen.

We know all too well how disappointing it is to create a character you thought was awesome, only to find out they’re absolutely useless because you picked a bunch of unnecessary or downright harmful spells. That’s why we’ve taken the liberty of suggesting a spell list that will make it as easy as possible for you to enjoy game content with your particular character.

(In the future, we plan to expand the list of available classes and backgrounds in our generator, and also add features to generate dungeon maps or even unexpected plot twists for your adventures.)

## The Advantages of Our Adventure

In addition to a free ticket to the Forgotten Realms, you get:
- Character backgrounds and avatars generated via YandexGPT API for full role-playing immersion.
- Access to homebrew and the ability to add your own house rules.
- The ability to balance stats, spells, and features based on community usefulness ratings.

We plan to store spell information in a database, and generate character stats using our own algorithm for efficient stat distribution and class/race selection. This way, a character created with our bot is guaranteed to be not only unique, but also comfortable to play in the game world.

## Self-hosted Deployment

Clone the repository:
```shell
git clone https://github.com/iomyaki/build-n-roll-tg-bot.git
```

### Using Docker

Build and run the Docker image:
```shell
docker compose up --build
```

### Without Docker

Install the dependencies:
```shell
pip install -r requirements.txt
```

Launch the bot:
```shell
python3 main.py
```

### Requirements

You will also need to specify your Telegram bot token, as well as API key and CATALOG_ID for YandexGPT, in the `.env` file.

For generating the character’s backstory and portrait, you will be asked to enter keywords for the generative model. You can enter anything, but keep in mind that your input will influence the generated result (sometimes in very unpredictable ways). You can generate a backstory and portrait for a character as many times as you want—it’s possible to adjust the keywords for the best result. The keywords message should not exceed 500 characters.

## Contribution

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## Developers

- GM (team lead, algorithm development) — Ivan Zolotnikov (*Иван Золотников*), [tg](https://t.me/Cat_of_Iello).
- Warlock (bot development) — Ivan Myakinkov (*Иван Мякиньков*), [tg](https://t.me/iomyaki).
- Fighter (spell database development) — Ivan Stupnitsky (*Иван Ступницкий*), [tg](https://t.me/YanagiRu).
- Wizard (API integration) — Matvey Bagrov (*Матвей Багров*), [tg](https://t.me/the_big_bagrovski).
- Monk (bot development, testing) — Alexander Kryukov (*Александр Крюков*).

## Presentation Materials

The project presentation is available [here](https://docs.google.com/presentation/d/1SUfxcJUfvSjAPUVbx636RNYPHiQ619aMU0qOwrFOLC0/edit?usp=sharing).

## Media about us

- [Dungeons, Dragons, and a Telegram Bot — ITMO Institute of Applied Computer Science](https://www.ipkn.itmo.ru/news/podzemelya-drakony-i-telegram-bot).
- [“Total Recall” and “WhiningMeter”: How the DevDays Fall 2024 hackathon went — ITMO Institute of Applied Computer Science](https://www.ipkn.itmo.ru/dd-fall2024).

## Recognition

<div align="center">
  <img src="https://github.com/user-attachments/assets/daadb78f-621c-46cc-8292-192af801861a" alt="Diploma" style="width:65%; height:auto">
</div>
