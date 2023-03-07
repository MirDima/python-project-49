from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_even(random_number):
    return random_number % 2 == 0


def get_data():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer
