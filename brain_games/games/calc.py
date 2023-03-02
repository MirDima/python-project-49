from random import randint
from random import choice

GAME_RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_data():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(['+', '-', '*'])
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number1} {operator} {number2}'
    correct_answer = str(operator_result(number1, operator, number2))
    return question, correct_answer


def operator_result(number1, operator, number2):
    if operator == '+':
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    return result
