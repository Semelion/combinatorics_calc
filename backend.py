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

