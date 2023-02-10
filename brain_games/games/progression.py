from random import randint


RULES = 'What number is missing in the progression?'
LOWER_LIMIT = 1
START_UPPER_LIMIT = 20
STEP_UPPER_LIMIT = 10


def get_data():
    length = 10
    start = randint(LOWER_LIMIT, START_UPPER_LIMIT)
    step = randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    progression = get_progression(start, step, length)
    numbers_list = []

    for index in progression:
        numbers_list.append(str(index))
    correct_answer_index = randint(LOWER_LIMIT, len(numbers_list) - 1)
    correct_answer = numbers_list[correct_answer_index]
    numbers_list[correct_answer_index] = ".."
    question = ' '.join(numbers_list)
    return question, correct_answer


def get_progression(start, step, length):
    end = start + (length * step)
    return range(start, end, step)