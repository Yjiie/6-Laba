"""
Есть требования:
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них на проверку того, что они являются вершинами квадрата.
"""
#Часть 1 
import itertools
import timeit

# Функция для алгоритмического подхода
def algorithmic_approach(points):
    permutations = []
    n = len(points)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    permutations.append(tuple(points[i] for i in indices[:]))
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                permutations.append(tuple(points[i] for i in indices[:]))
                break
        else:
            break
    return permutations

# Функция для подхода с использованием функций Питона
def python_functions_approach(points):
    return list(itertools.permutations(points))

# Функция для записи времени выполнения
def score_time(func, points):
    return timeit.timeit(lambda: func(points), number=1)

# Пример точек
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Измерение времени выполнения
algorithmic_time = score_time(algorithmic_approach, points)
python_functions_time = score_time(python_functions_approach, points)

# Вывод результатов
print(f"Алгоритмический подход: {algorithmic_time:.6f} сек")
print(f"Подход с использованием функций Питона: {python_functions_time:.6f} сек")


#Часть 2 Ограничение:
#Расстояние между любыми двумя точками не должно превышать заданное значение
import itertools
import timeit
import math

# Функция для вычисления расстояния между двумя точками
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Функция для проверки ограничения на расстояние
def check_distance_constraint(permutation, max_distance):
    for i in range(len(permutation) - 1):
        if distance(permutation[i], permutation[i+1]) > max_distance:
            return False
    return True

# Функция для нахождения всех допустимых обходов с ограничением
def find_valid_tours(points, max_distance):
    valid_tours = []
    for permutation in itertools.permutations(points):
        if check_distance_constraint(permutation, max_distance):
            valid_tours.append(permutation)
    return valid_tours

# Пример точек
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
max_distance = 3.0

# Измерение времени выполнения
start_time = timeit.default_timer()
valid_tours = find_valid_tours(points, max_distance)
end_time = timeit.default_timer()

# Вывод результатов
print(f"Допустимые обходы: {valid_tours}")
print(f"Время выполнения: {end_time - start_time:.6f} сек")

