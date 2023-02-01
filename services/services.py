import random
import sqlite3

from lexicon import RU_LEXICON
from aiogram.types import Message


def _choose_bot() -> str:
    result = random.choice([RU_LEXICON['rock'], RU_LEXICON['paper'], RU_LEXICON['scissorts']])

    return result    


def choose_who_won(person_choose: str) -> str:
    rule_game: dict = {
        RU_LEXICON['rock']: RU_LEXICON['scissorts'],
        RU_LEXICON['scissorts']: RU_LEXICON['paper'],
        RU_LEXICON['paper']: RU_LEXICON['rock']
    }
    bot_choose: str = _choose_bot()

    if bot_choose == person_choose:
        return 'draw'
    elif rule_game[person_choose] == bot_choose:
        return 'win'
    else:
        return 'lose'


def create_users_db(message: Message):
    try:
        db = sqlite3.connect(r'database/users.sqlite')
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id BIGINT PRIMARY KEY,
            count_game INT,
            count_win INT);
        """)

        cursor.execute('SELECT user_id FROM users WHERE user_id=?', (message.from_user.id, ))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (message.from_user.id, 0, 0))
        
        db.commit()

        db.close()
    except sqlite3.Error as error:
        print("Ошибка в create", error)
    finally:
        if db:
            db.close()



def add_count_game(message: Message):
    try:
        db = sqlite3.connect(r'database/users.sqlite')
        cursor = db.cursor()

        cursor.execute("UPDATE users SET count_game = count_game + ? WHERE user_id=?", (1, message.from_user.id))
        db.commit()

        db.close()
    except sqlite3.Error as error:
        print("Ошибка в add_count_game", error)
    finally:
        if db:
            db.close()

def add_count_win(message: Message):
    try:
        db = sqlite3.connect(r'database/users.sqlite')
        cursor = db.cursor()

        cursor.execute("UPDATE users SET count_win = count_win + ? WHERE user_id=?;", (1, message.from_user.id))
        db.commit()
        
        db.close()
    except sqlite3.Error as error:
        print('Ошибка в add_count_win', error)
    finally:
        if db:
            db.close()
