from random import choice
from lexicon import RU_LEXICON


def _choose_bot() -> str:
    result = choice([RU_LEXICON['rock'], RU_LEXICON['paper'], RU_LEXICON['scissorts']])

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
