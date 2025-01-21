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
                    # Ограничение: отфильтруем только те комбинации, где минимальная сторона квадрата больше 5
                    distances = [math.dist(subset[m], subset[n]) for m in range(4) for n in range(m + 1, 4)]
                    if min(distances) > 5 and is_square(subset):
                        squares.append(subset)
    return squares

# Функциональный подход
def generate_squares_functional(points):
    """Формирование квадратов с использованием функций Python."""
    squares = []
    for combination in itertools.combinations(points, 4):
        print(f"Проверяем комбинацию: {combination}")
        # Ограничение: отфильтруем только те комбинации, где минимальная сторона квадрата больше 5
        distances = [math.dist(combination[m], combination[n]) for m in range(4) for n in range(m + 1, 4)]
        if min(distances) > 5 and is_square(combination):
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

    # Целевая функция: максимизировать площадь квадрата
    def square_area(square):
        distances = sorted([math.dist(square[i], square[j]) for i in range(4) for j in range(i + 1, 4)])
        side = distances[0]  # Первая сторона (наименьшее расстояние среди равных)
        return side ** 2

    optimal_square = max(squares_functional, key=square_area, default=None)

    # Вывод результатов
    print(f"Квадраты (алгоритмический подход): {squares_algorithmic}")
    print(f"Время (алгоритмический подход): {time_algorithmic:.6f} секунд")
    
    print(f"Квадраты (функциональный подход): {squares_functional}")
    print(f"Время (функциональный подход): {time_functional:.6f} секунд")

    if optimal_square:
        print(f"Оптимальный квадрат (максимальная площадь): {optimal_square}")
        print(f"Площадь оптимального квадрата: {square_area(optimal_square):.2f}")
    else:
        print("Оптимальный квадрат не найден.")

    # Сравнение времени выполнения
    print("\nСравнение времени выполнения:")
    print(f"Функциональный подход быстрее на {((time_algorithmic - time_functional) / time_algorithmic) * 100:.2f}%" if time_algorithmic > time_functional else f"Алгоритмический подход быстрее на {((time_functional - time_algorithmic) / time_functional) * 100:.2f}%")
