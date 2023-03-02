import math
from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 50


def get_data():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
