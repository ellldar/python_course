# Homework
# Ex 1

# list_ = [1, 2, 3, 4]
# total = sum(list_)
# print(total)

# Ex 2

# from random import random
#
# list_ = [round(random() * 10) for _ in range(round(random() * 20))]
# new_list = list(filter(lambda a: a > 3, list_))
# print("Before\t:", list_)
# print("After\t:", new_list)

# Ex 3

# from random import random
#
# list_ = [-10 + round(random() * 20) for _ in range(round(random() * 20))]
# neg_nums = list(filter(lambda a: a < 0, list_))
# has_negative = any([a < 0 for a in list_])
# print("Before\t:", list_)
# print("After\t:", neg_nums)
# print("The list", "contains" if has_negative else "doesn't contain", "negative numbers!")

# Ex 4

# from random import random
#
# list_ = [round(random() * 10) for _ in range(round(random() * 15))]
# result_ = list(map(lambda i: i ** 2, list_))
# print("Before\t:", list_)
# print("After\t:", result_)

# Ex 5

# from random import random
#
# list_ = [round(random() * 10) for _ in range(round(random() * 20))]
# result_ = list(filter(lambda a: a % 2 == 0, list_))
# print("Before\t:", list_)
# print("After\t:", result_)

# Ex 6

# list_ = ["hello", "world", "kyrgyzstan", "uzbekistan", "mouse", "keyboard", "semipalatinsk"]
# result_ = list(filter(lambda word: len(word) > 7, list_))
# print("Before\t:", list_)
# print("After\t:", result_)

# Ex 7

# from functools import reduce
#
# list_ = [5, 6, 7, 8]
# result_ = reduce(lambda a, b: a * b, list_)
# print("List\t:", list_)
# print("Result\t:", result_)

# Ex 8

# from random import random
#
# list_ = [round(random() * 20) for _ in range(round(random() * 30))]
# even = sum(1 for item in list_ if item % 2 == 0)
# odd = len(list_) - even
# print(list_)
# print(f"В списке {even} четных и {odd} нечетных чисел")

# Ex 9

# def check_value(item):
#     if item < 0:
#         return False
#     elif item > 0:
#         return True
#     else:
#         return 0
#
# list_ = [-1, 2, 3, 0, 5, -3, 7]
# list_ = list(map(check_value, list_))
# print(list_)

# Ex 10

from functools import reduce

names = ['Urmat', 'Joldosh', 'Aigerim', 'Samat', 'Umut', 'Almaz', 'Kanykei', 'Lampochkam', 'Lena', 'Idris']
result = reduce(lambda a, b: a if len(a) > len(b) else b, names)
print(names)
print(result)