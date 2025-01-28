import itertools
import time
import math

def generate_permutations_algorithmic(points):
    """Алгоритмическое создание перестановок с учетом ограничений."""
    def permute(points, l, r, result):
        if l == r:
            if satisfies_constraints(points):  # Проверяем ограничение
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
    """Создание перестановок с помощью itertools с учетом ограничений."""
    return [list(perm) for perm in itertools.permutations(points) if satisfies_constraints(perm)]

def satisfies_constraints(permutation):
    """Проверяет, удовлетворяет ли перестановка заданным ограничениям."""
    # ограничения: точка P1 должна быть на первом или втором месте
    if "P1" in permutation:
        return permutation.index("P1") in [0, 1]
    return True

def objective_function(permutation):
    """Целевая функция для оценки перестановки."""
    # Пример: минимизируем расстояние между первой и последней точкой (условно их индексы)
    return abs(permutation.index("P1") - permutation.index("P5"))

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

# Находим оптимальное решение
best_permutation = min(permutations_pythonic, key=objective_function)
best_value = objective_function(best_permutation)
print(f"\nОптимальная перестановка: {best_permutation} с целевой функцией: {best_value}")
