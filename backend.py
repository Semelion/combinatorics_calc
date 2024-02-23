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
    return list(all_arrangements)

#для размещений без повторений
def arrangements_without_replacement(choices, length):
    # Генерируем все возможные перестановки без повторений
    all_arrangements = permutations(choices, length)
    return list(all_arrangements)

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

#для размещений с повторениями 
def get_permutation (n, k):
    z = [0 for i in range(k)]
    while True:
        print (z)
        for i in range(k-1, -1,- 1):
            if z[i] < n-1:
                break
        else:
            return
        z[i] += 1
        for j in range(i+1, k):
            z[j] = 0 

#для размещений без повторений
def swap(sequence, i, j):
    sequence[i], sequence[j] = sequence[j], sequence[i]

def reverse(sequence, index):
    shift = index + 1
    n = len(sequence)
    for i in range((n - shift) // 2):
        sequence[shift + i], sequence[n - 1 - i] = sequence[n - 1 - i], sequence[shift + i]

def k_permutation_of_n(k, sequence):
    n = len(sequence)
    for j in range(k, n):
        if sequence[j] > sequence[k-1]:
            break
    else:
        j = n
    if j < n:
        swap(sequence, k-1, j)
        return sequence[:k:]
    else:
        reverse(sequence, k-1)
        for i in range(k-2, -1, -1):
            if sequence[i] < sequence[i+1]:
                break
        else:
            return None
        for j in range(n-1, 1, -1):
            if sequence[j] > sequence[i]:
                break
        swap(sequence, i, j)
        reverse(sequence, i)
        return sequence[:k:]
