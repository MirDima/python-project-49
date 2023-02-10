from random import randint
from random import choice

RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_data():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    operators = choice(['+', '-', '*'])
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num_one} {operators} {num_two}'
    correct_answer = str(operator_result(num_one, operators, num_two))
    return question, correct_answer


def operator_result(num_one, operators, num_two):
    if operators == '+':
        result = num_one + num_two
    if operators == '-':
        result = num_one - num_two
    if operators == '*':
        result = num_one * num_two
        return result
