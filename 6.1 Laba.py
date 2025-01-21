"""
Есть требования:
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них на проверку того, что они являются вершинами квадрата.
"""
import itertools
import time
import math

def is_square(points):
    """Проверка, образуют ли 4 точки квадрат."""
    if len(points) != 4:
        return False

    # Вычисляем все расстояния между точками
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.dist(points[i], points[j])
            distances.append(dist)

    distances.sort()

    # У квадрата должно быть 4 равных стороны и 2 равных диагонали
    if len(distances) != 6:
        return False

    side = distances[0]
    diagonal = distances[4]

    return (
        math.isclose(distances[0], side) and
        math.isclose(distances[1], side) and
        math.isclose(distances[2], side) and
        math.isclose(distances[3], side) and
        math.isclose(distances[4], diagonal) and
        math.isclose(distances[5], diagonal) and
        math.isclose(side * math.sqrt(2), diagonal)
    )

# Алгоритмический подход
def generate_squares_algorithmic(points):
    """Формирование квадратов алгоритмическим методом."""
    squares = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    subset = [points[i], points[j], points[k], points[l]]
                    print(f"Проверяем комбинацию: {subset}")
                    if is_square(subset):
                        squares.append(subset)
    return squares

# Функциональный подход
def generate_squares_functional(points):
    """Формирование квадратов с использованием функций Python."""
    squares = []
    for combination in itertools.combinations(points, 4):
        print(f"Проверяем комбинацию: {combination}")
        if is_square(combination):
            squares.append(combination)
    return squares

# Генерация случайных точек для теста
import random

def generate_random_points(k, x_range=(0, 100), y_range=(0, 100)):
    """Генерация K случайных точек."""
    points = [(random.randint(*x_range), random.randint(*y_range)) for _ in range(k // 2)]
    # Добавляем точки с потенциальной квадратной структурой
    for _ in range(k // 2):
        x, y = random.randint(*x_range), random.randint(*y_range)
        size = random.randint(5, 15)
        points.extend([(x, y), (x + size, y), (x, y + size), (x + size, y + size)])
    return random.sample(points, k)
# Основной блок
if __name__ == "__main__":
    K = 10  # Количество точек
    points = generate_random_points(K)
    print(f"Сгенерированные точки: {points}")

    # Измеряем время для алгоритмического подхода
    start_time = time.time()
    squares_algorithmic = generate_squares_algorithmic(points)
    time_algorithmic = time.time() - start_time

    # Измеряем время для функционального подхода
    start_time = time.time()
    squares_functional = generate_squares_functional(points)
    time_functional = time.time() - start_time

    # Вывод результатов
    
   # Вывод результатов
   
    print(f"Квадраты (алгоритмический подход): {squares_algorithmic}")
    print(f"Время (алгоритмический подход): {time_algorithmic:.6f} секунд")
    
    print(f"Квадраты (функциональный подход): {squares_functional}")
    print(f"Время (функциональный подход): {time_functional:.6f} секунд")

    # Сравнение времени выполнения
    print("\nСравнение времени выполнения:")
    print(f"Функциональный подход быстрее на {((time_algorithmic - time_functional) / time_algorithmic) * 100:.2f}%" if time_algorithmic > time_functional else f"Алгоритмический подход быстрее на {((time_functional - time_algorithmic) / time_functional) * 100:.2f}%")
