# Напишите програму, которая на вход принимает
# цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# print('Введите номер дня недели: ')
# a = int(input())
# if a > 0 and a < 6:
#     print ('Это будний день')
# elif a >= 6 and a < 8:
#     print('Это выходной день')
# else:
#     print('Это не день недели')

# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not (w and z or not y or (not x == (not w))):
#                     print(x, y, z, w)


# Напишите программу, которая принимает на вход координаты точки
# (X и Y), при чём X и Y не равны 0, и выдаёт номер четверти плоскости
# в которой находится эта точка (или на какой оси).

# X = int(input('Введите координату X:'))
# Y = int(input('Введите координату Y:'))
# if X > 0 and Y > 0 :
#     print('I четверть')
# elif X > 0 and Y < 0 :
#     print('IV четверть')
# elif X < 0 and Y < 0 :
#     print('III четверть')
# elif X < 0 and Y > 0 :
#     print('II четверть')
# else:
#     print('Не соответствует заданным параметрам')


# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Введите номер четверти')
# a = int(input())
# if a == 1 :
#     print('X от 0 до + ∞ ; Y от 0 до + ∞')
# elif a == 2 :
#     print('X от 0 до - ∞ ; Y от 0 до + ∞')
# elif a == 3 :
#     print('X от 0 до - ∞ ; Y от 0 до - ∞')
# elif a == 4 :
#     print('X от 0 до + ∞ ; Y от 0 до + ∞')
# else:
#     print('Не соответствует заданным параметрам')

# Напишите программу, которая принимает на вход координаты
#    двух точек и находит расстояние между ними в 2D пространстве.
#    https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

# x_1 = int(input())
# y_1 = int(input())
# x_2 = int(input())
# y_2 = int(input())

# print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")