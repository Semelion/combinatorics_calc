from itertools import product
from itertools import permutations

#для правила суммы
def rule_of_sum(numbers):
    # Проверяем, пуст ли список
    if not numbers:
        return 0
    # Рекурсивно применяем правило суммы
    return numbers[0] + rule_of_sum(numbers[1:])

#для правила произведения
def rule_of_multiplication(numbers):
    if not numbers:
        return 1

        # Рекурсивно применяем правило произведения
    return numbers[0] * rule_of_multiplication(numbers[1:])

#для размещений с повторениями
def arrangements_with_replacement(choices, length):
    # Генерируем все возможные комбинации с повторениями
    all_arrangements = product(choices, repeat=length)
    return len(list(all_arrangements))

#для размещений без повторений
def arrangements_without_replacement(choices, length):
    # Генерируем все возможные перестановки без повторений
    all_arrangements = permutations(choices, length)
    return len(list(all_arrangements))

#для сочетаний с повторениями
def next_combination(combination, n):
    k = len(combination)
    for i in range(k-1, -1, -1):
        if combination[i] < n-1:
            break
    else:
        return None
    combination[i] += 1
    for j in range(i+1, k):
        combination[j] = combination[i]
    return combination

def combination_generator(n, k):
    combination = [0]*k
    while combination is not None:
        yield combination
        combination = next_combination(combination, n)
    return None

def sequence_combination_generator(sequence, k):
    n = len(sequence)
    for comb in combination_generator(n, k):
        result = [sequence[i] for i in comb]
        yield result
    return None


# для сочетаний без повторений
def print_combination(k, n):
    comb_ls = []
    for i in range(k):
        comb_ls.append(i)
    comb_ls.append(n)
    comb_ls.append(0)
    while True:
        print(comb_ls[0:k])
        for j in range(len(comb_ls)-1):
            if comb_ls[j] + 1 == comb_ls[j+1]:
                comb_ls[j] = j
            else:
                break
        if j < k:
            comb_ls[j] += 1
        else:
            break
