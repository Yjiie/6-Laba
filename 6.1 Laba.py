"""
Есть требования:
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

На плоскости задано К точек. Сформировать все возможные варианты обхода этих точек.
"""
import itertools
import time

def generate_permutations_algorithmic(points):
    """Алгоритмическое создание перестановок."""
    def permute(points, l, r, result):
        if l == r:
            result.append(points[:])  # Создаем копию текущего состояния
        else:
            for i in range(l, r + 1):
                points[l], points[i] = points[i], points[l]  # Меняем местами элементы
                permute(points, l + 1, r, result)
                points[l], points[i] = points[i], points[l]  # Возвращаем порядок обратно

    result = []
    permute(points, 0, len(points) - 1, result)
    return result

def generate_permutations_pythonic(points):
    """Создание перестановок с помощью itertools."""
    return list(map(list, itertools.permutations(points)))

# Задаем точки
k = 5  # Количество точек 
points = [f"P{i}" for i in range(1, k + 1)]

print(f"Точки: {points}\n")

# 1. Алгоритмический метод
start_time = time.time()
permutations_algorithmic = generate_permutations_algorithmic(points)
algorithmic_time = time.time() - start_time
print(f"Алгоритмический метод: {len(permutations_algorithmic)} перестановок за {algorithmic_time:.6f} секунд.")
print("\nВсе перестановки (алгоритмический метод):")
for perm in permutations_algorithmic:
    print(perm)

# 2. Метод с помощью Python функций
start_time = time.time()
permutations_pythonic = generate_permutations_pythonic(points)
pythonic_time = time.time() - start_time
print(f"\nPython функции: {len(permutations_pythonic)} перестановок за {pythonic_time:.6f} секунд.")
print("\nВсе перестановки (Python функции):")
for perm in permutations_pythonic:
    print(perm)

