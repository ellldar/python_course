# arr = list(range(0, 10))
# res = [num * 2 for num in arr if num <= 5]
# arr2 = list(range(15, 20))
# res.extend(arr2)
# print(arr)
# print(res)
# if any(num > 15 for num in res):
#     print("Success!")
#
# if all(num >= 0 for num in res):
#     print("All is true!")

# Task 1

# friends = ['Данчик', 'Макс', 'Чина', 'Алтын', 'Тиля']
# for item in friends:
#     print(item)

# Task 2

# bikes = ['Triumph', 'BMW', 'Honda', 'Kawasaki', 'Harley Davidson']
# info = ['крутой круизер', 'самая быстрая', 'самая резвая', 'хорошо управляемая', 'для недалеких поездок']

# for item in zip(bikes, info):
#     print(f'{item[0]} - {item[1]}')

# Task 3

# myList = list("What a wonderful world!")
# length = len(myList)
# middle = length // 2
# if length % 2 != 0:
#     middle += 1
# part1 = myList[0:middle]
# part2 = myList[middle:]

# newList = [letter for letter in part2]
# newList += [letter for letter in part1]
# print(newList)

# Task 4

# myList = ["Hello", "World"]
# myList[0], myList[-1] = myList[-1], myList[0]
# print(myList)

# OR

# myList = ["Hello", "World"]
# myList.reverse()
# print(myList)

# Task 5

# suitcase = []
# suitcase.append('Плавки')
# suitcase.append('Полотенце')
# suitcase.append('Толстовка')
# suitcase.append('Шлепанцы')
# suitcase.append('Солнцезащитные очки')
# print('Набрали вещи')
# print(suitcase)
# suitcase.pop()
# print('Убрал последнюю вещь')
# print(suitcase)
# suitcase.insert(0, 'Музыкальная колонка')
# print('В начало списка добавил колонку')
# print(suitcase)

# Task 6

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [num for num in a if num < 5]
# print(res)

# Task 7

# data = map(int, input("Введите числа: ").split(','))
# myList = list(data)
# myTuple = tuple(myList)
# print(myList)
# print(myTuple)

# Task 8

# myList = list(range(0, 10))
# newList = [str(item) for item in myList]
# print(newList)

# Task 9

# myList = list(range(0, 15))
# print(myList)
# newList = []
# for item in myList:
#     newList.append("Четное" if item % 2 == 0 else "Нечетное")
# print(newList)

# Task 10

# from random import random
#
# nums = []
# for i in range(0, 20):
#     nums.append(int(random() * 100))
# print(nums)

# Task 11

# myList = [i for i in range(0, 100, 2)]
# print(myList)

# Task 12

# from random import random
# list1 = [int(random() * 100) for _ in range(0, 20)]
# list2 = [int(random() * 100) for _ in range(0, 20)]
# print(list1)
# print(list2)
# newList = list1 + list2
# print(newList)
# print(sum(newList))

# Task 13

# nums = []
# while True:
#     num = input("Введите число: ")
#     if num.isalpha():
#         break
#     nums.append(int(num))
#
# nums.sort()
# print(nums)

# Task 14

# nums = list(map(int, input("Введите три числа через пробел: ").split(' ')))
# multiple = False
# for i in nums:
#     c = nums.count(i)
#     if c > 1:
#         multiple = True
#         break
#
# print("YES" if multiple == True else "ERROR")

# Task 15

# myList = [num for num in range(54, 9184) if num % 5 == 0]
# print(myList)

# CLASSWORK
# Task 1

# nums = list(map(int, input("Введите числа через запятую: ").split(',')[0:7]))
# print(nums[0], nums[-1])
# nums.pop()
# nums.append("Makers")
# print(nums)

# Task 2
# from random import random
#
# nums = [int(random() * 100) for _ in range(0, 10)]
# nums.sort()
# print(nums)

# Task 3

# words = input("Введите слова через пробел: ").split(' ')
# length = [len(item) for item in words]
# print(words)
# print(length)

# How to join separated characters into a string
from string import ascii_lowercase as abc
arr = list(range(0, 20))
# res = "".join([str(i) for i in arr])
res = "".join(abc[abc.index(i) - 1] for i in "qfsbtqfsbbebtusb")
print(res)
