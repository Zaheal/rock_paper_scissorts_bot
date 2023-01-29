import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from random import randint
from lexicon import RU_LEXICON


def choose_bot() -> str:
    rule_game: dict = {
        0: RU_LEXICON['rock'],
        1: RU_LEXICON['scissorts'],
        2: RU_LEXICON['paper']
    }
    r = randint(0, 2)

    return rule_game[r]
    

def choose_who_won(bot_choose: str, person_choose: str) -> str:
    rule_game: dict = {
        RU_LEXICON['rock']: RU_LEXICON['scissorts'],
        RU_LEXICON['scissorts']: RU_LEXICON['paper'],
        RU_LEXICON['paper']: RU_LEXICON['rock']
    }

    if bot_choose == person_choose:
        return 'draw'
    elif rule_game[person_choose][0] == bot_choose:
        return 'win'
    else:
        return 'lose'


    