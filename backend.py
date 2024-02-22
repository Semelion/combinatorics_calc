from itertools import product
from itertools import permutations
def rule_of_sum(numbers):
    # Проверяем, пуст ли список
    if not numbers:
        return 0
    # Рекурсивно применяем правило суммы
    return numbers[0] + rule_of_sum(numbers[1:])

def rule_of_multiplication(numbers):
    if not numbers:
        return 1

        # Рекурсивно применяем правило произведения
    return numbers[0] * rule_of_multiplication(numbers[1:])

def arrangements_with_replacement(choices, length):
    # Генерируем все возможные комбинации с повторениями
    all_arrangements = product(choices, repeat=length)
    return list(all_arrangements)


def arrangements_without_replacement(choices, length):
    # Генерируем все возможные перестановки без повторений
    all_arrangements = permutations(choices, length)
    return list(all_arrangements)


