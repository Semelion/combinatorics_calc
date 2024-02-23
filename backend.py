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

#для перестановки с повторениями
def arrangements_with_replacement(choices, length):
    # Генерируем все возможные комбинации с повторениями
    all_arrangements = product(choices, repeat=length)
    return len(list(all_arrangements))

#для перестановки без повторений
def arrangements_without_replacement(choices, length):
    # Генерируем все возможные перестановки без повторений
    all_arrangements = permutations(choices, length)
    return len(list(all_arrangements))

#для сочетаний с повторениями
def next_combination(combination, n):
    # combination - текущее сочетание с повторениями, n - максимальное значение, которое может принимать элемент сочетания
    # Возвращает: Cочетание с повторениями или None, если текущее сочетание является последним
    k = len(combination)
    # Ищу первый элемент сочетания, который меньше n-1, начиная с конца
    for i in range(k-1, -1, -1):
        if combination[i] < n-1:
            break
    else:
        # Если все элементы сочетания равны n-1, возвращаем None
        return None
    # Увеличиваю найденный элемент на  1 и заполняю все последующие элементы значением этого элемента
    combination[i] +=  1
    for j in range(i+1, k):
        combination[j] = combination[i]
    return combination

def combination_generator(n, k):
    combination = [0]*k
    count =  0  # Счетчик для подсчета комбинаций
    while combination is not None:
        count +=  1  # Увеличиваю счетчик на  1 при каждой новой комбинации
        combination = next_combination(combination, n)
    return count

def sequence_combination_generator(sequence, k):
    n = len(sequence)
    # Вызываю combination_generator для подсчета комбинаций
    count = combination_generator(n, k)
    return count


def count_combinations(k, n):
    comb_ls = []
    # Заполняю список начальными значениями
    for i in range(k):
        comb_ls.append(i)
    # Добавляю n в список, чтобы включить его в сочетания
    comb_ls.append(n)
    # Добавляю  0 в конец списка для упрощения  логики генерации сочетаний
    comb_ls.append(0)

    # Счетчик для подсчета сочетаний
    count =  0

    # Основной цикл генерации сочетаний
    while True:
        # Увеличиваю счетчик на  1 при каждом обновлении сочетания
        count +=  1

        # Цикл для обновления текущего сочетания
        for j in range(len(comb_ls)-1):
            # Если текущий элемент сочетания +  1 равен следующему элементу, обновляем текущий элемент значением индекса
            if comb_ls[j] +  1 == comb_ls[j+1]:
                comb_ls[j] = j
            else:
                # Если текущий элемент сочетания не может быть обновлен, прерываем цикл
                break
        # Если не получится обновить первый элемент сочетания, значит, все сочетания были сгенерированы
        if j < k:
            # Увеличиваю текущий элемент сочетания на  1
            comb_ls[j] +=  1
        else:
            # Если достигнут конец списка, прерываю основной цикл
            break

    return count
"""    
n =  5  
k =  3  
print(count_combinations(k, n))
"""
#для размещений с повторениями
def count_permutations(n, k):
    z = [0 for i in range(k)]
    count =  0
    while True:
        # Счетчик для подсчета размещений 
        count +=  1

        for i in range(k-1, -1, -1):
            if z[i] < n-1:
                break
        else:
            return count
        z[i] +=  1
        for j in range(i+1, k):
            z[j] =  0

    return count

"""
n = 5
k = 3
print(count_permutations(k,  n))
"""
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
