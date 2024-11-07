import sqlite3 as sq
from aiogram.types import User


db = sq.connect("app/dnd_test.db")
cur = db.cursor()


async def db_start() -> None:
    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, number_of_chars INTEGER DEFAULT 0);")
    db.commit()


async def check_user(user_id: int) -> None:
    cur.execute(f"SELECT user_id FROM users WHERE user_id = {user_id} LIMIT 1;")
    return cur.fetchone()


async def add_user(user: User) -> None:
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?);", (user.id,))
    db.commit()


async def get_characters_num(user_id: int) -> None:
    cur.execute(f"SELECT number_of_chars FROM users WHERE user_id = {user_id};")
    return cur.fetchone()


async def update_characters_num(user_id: int, number_of_chars: int):
    cur.execute(f"UPDATE users SET number_of_chars = {number_of_chars} WHERE user_id = {user_id};")
    db.commit()


async def add_user_character(character_dict: dict, user: User) -> None:
    cur.execute("""CREATE TABLE IF NOT EXISTS characters(
        character_id TEXT PRIMARY KEY,
        user_id INTEGER,
        name TEXT,
        class TEXT,
        level INTEGER DEFAULT 1,
        hp INTEGER DEFAULT 10,
        sex TEXT,
        race TEXT DEFAULT 'human',
        alignment TEXT,
        str INTEGER DEFAULT 10,
        dex INTEGER DEFAULT 10,
        con INTEGER DEFAULT 10,
        int INTEGER DEFAULT 10,
        wis INTEGER DEFAULT 10,
        cha INTEGER DEFAULT 10,
        proficiencies TEXT DEFAULT '',
        feats TEXT DEFAULT '',
        spells TEXT DEFAULT '',
        skills TEXT DEFAULT '');""")
    if 'character_id' in character_dict:
        #TODO
        db.commit()
        return
    else:
        cur.execute("""INSERT INTO characters (
            character_id,
            user_id,
            name,
            class,
            level,
            hp,
            sex,
            race,
            alignment,
            str,
            dex,
            con,
            int,
            wis,
            cha,
            proficiencies,
            feats,
            spells,
            skills
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            f"{user.id}+{get_characters_num(user.id)}",
            user.id,
            "name",
            character_dict["class"],
            character_dict["level"],
            '',
            character_dict["sex"],
            character_dict["race"],
            character_dict["alignment"],
            character_dict["str"],
            character_dict["dex"],
            character_dict["con"],
            character_dict["int"],
            character_dict["wis"],
            character_dict["cha"],
            '',
            '',
            '',
            '',

        ))
    db.commit()



async def get_spells(class_name, subclass_name, level) -> None:
    