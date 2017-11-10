# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction
import fractions


def nash_equilibrium(A):

    #Векторы оптимальных стратегий первого и второго игрок
    a1 = [ ]
    a2 = [ ]

    #Результат(цена) игры
    game_result = 0

    #Векторы правых частей для ЗЛП
    b1 = [ ]
    b2 = [ ]

    #Вектор целевых функций для ЗЛП
    c1 = [ ]
    c2 = [ ]

    #Размер матрицы игры
    n = A.shape[0]
    m = A.shape[1]

    #Проверка на отрицательные элементы с последующим
    #преобразованием к игре без отрицательных значений
    a_min = np.amin(A)
    if (a_min <= 0):
        A += abs(a_min) + 1

    #Решение ЗЛП для первого и второго игрока
    A_t = -np.transpose(A)
    b1 = -np.ones(m)
    c1 = np.ones(n)
    b2 = np.ones(n)
    c2 = -np.ones(m)

    res = linprog(c1, A_ub = A_t, b_ub = b1)
    a1 = res.get("x")

    res = linprog(c2, A_ub = A, b_ub = b2)
    a2 = res.get("x")

    #Нахождение результата(цены) игры с приведением к исходным данным
    game_result = 1 / np.sum(a1)
    a1 *= game_result
    a2 *= game_result

    if (a_min <= 0):
        game_result += a_min - 1

        # Преобразование к обыкновенным дробям
    a_str1 = []
    a_str2 = []
    for i in range(n):
        a_str1.append(str(fractions.Fraction.from_float(a1[i]).limit_denominator(10000)))
    for j in range(m):
        a_str2.append(str(fractions.Fraction.from_float(a2[j]).limit_denominator(10000)))
    ans_str = str(Fraction.from_float(game_result).limit_denominator(10000))
    return a_str1, a_str2, ans_str
