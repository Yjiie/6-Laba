"""
Есть требования:
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

На плоскости задано К точек. Сформировать все возможные варианты выбора множества точек из них на проверку того, что они являются вершинами квадрата.
"""
from itertools import combinations
import timeit

nmax = 20  # макс. кол.точек


# является ли квадратом
def square(a, b, c, d):
    s1 = (a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2
    s2 = (a['x'] - c['x']) ** 2 + (a['y'] - c['y']) ** 2
    s3 = (a['x'] - d['x']) ** 2 + (a['y'] - d['y']) ** 2
    s4 = (b['x'] - c['x']) ** 2 + (b['y'] - c['y']) ** 2
    s5 = (b['x'] - d['x']) ** 2 + (b['y'] - d['y']) ** 2
    s6 = (c['x'] - d['x']) ** 2 + (c['y'] - d['y']) ** 2
    return ((s1 == s3) and (s1 == s4) and (s1 == s6) and (s2 == s5) and (s2 == 2 * s1)) \
        or ((s1 == s2) and (s1 == s5) and (s1 == s6) and (s3 == s4) and (s3 == 2 * s1)) \
        or ((s2 == s3) and (s2 == s4) and (s2 == s5) and (s1 == s6) and (s1 == 2 * s2))


n = 0
while n not in range(4, nmax + 1):
     n = int(input(f"Количество точек от 4 до {nmax} n = "))

t = [{'x': 0, 'y': 0} for _ in range(n)]  # массив точек

print("Введите координаты", n, "точек, целые числа:")
for i in range(n):
    print("Точка", i + 1)
    t[i]['x'] = int(input("x="))
    t[i]['y'] = int(input("y="))


def find_square_alg(t):
    s_list = []
    n_list = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if square(t[i], t[j], t[k], t[l]):
                        s_list.append([[t[i]['x'], t[i]['y']],
                                       [t[j]['x'], t[j]['y']],
                                       [t[k]['x'], t[k]['y']],
                                       [t[l]['x'], t[l]['y']]])
                    else:
                        n_list.append([[t[i]['x'], t[i]['y']],
                                       [t[j]['x'], t[j]['y']],
                                       [t[k]['x'], t[k]['y']],
                                       [t[l]['x'], t[l]['y']]])
    return s_list, n_list


def find_square_py(t):
    s_list = []
    n_list = []
    for combination in list(combinations(t, 4)):
        if square(combination[0], combination[1], combination[2], combination[3]):
            s_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
        else:
            n_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
    return s_list, n_list


start_time = timeit.timeit()
square_list, no_square_list = find_square_alg(t)
algorithmic_time = timeit.timeit() - start_time
print('Точки образующие квадрат(алгоритмический подход): ')
print(*square_list, sep='\n')
print('Точки не образующие квадрат(алгоритмический подход): ')
print(*no_square_list, sep='\n')
print('Время работы алгоритмического алгоритма: ', algorithmic_time)

start_time = timeit.timeit()
square_list, no_square_list = find_square_py(t)
pythonic_time = timeit.timeit() - start_time
print('Точки образующие квадрат(python функция): ')
print(*square_list, sep='\n')
print('Точки не образующие квадрат(python функция): ')
print(*no_square_list, sep='\n')
print('Время работа алгоритма с python функцией: ', pythonic_time)


def find_square_opt(t):
    print('lox')
    s_list = []
    n_list = []
    filtered_t = list(filter(lambda p: p['x'] % 2 == 0 and p['y'] % 2 == 0, t))
    for combination in list(combinations(filtered_t, 4)):
        if square(combination[0], combination[1], combination[2], combination[3]):
            s_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
        else:
            n_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
    return s_list, n_list


start_time = timeit.timeit()
square_list, no_square_list = find_square_opt(t)
pythonic_time_opt = timeit.timeit() - start_time
print('Точки (с четными координатами) образующие квадрат: ')
print(*square_list, sep='\n')
print('Точки (с четными координатами) не образующие квадрат: ')
print(*no_square_list, sep='\n')
print('Время работы оптимального алгоритма: ', pythonic_time_opt)
