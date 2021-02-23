
# Proper Way of defining a function

# def do_something(item: str) -> str:
#     return item.title()
#
# print(do_something("hello"))

# Playing with ZIP function

from random import random

# list1 = [round(random() * 10) for _ in range(20)]
# list2 = [round(random() * 10) for _ in range(20)]
# print("*" * 30, "BEFORE", "*" * 30)
# print(list1)
# print(list2)
# print("*" * 30, "ZIPPED", "*" * 30)
# zipped = list(zip(list1, list2))
# print(zipped)
# print("*" * 30, "AFTER", "*" * 30)
# unzip1, unzip2 = map(list, zip(*zipped))
# print(unzip1)
# print(unzip2)

# Playing with Reducer

# from functools import reduce

# Finding Max with reducer

# list3 = [round(random() * 20) for _ in range(round(random() * 10) + 10)]
# find_max = reduce(lambda a, b: a if a > b else b, list3)
# print(list3)
# print("Max:", find_max)

# Finding Sum with reducer

# find_sum = reduce(lambda a, b: a + b, list3)
# print("Sum:", find_sum)

# Finding Product with reducer
# find_mult = reduce(lambda a, b: a * b, list3)
# print("Product:", find_mult)

# TASKS

# Task 1

# from math import sqrt
#
# list_ = [5, 15, 6.0, 'hello', {'abc', 'efgh'}, (1, 2, 3), ['qr', 'code', 'yes']]
# for item in list_:
#     if isinstance(item, int):
#         print(f"Корень {item} = {round(sqrt(item), 4)}")

# Task 2

# from random import random
#
# def send_letter(item):
#     print(f"Уважаемый/ая {item[0]}! Вы набрали {item[1]} баллов, в связи с чем объявляем о вашем отчислении")
#
# names = ['Urmat', 'Joldosh', 'Aigerim', 'Samat', 'Umut', 'Almaz', 'Kanykei', 'Lena', 'Idris']
# grades = [round(random() * 60 + 40) for _ in range(len(names))]
# course = {item[0]: item[1] for item in zip(names, grades)}
# print(course)
# failed = {key: value for key, value in course.items() if value < 60}
# for item in failed.items():
#     send_letter(item)

# Task 3

from functools import reduce

list_ = ['a', 'b', 'c', 'd', 'e', 'i', 'p', 'a', 'b', 'j']
text_ = reduce(lambda a, b: a + b, list_)
print(text_)