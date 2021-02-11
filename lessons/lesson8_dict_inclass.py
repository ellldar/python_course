# mydict = {
#     285: 'Aleksey Medvedev',
#     287: 'Yunus Makeev',
#     289: 'Eldar Supataev',
#     290: 'Nurdan Tursunaliev'
# }
#
# mykeys = list(mydict.keys())
# for key in mykeys:
#     if key == 290:
#         mydict.pop(key)
#
# print(mydict)

# emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
# email_at_dotcom = dict([name, '.com' in email] for name, email in emails.items())
# print(emails)
# print(email_at_dotcom)
#
# newdict = dict.fromkeys(('BMW', 'Mercedes', 'Honda'), 5)
# newdict.setdefault('Toyota', 6)
# # newdict.update({'Toyota': 6})
# print(newdict)
# newdict.popitem()
# print(newdict)

# ----------------- CLASSROOM TASKS -----------------

# print("---------------------- CLASSROOM TASKS -------------------------")

# ----------------- PRIME NUMBERS -------------------

# for n in range(2, 20):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # цикл потерпел неудачу, не найдя множитель
#         print(n, 'is a prime number')

# # --------------- In-class Exercise -----------------
#
# my_dict = {
#     'Worker': {'Manager': 1, 'Accountant': 3},
#     'Figures': {'Circle': 3, 'Triangle': 3, 'Rectangle': 4, 'Octagon': 8}
# }
#
# for key, value in list(my_dict.items()):
#     print(key, ":", value)
#     for key1, value1 in list(value.items()):
#         print("Values: ", key1)
#         if key1 in ["Circle", "Octagon"]:
#             print("Value found: ", value1)
#             my_dict[key].pop(key1)
#
# print(my_dict)

# Task 1

# university = {'SFW': 30, 'ICP': 100, 'BA': 78, 'ECO': 83, 'PSY': 17, 'MED': 45}
# print(university)
# university['SFW'] += 5
# university.setdefault("LING", 0)
# university.pop("MED")
# student_count = sum(university.values())
# print(university)
# print("Количество студентов:", student_count)

# Task 2

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# dict2 = {}
# print("Dictionary 1:", dict1)
# for key, value in dict1.items():
#     dict2.setdefault(value, key)
# print("Dictionary 2:", dict2)

# Task 3

# guest_num = int(input("Сколько гостей вы хотите пригласить? "))
# guests = {}
# i = 1
# while i < guest_num + 1:
#     name = input("Введите имя гостя: ")
#     if len(name) == 0:
#         print("Неправильный ввод данных!")
#         continue
#     guests.update({i: name})
#     i += 1
# else:
#     for key in guests:
#         print(f"№:{key}\t| {guests[key]}")

# Task 4

# shop_list = { "Хлеб": 2, "Молоко": 3, "Колбаса": 1, "Сметана": 1, "Картошка": 3 }
# print("Вы пришли в магазин. Вам нужно купить следующие продукты:")
# print([key for key in shop_list.keys()])
# while True:
#     item = input("Какой продукт купили? ").capitalize()
#     if item in shop_list.keys():
#         print("Отлично! Продукт куплен!")
#         shop_list.pop(item)
#     else:
#         print("Данного продукта нет в списке. Выберете другой!")
#     if len(list(shop_list)) == 0:
#         break
#     else:
#         print("Осталось купить", shop_list)
# print("Все продукты куплены!")

shop_list = { "Хлеб": 2, "Молоко": 3, "Колбаса": 1, "Сметана": 1, "Картошка": 3 }
for key, value in shop_list.items():
    shop_list[key] = value * 5
print(shop_list)