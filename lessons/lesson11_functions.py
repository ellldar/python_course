# Check yourself

# Ex 1

# stroka = "hello, this is a beautiful world!"
# middle = len(stroka) // 2 if len(stroka) % 2 == 0 else len(stroka) // 2 + 1
# list_ = list(stroka)[middle:] + list(stroka)[0:middle]
# print(list_)

# Ex 2

# text = ["hello", "world"]
# text[0], text[1] = text[1], text[0]
# print(text)

# Ex 3

# set1 = {"apple", "banana", "cherry", "pear"}
# set2 = {"mango", "strawberry", "cherry", "orange", "apple"}
# res = set1.intersection(set2)
# print(res)

# Ex 4

# tilek = {"Dodo", "ImperiaPizza", "FreshBox"}
# timur = {"OcakKebab", "FreshBox"}
# alex = {"FreshBox", "KFC"}
# elina = tilek | timur | alex
# res = tilek & timur & alex & elina
# print(res)

# Ex 5

# dict_ = {"apple": 65, "pear": 80, "orange": 120, "cherry": 235, "banana": 110}
# dict_ = {key: value for key, value in dict_.items() if value % 2 != 0}
# print(dict_)

# Ex 6

# dict_ = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# res = sum(value for value in dict_.values())
# print(res)

# Ex 7

# list_ = range(1, 10)
# dict_ = {value: value ** 2 for value in list_}
# print(dict_)

# Ex 8

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}, 'third': {'c': 3}, 'fourth': {'d': 4}}
# my_dict = {key: value2
#            for key, value in my_dict.items()
#            for key2, value2 in value.items()
#            if value2 == max(value.values())}
# print(my_dict)

# Ex 9

# dict_ = {"one": 1, "two": 2, "three": 3, "four": 4}
# try:
#     print(dict_["five"])
# except KeyError:
#     print("No item with key value of 'five'")
# except:
#     print("Unexpected error")

# Ex 10

# try:
#     amount = int(input("Сколько денег в бумажнике? "))
#     if amount < 0:
#         raise Exception("Сумма не может быть отрицательной")
# except ValueError:
#     print("Введите целое положительное число")

# CLASSWORK

from random import random

# Ex 1

# def generate_password(firstName, lastName):
#     password = firstName + lastName
#     for num in range(7):
#         temp = round(random() * 9)
#         password += str(temp)
#     return(password)
#
#
# def get_info():
#     firstName = input("Введите имя: ")
#     lastName = input("Введите фамилию: ")
#     return(generate_password(firstName, lastName))
#
# print(get_info())

# Ex 2

# def add(num1, num2):
#     return(num1, num2)
#
# def substract(num1, num2):
#     return(num1 - num2)
#
# def multiply(num1, num2):
#     return(num1 * num2)
#
# def divide(num1, num2):
#     try:
#         return(num1 / num2)
#     except ZeroDivisionError:
#         return None
#
# def get_data():
#     dispatch = {'+': add, '-': substract, '*': multiply, '/': divide}
#     print("Введите задачу для решения в следующем формате 'число1 (операция) число2'")
#     print("Поддерживаемые операции: +, -, *, /")
#     print("Например: 5 + 8")
#     try:
#         data = input("Ввод: ").split(' ')[0:3]
#         num1 = int(data[0])
#         oper = data[1]
#         num2 = int(data[2])
#         if oper in dispatch.keys():
#             result = dispatch[oper](num1, num2)
#             if result is None:
#                 raise Exception("Ошибка! Невозможно деление на ноль")
#         else:
#             raise Exception("Неверная операция. Поддерживаемые операции: +, -, *, /")
#     except ValueError:
#         print("Введите целые числа")
#     else:
#         return f"{num1} {oper} {num2} = {result}"
#     finally:
#         print("Проверьте правильность введенных данных")
#
# print(get_data())

# Ex 3

# def ice_cream(taste='', size='', *args):
#     print(f"Вы выбрали вкус {taste} и размер {size}")
#     if len(args) > 0:
#         print("Дополнительные добавки:", end=" ")
#         print(", ".join(args))
#
# ice_cream("Клубничный", "Большой", "Арахис", "Сироп")
