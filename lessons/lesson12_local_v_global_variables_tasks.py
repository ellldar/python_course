# TASKS

# Self-Imposed Task 1

# def average(*args):
#     try:
#         assert len(args) != 0, 'List is empty'
#     except AssertionError as ae:
#         print("Error:", ae)
#     else:
#         return sum(args) / len(args)
#
# print(average(12, 1, 14, 5, 3, 3, 1, 15, 19, 10))
# print(average(13, 17, 11, 4, 6, 6, 11, 11))
# print(average())

# Task 1

# shirts = {0: 'красная', 1: 'синяя'}
# try:
#     month = int(input("Введите число месяца: "))
#     assert month >= 0 and month <= 12
#     key = month % 2
# except ValueError:
#     print("Ошибка! Введите целое число")
# except AssertionError:
#     print("Неверный месяц. Должно быть значение между 1 и 12")
# else:
#     print(f"В этом месяце Ирина будет носить футболку - {shirts[key]}")

# Task 2

# try:
#     data = input("Введите два целых числа через пробел: ").split(' ')
#     assert len(data) == 2
#     num1 = int(data[0])
#     num2 = int(data[1])
#     if num2 == 0:
#         raise ZeroDivisionError
# except ValueError:
#     print("Ошибка! Нужно вводить только целые числа")
# except AssertionError:
#     print("Ошибка! Нужно ввести 2 целых числа")
# except ZeroDivisionError:
#     print("Невозможно деление на 0")
# else:
#     if num1 % num2 == 0:
#         print(f"Да! {num1} делиться на {num2}")
#     else:
#         print(f"Нет! {num1} не делится на {num2}")
#     print(f"{num1} / {num2} = {num1 // num2}", f"с остатком {num1 % num2}" if num1 % num2 != 0 else "")

# Task 3

# def find_max(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
#
# print(find_max(5, 7, 9))
# print(find_max(15, 7, 9))
# print(find_max(5, 17, 9))
# print(find_max(5, 7, 29))

# Task 4

# from random import random
#
# def find_square(mylist):
#     return [item ** 2 for item in mylist]
#
# list_ = [round(random() * 10) for _ in range(round(random() * 10 + 10))]
# print("Ввод\t:", list_)
# print("Вывод\t:", find_square(list_))

# Task 5

# from random import random
#
# def factorial(num):
#     return num * factorial(num - 1) if num > 1 else 1
#
# def calculate(mylist):
#     return [factorial(item) for item in mylist]
#
# list_ = [round(random() * 10) for _ in range(round(random() * 10 + 5))]
# print("Ввод\t:", list_)
# print("Вывод\t:", calculate(list_))

# Task 6

# def age_control(mydict):
#     temp = {key: value for key, value in mydict.items() if value > 17}
#     return temp.keys()
#
# friends = {'Murat': 24, 'Erjan': 21, 'Chyngyz': 24, 'Altynai': 17, 'Asema': 16}
# print("В клуб поздно ночью пришли -", ", ".join(friends))
# print("Но в клуб смогут пройти только -", ", ".join(age_control(friends)))

# Task 7

# def make_capitalize(list_):
#     return [item.capitalize() for item in list_]
#
# names = ['jumagul', 'eldar', 'aiperi', 'liana', 'idris', 'mariko', 'aziz', 'chyngyz']
# names_with_capital_letter = make_capitalize(names)
# print(names_with_capital_letter)

# Task 8

# def analyze(word):
#     vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#     consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
#     # v_count - vowel count, c_count - consonants count, o_count - other symbols count
#     v_count, c_count, o_count = 0, 0, 0
#     for w in word.lower():
#         if w in vowels:
#             v_count += 1
#         elif w in consonants:
#             c_count += 1
#         else:
#             o_count += 1
#     print(f"Разбор символов для строки: '{word}'")
#     print("Гласные\t\t-", v_count)
#     print("Согласные\t-", c_count)
#     print("Другие\t\t-", o_count)
#
# text1 = "Привет всем! Меня зовут Тони Старк. Я Железный Человек!"
# analyze(text1)
# text2 = "Никогда! Никогда нельзя недооценивать важность хорошего своевременного сна!!!"
# analyze(text2)

# Task 9

# list_ = list()
#
# print("Пожалуйста, вводите целые числа по одному. Введите 'Q' чтоб завершить ввод чисел")
# while True:
#     try:
#         entry = input("Ввод: ").lower()
#         if entry == 'q':
#             break
#         num = int(entry)
#         assert num in range(0, 11)
#     except ValueError:
#         print("Ошибка ввода! Введите целое число или 'Q' для завершения")
#         print("Попробуйте еще раз")
#         continue
#     except AssertionError:
#         print("Ошибка ввода! Значение должно быть между 0 и 10 влючительно")
#         print("Попробуйте еще раз")
#         continue
#     else:
#         list_.append(num)
#
# print(list_)

# Task 10

from random import random

def less_than_7(list_):
    return [item for item in list_ if item < 7]
list_ = [round(random() * 10) for _ in range(round(random() * 10 + 10))]
print("Ввод\t:", list_)
print("Вывод\t:", less_than_7(list_))