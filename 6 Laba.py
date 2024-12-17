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
import time

# Вариант 1: Алгоритмическая реализация 
def generate_algorithmic(points):
    def generate(current, remaining):
        if len(remaining) == 0:
            permutations.append(list(current))
        else:
            for i in range(len(remaining)):
                generate(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    permutations = []
    generate([], points)
    return permutations

# Вариант 2: Использование встроенной функции itertools.permutations
def generate_permutations_python(points):
    return list(itertools.permutations(points))
#Часть 2
#  Ограничение: предел области
def valid_path(path, area_limit):
    for p in path:
        if not (area_limit[0] <= p[0] <= area_limit[2] and area_limit[1] <= p[1] <= area_limit[3]):
            return False
    return True

# Вариант 1: Алгоритмическая реализация с ограничениями
def generate_algorithmic_with_limit(points, area_limit):
    def generate(current, remaining):
        if len(remaining) == 0:
            if valid_path(current, area_limit):  # Проверка на корректность пути
                permutations.append(list(current))
        else:
            for i in range(len(remaining)):
                generate(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    permutations = []
    generate([], points)
    return permutations

# Вариант 2: Использование встроенной функции itertools.permutations с ограничениями
def generate_permutations_python_with_limit(points, area_limit):
    valid_permutations = []
    for perm in itertools.permutations(points):
        if valid_path(perm, area_limit):
            valid_permutations.append(perm)
    return valid_permutations

# Пример: 4 точки на плоскости
points = [(1, 2), (3, 4), (5, 6), (7, 8)] 
area_limit = (0, 0, 10, 10)  # Прямоугольная область (x_min, y_min, x_max, y_max)

# Измеряем время выполнения для алгоритмического варианта без ограничений
start_time = time.time()
algorithmic_permutations = generate_algorithmic(points)
algorithmic_time = time.time() - start_time

# Измеряем время выполнения для варианта с использованием функций Python без ограничений
start_time = time.time()
python_permutations = generate_permutations_python(points)
python_time = time.time() - start_time

# Выводим результаты времени для первой части
print(f"Алгоритмическая реализация без ограничений: {algorithmic_time:.6f} секунд")
print(f"Встроенная функция Python без ограничений: {python_time:.6f} секунд")

# Сравниваем скорости для первой части
if algorithmic_time < python_time:
    print("Алгоритмическая реализация без ограничений быстрее.")
elif algorithmic_time > python_time:
    print("Встроенная функция Python без ограничений быстрее.")
else:
    print("Обе реализации без ограничений работают с одинаковой скоростью.")
'''
# Выводим первые 5 перестановок для проверки без ограничений
print("Первые 5 перестановок (алгоритм без ограничений):", algorithmic_permutations[:5])
print("Первые 5 перестановок (Python без ограничений):", python_permutations[:5])
'''
# Измеряем время выполнения для алгоритмического варианта с ограничениями
start_time = time.time()
algorithmic_permutations_with_limit = generate_algorithmic_with_limit(points, area_limit)
algorithmic_time_with_limit = time.time() - start_time

# Измеряем время выполнения для варианта с использованием функций Python с ограничениями
start_time = time.time()
python_permutations_with_limit = generate_permutations_python_with_limit(points, area_limit)
python_time_with_limit = time.time() - start_time

# Выводим результаты времени для второй части (с ограничениями)
print(f"Алгоритмическая реализация с ограничениями: {algorithmic_time_with_limit:.6f} секунд")
print(f"Встроенная функция Python с ограничениями: {python_time_with_limit:.6f} секунд")

# Сравниваем скорости для второй части
if algorithmic_time_with_limit < python_time_with_limit:
    print("Алгоритмическая реализация с ограничениями быстрее.")
elif algorithmic_time_with_limit > python_time_with_limit:
    print("Встроенная функция Python с ограничениями быстрее.")
else:
    print("Обе реализации с ограничениями работают с одинаковой скоростью.")

# Выводим результаты для проверенных перестановок с ограничениями
print("Количество проверенных перестановок с ограничениями (алгоритм):", len(algorithmic_permutations_with_limit))
print("Количество проверенных перестановок с ограничениями (Python):", len(python_permutations_with_limit))
'''
# Выводим первые 5 перестановок для проверки с ограничениями
print("Первые 5 перестановок с ограничениями (алгоритм):", algorithmic_permutations_with_limit[:5])
print("Первые 5 перестановок с ограничениями (Python):", python_permutations_with_limit[:5])
'''
