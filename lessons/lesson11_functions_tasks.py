# Homework - Tasks

# Task 1

# def add(num1, num2):
#     return num1 + num2
#
# print(add(5, 10))

# Task 2
#
# def print_len(str1):
#     print(len(str1))
#
# txt = 'What a beautiful day!'
# print_len(txt)

# Task 3

# def func(param1, param2):
#     print('Тип первого параметра', type(param1))
#     print('Тип второго параметра', type(param2))
#
# func({'key': 'value'}, [1,2,3,4])

# Task 4

# def divide(num1, num2):
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print("Ошибка! Невозможно деление на ноль")
#         result = None
#     return result
#
# print(divide(5, 10))
# print(divide(0, 20))
# print(divide(20, 0))

# Task 5

# def print_dict(data):
#     if isinstance(data, dict):
#         for key in data.keys():
#             print(key)
#     else:
#         print(f"Введенные данные {data} не являются словарем")
#
# dict_ = {'one': 1, 'two': 2}
# list_ = [1,2,3,4]
# print_dict(dict_)
# print_dict(list_)

# Task 6

# def check_number(num):
#     if num % 2 == 0:
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")
#
# check_number(10)
# check_number(15)
# check_number(11)
# check_number(0)

# Task 7

# def check_poly(data):
#     res1 = data.lower().replace(" ", "")
#     res2 = res1[::-1]
#     if res1 == res2:
#         print(f"Да! '{data}' является полиндромом")
#     else:
#         print(f"Нет! '{data}' не является полиндромом")
#
# check_poly("101")
# check_poly("кок")
# check_poly("топот")
# check_poly("комок")
# check_poly("Солнце")
# check_poly("Я иду с мечем судия")
# check_poly("Лида Ланцет отец наладил")

# Task 8

# def compare(num1, num2):
#     return num1 if num1 > num2 else num2
#
# def get_info():
#     data = input("Введите два числа через пробел: ").split(" ")[0:2]
#     try:
#         num1 = int(data[0])
#         num2 = int(data[1])
#     except ValueError:
#         print("Ошибка! Введите целые числа")
#     else:
#         print(compare(num1, num2))
#
# get_info()

# Task 9

# def calculate(list_):
#     res = 1
#     for item in list_:
#         res *= item
#     return res
#
# def get_info():
#     data = input("Введите числа через пробел: ").split(" ")
#     try:
#         nums = list(map(int, data))
#         result = calculate(nums)
#         print(result)
#     except ValueError:
#         print("Ошибка! Введите целые числа")
#
# get_info()

# Task 10

# def calculate(num):
#     temp = num
#     res = 0
#     while temp > 0:
#         res += temp % 10
#         temp //= 10
#     return res
#
# def get_info():
#     try:
#         num = int(input("Ввод: "))
#         print(calculate(num))
#     except ValueError:
#         print("Ошибка! Введите целое число")
#
# get_info()