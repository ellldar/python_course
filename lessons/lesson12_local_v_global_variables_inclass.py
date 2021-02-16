# In-Class Tasks

# Ex 1

# matreshka = 10
# def func1():
#     global matreshka
#     matreshka1 = 20
#     matreshka += matreshka1
#     def func2():
#         global matreshka
#         matreshka2 = 30
#         matreshka += matreshka2
#     func2()
#     return matreshka
#
# print(func1())

# Ex 2

from random import random

list_ = []

def add():
    global list_
    name = input("Введите имя: ")
    list_.append(name)

def remove():
    global list_
    if len(list_) > 0:
        print(list_)
    try:
        index = int(input("Введите индекс для удаления: "))
        removed = list_.pop(index)
        print(f"Удалено значение '{removed}'")
    except ValueError:
        print("Неправильный формат данных. Введите целое число")
    except IndexError:
        print(f"Отсутствует значение по индексу - {index}")

for i in range(10):
    which = round(random())
    print(f"{i + 1}) ", end=" ")
    if which == 1 or len(list_) == 0:
        add()
    else:
        remove()

print(list_)
