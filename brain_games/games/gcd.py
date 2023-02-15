import math
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 2
MAX_NUMBER = 50


def get_data():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num_one} {num_two}'
    correct_answer = str(math.gcd(num_one, num_two))
    return question, correct_answer
