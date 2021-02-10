import random

# Task 1

# password = input("Введите пароль: ")
# size = len(password)
# if (size < 8):
#     print("Ваш пароль должен содержать не менее 8 символов")
# if (not password.isalpha()):
#     print("Ваш пароль должен содержать только буквы")
# else:
#     print("Ваш пароль сохранен!")

# Task 2
#
# grades = input("Введите свои баллы по математике, английскому языку и литературе через запятую: ")
# average = sum(map(int, grades.split(','))) / 3
# if average > 69:
#     print("Вы допущены к экзаменам. Ваш средний балл составляет %.2f" % average)
# else:
#     print("Вы не допущены к экзаменам. Ваш средний балл составляет %.2f" % average)

# Task 3

# index = int(random.random() * 3)
# list = ['Камень', 'Ножницы', 'Бумага']
# selection = list[index]
# userSelection = input('Ваш выбор (Камень, Ножницы, Бумага): ')
# print("Выбор компьютера: ", selection)
# print("Вывод: ", "Вы выиграли!" if selection == userSelection else "Вы проиграли!")

# Homework

# Task 1

# num = int(input("Введите число: "))
# print("True" if num > 5 else "False")

# Task 2

# text = input("Введите что-нибудь: ")
# print("True" if len(text) >= 5 else "False")

# Task 3
#
# grade = int(input("Введите оценку: "))
# if (grade > 100 or grade < 0):
#     print("Ошибка ввода. Оценка должна быть между значениями 0 и 100")
# elif grade >= 90:
#     print("Отлично, ваша оценка 5")
# elif grade >= 80:
#     print("Здорово, ваша оценка 4")
# elif grade >= 70:
#     print("Хорошо, ваша оценка 3")
# elif grade >= 60:
#     print("Вам стоит подучить материал")
# else:
#     print("Вы не сдали экзамен")

# Extra Exercise
#
# data = input("Введите два числа через пробел: ").split(' ')
# num1 = int(data[0])
# num2 = int(data[1])
# print("Both equal" if num1 == num2 else "num1 is bigger than num2" if num1 > num2 else "num1 is smaller than num2")

# Task 4
#
# num = int(input("Введите любое целое число: "))
# print("Negative" if num < 0 else "Zero" if num == 0 else "Positive")

# Task 5

# data = input("Введите два числа через пробел: ").split(' ')[0:2]
# num1 = int(data[0])
# num2 = int(data[1])
# print("Наименьшее число: ", num1 if num1 < num2 else num2)

# Task 6
#
# data = input("Введите три числа через пробел: ").split(' ')
# num1 = int(data[0])
# num2 = int(data[1])
# num3 = int(data[2])
# if num1 < num2 and num1 < num3:
#     print("Наименьшее число: ", num1)
# elif num2 < num1 and num2 < num3:
#     print("Наименьшее число: ", num2)
# else:
#     print("Наименьшее число: ", num3)

# Task 7

# data = input("Введите три числа через пробел: ").split(' ')
# num1 = int(data[0])
# num2 = int(data[1])
# num3 = int(data[2])
# if num1 == num2 and num1 == num3:
#     print(3)
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print(2)
# else:
#     print(0)

# Task 8

# data = input("Введите два числа через пробел: ").split(' ')
# num1 = int(data[0])
# num2 = int(data[1])
# ans = True if num1 % num2 == 0 else False
# print(f'{num1}', 'делится' if ans else 'не делится', f'на {num2}')
# print("Частное:", num1 // num2)
# if not ans:
#     print("Остаток:", num1 % num2)

# Task 9
#
# year = int(input("Введите номер года: "))
# if year % 400 == 0:
#     print("YES")
# elif year % 4 == 0 and year % 100 != 0:
#     print("YES")
# else:
#     print("NO")

# Task 10

# num = int(input("Введите число: "))
# select = int(input("Выбрать (1 - байт, 2 - килобайт): "))
# if select == 1:
#     print(bytes(num))
# elif select == 2:
#     print(bytes(num // 1024))
# else:
#     print("Неправильный выбор")

# Task 11
#
# num = int(input("Введите число являющееся кодом символа: "))
# char = chr(num)
# print(f"Символ '{char}'", "не является" if not char.isalpha() else "является", "буквой")

# Task 12

# while True:
#     data = input("Введите параметры n, m, k через пробел: ").split(' ')
#     if len(data) < 3:
#         break
#     n = int(data[0])
#     m = int(data[1])
#     k = int(data[2])
#     if k >= n * m:
#         print("NO!")
#     elif k % n == 0 or k % m == 0:
#         print("YES!")
#     else:
#         print("NO!")

# Task 13

# print("Узнайте возраст своей собаки в собачьих годах!")
# age = int(input("Введите возраст в человеческих годах: "))
# if (age > 2):
#     print("Ответ: ", 21 + (age - 2) * 4)
# elif age < 0:
#     print("Ошибка ввода! Возраст должен быть положительным числом!")
# else:
#     print("Ответ: ", int(10.5 * age))

# Task 14

# print("Пожалуйста, вводите координаты (x, y) через пробел")
# x1, y1 = map(int, input("Координаты первой клетки (x y): ").split(' ')[0:2])
# x2, y2 = map(int, input("Координаты второй клетки (x y): ").split(' ')[0:2])
# if y2 != y1:
#     slope = abs((x2 - x1) / (y2 - y1))
# if x1 == x2 and y1 == y2:
#     print("Слон никуда не сдвинется!")
# elif slope == 1:
#     print("ХОД СЛОНОМ ВОЗМОЖЕН!")
# else:
#     print("ХОД СЛОНОМ НЕВОЗМОЖЕН!")

# Task 15

x1, y1, x2, y2 = map(int, input("Введите две координаты (x1 y1 x2 y2): ").split(' ')[0:4])
err = sum(map(lambda n: 0 if (n > 0 and n <= 8) else 1, [x1, y1, x2, y2]))
if err > 0:
    print("Неправильные координаты. Значения должны быть между 1 и 8")
elif x1 == x2 and y1 == y2:
    print("Ладья никуда не сдвинется")
elif x1 == x2 or y1 == y2:
    print("Ход ладьей возможен!")
else:
    print("Ход ладьей невозможен!")
