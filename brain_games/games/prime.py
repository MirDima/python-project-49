from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

RANGE_START = 2
RANGE_STEP = 1

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(random_number):
    if random_number < 2:
        return False
    for i in range(RANGE_START, random_number, RANGE_STEP):
        if random_number % i == 0:
            return False
    return True


def get_data():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer
