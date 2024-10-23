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

def python_functions_approach(points):
    return list(itertools.permutations(points))

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

print("Все возможные варианты обхода точек (алгоритмический подход):")
algorithmic_permutations = algorithmic_approach(points)
print(algorithmic_permutations)

print("Все возможные варианты обхода точек (подход с использованием функций Питона):")
python_functions_permutations = python_functions_approach(points)
print(python_functions_permutations)

#Часть 2 Ограничение:
#Расстояние между любыми двумя точками не должно превышать заданное значение
import itertools
import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_distance_constraint(permutation, max_distance):
    for i in range(len(permutation) - 1):
        if distance(permutation[i], permutation[i+1]) > max_distance:
            return False
    return True

def find_valid_tours(points, max_distance):
    valid_tours = []
    for permutation in itertools.permutations(points):
        if check_distance_constraint(permutation, max_distance):
            valid_tours.append(permutation)
    return valid_tours

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
max_distance = 3.0

print("Допустимые обходы:")
valid_tours = find_valid_tours(points, max_distance)
print(valid_tours)
