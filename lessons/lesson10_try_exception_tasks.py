# TASKS

# Task 1

# try:
#   print("Запустить какой-нибудь код")
#   if <condition>:
#     raise Exception("Можно поднимать свои исключения")
# except <Название Исключения>:
#   print("Поймали конкретное исключение")
# except:
#   print("Поймали общее исключение")
# else:
#   print("Никаких исключений не возникло")
# finally:
#   print("Код, который запустится в любом случае")

# Task 2

# b = 10
# c = 11
#
# try:
#     print(a)
# except NameError:
#     print("Variable is not defined")

# Task 3

# try:
#     values = [int(i) for i in input("Введите два числа через пробел: ").split(' ')]
#     res = values[0] / values[1]
# except ZeroDivisionError:
#     print("Division by zero occured")
# else:
#     print(f"{values[0]} / {values[1]} = {round(res, 2)}")

# Task 4

# try:
#     values = [int(i) for i in input("Введите два числа через пробел: ").split(' ')]
#     res = sum(values)
# except ValueError:
#     print("Error: Please, input integer values")
# else:
#     print(f"{values[0]} + {values[1]} = {round(res, 2)}")

# Task 5

# mydict = {'one': 1, 'two': 2, 'three': 3}
# try:
#     item = mydict['four']
# except KeyError:
#     print("There's no element with a key value of 'four'")

# Task 6

# mylist = [1, 2, 3, 4, 5]
# try:
#     item = mylist[6]
# except IndexError:
#     print("There's no element at index '6'")

# Task 7

# try:
#     num1 = input("Введите первое число: ")
#     num2 = input("Введите второе число: ")
#     res = int(num1) / int(num2)
# except ZeroDivisionError:
#     print("Ошибка: невозможно выполнить деление на 0")
# except ValueError:
#     print("Ошибка: введите целое число")
# except:
#     print("Произошла неучтенная ошибка")
# else:
#     print(res)

# Task 8

# try:
#     amount = int(input("Сколько денег у вас в бумажнике? "))
#     if amount < 0:
#         raise Exception("Сумма не может быть отрицательной!")
# except ValueError:
#     print("Ошибка: введите целое число")

# Task 10

try:
    age = int(input("Введите свой возраст: "))
    if age < 18:
        raise Exception("Доступ запрещен!")
except ValueError:
    print("Введен некорректный возраст")
else:
    print("Спасибо!")
finally:
    print("До свидания")