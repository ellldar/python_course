# Task 1

# list_ = [n for n in range(1, 100)]
# print(list_)

# Task 2

# list_ = [n for n in range(1, 50) if n % 2 != 0]
# print(list_)

# Task 3

# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# list_ = [n for n in int_list if n > 0 and n % 2 == 0]
# print(list_)

# Task 4

# list_ = [n ** 2 for n in range(1, 26)]
# print(list_)

# Task 5

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(n) for n in str_list]
# print(int_list)

# Task 6

# list_ = [n if n % 2 != 0 else n ** 2 for n in range(1, 11)]
# print(list_)

# Task 7

# list_ = [True if n % 2 == 0 else False for n in range(1, 10)]
# print(list_)

# Task 8

# names = ['Али', 'Максат', 'Азиз', 'Зоя', 'Айбек', 'Жайнак', 'Мия', 'Лиана', 'Марико', 'Идрис']
# names = ['shorter' if len(n) <= 4 else 'longer' for n in names]
# print(names)

# Task 9

# dict_ = {item: item ** 2 for item in range(1, 10)}
# print(dict_)

# Task 10

# while True:
#     num = int(input("Введите любое число от 1 до 10: "))
#     if num < 1 or num > 10:
#         print("Неправильный диапазон! Введите еще раз!")
#     else:
#         break
# dict_ = {i: i ** 2 for i in range(1, 500) if i % num == 0}
# print(dict_)

# Task 11

# list_ = {'a': 1, 'b': 5, 'c': 4, 'd': 3, 'e': 2, 'f': 6}
# list_ = {key: [n for n in range(1, value + 1)] for key, value in list_.items()}
# print(list_)

# Task 12

# import random
#
# words = ['hello', 'world', 'karakol', 'bishkek', 'talas', 'osh', 'batken', 'isfana']
# dict_ = {word: int(random.random() * 100) for word in words}
# print("Before\t:", dict_)
# dict_ = {key: 'even' if value % 2 == 0 else 'odd' for key, value in dict_.items()}
# print("After\t:", dict_)

# Task 13

# text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [int(word) for word in text.split(' ') if word.isdigit()]
# print(list_)

# Task 14

# students = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87},
#     'Pedro': {'history': 97, 'math': 85, 'literature': 93}
# }
#
# for key, value in students.items():
#     max_value = max({val for val in value.values()})
#     max_key = list({key1 for key1, value1 in value.items() if value1 == max_value})[0]
#     students[key] = max_key
# print(students)

# Task 15

my_dict = {'first': {'a': 1}, 'second': {'b': 2}, 'third': {'c': 3}}
for key, value in my_dict.items():
    my_dict[key] = max({val for val in value.values()})
print(my_dict)