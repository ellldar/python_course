# TUPLES & SETS
# CLASSWORK

# Task 1
#
# okroshka = {'квас', 'колбаса', 'огурцы', 'яйца', 'лук зеленый', 'укроп', 'петрушка', 'сметана', 'соль', 'сахар', 'горчица'}
# olivie = {'картофель', 'морковь', 'огурцы', 'горошек', 'колбаса', 'яйца', 'майонез', 'сметана', 'соль', 'черный перец'}
#
# common = okroshka & olivie
# print("Общие ингредиенты окрошки и оливье:", ", ".join(str(i) for i in common))
# print("Всего {} ингредиентов".format(len(common)))
#
# okroshka_unique = okroshka.difference(olivie)
# print("Уникальные ингредиенты окрошки: ", ", ".join(str(o) for o in okroshka_unique))
# olivie_unique = olivie.difference(okroshka)
# print("Уникальные ингредиенты оливье: ", ", ".join(str(o) for o in olivie_unique))

# Task 2

# users = {("Alice", "Python", 3),
#          ("Max", "Python", 2),
#          ("Max", "JavaScript", 2),
#          ("John", "Python", 5),
#          ("Ella", "JavaScript", 4),
#          ("Yunus", "Python", 3),
#          ("Yunus", "JavaScript", 3)}
#
# # Находит количество изучающих Python и JavaScript по-отдельности
# count_py = sum(user.count("Python") for user in users)
# count_js = sum(user.count("JavaScript") for user in users)
# print("Количество изучающих Python -", count_py)
# print("Количество изучающих JavaScript -", count_js)
#
# # Найти пользователей изучающих оба языка
# users_py = set(user[0] for user in users if user[1] == 'Python')
# users_js = set(user[0] for user in users if user[1] == 'JavaScript')
# print("Пользователи изучающие оба языка -", ", ".join(users_py & users_js))

# Task 3

# repeat = True
# while repeat:
#     currency = input("Введите валюту (сом или доллар): ").lower()
#     if currency == 'сом':
#         amount = int(input("Введите сумму, которую вы хотите перевести в доллары: "))
#         res = amount / 84
#     elif currency == 'доллар':
#         amount = int(input("Введите сумму, которую вы хотите перевести в сомы: "))
#         res = amount * 84
#     else:
#         print("Неправильный ввод вида валюты. Попробуйте еще раз.")
#         continue
#     print("Вывод:", '{0:.2f}'.format(res), "USD" if currency == 'сом' else "KGS")
#     again = input("Хотите продолжить? (Да/Нет): ").lower()
#     repeat = True if again == 'да' else False

# HOMEWORK

# Task 1

# set_ = set("Kyrgyzstan")
# print(set_)

# Task 2

# set_ = set(range(0, 20))
# print(len(set_))

# Task 3

# set_ = {"Kyrgyzstan"}
# set_.add("Hello World")
# print(set_)

# Task 4

# set1 = {1, 2, 5, 9, 7}
# set2 = {2, 4, 6, 5, 8, 9}
# set1.update(set2)
# print(set1)

# Task 5

# set1.discard(9)
# print(set1)

# Task 6

# set1.remove(9)
# print(set1)

# Task 7

# set1.clear()
# print(set1)

# Task 8

# set1 = {1, 2, 5, 9, 7, 11}
# set2 = {2, 4, 6, 5, 8, 9, 13, 17}
# print(set1.intersection(set2))
# print(set1 & set2)

# Task 9

# set1 = {1, 2, 5, 9, 7, 11}
# set2 = {2, 4, 6, 5, 8, 9, 13, 17}
# print(set1.difference(set2))
# print(set1 - set2)

# Task 10

# set1 = {1, 2, 5, 9, 7, 11}
# set2 = {2, 4, 6, 5, 8, 9, 13, 17}
# print(set1.union(set2))
# print(set1 | set2)

# Task 11

# set1 = {2, 6, 9, 17}
# set2 = {2, 4, 6, 5, 8, 9, 13, 17}
# if set1.issubset(set2):
#     print("ПОДМНОЖЕСТВО!")

# Task 12

# set1 = {2, 4, 6, 5, 8, 9, 13, 17}
# set2 = {2, 6, 9, 17}
# if set1.issuperset(set2):
#     print("НАДМНОЖЕСТВО!")

# Task 13

# rob = {5, 7, 11, 10, 28}
# kyle = {29, 2, 6, 12, 3}
# mary = {1, 5, 14, 8, 22}
#
# kyle_guess = not rob.isdisjoint(kyle)
# mary_guess = not rob.isdisjoint(mary)
# if kyle_guess:
#     print("Кайл угадал хотя бы одно число!")
# if mary_guess:
#     print("Мэри угадала хотя бы одно число!")
# if not kyle_guess and not mary_guess:
#     print("Никто не угадал ни одного числа!")

# Task 14

# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox', 'Begemot'}
# timur = {'OcakKebab', 'FreshBox', 'Begemot'}
# alex = {'FreshBox', 'KFC', 'Begemot'}
# elina = tilek | timur | alex
# result = tilek & timur & alex & elina
# print("Самый оптимальный вариант для всех это -", ", ".join(result))

# Task 15

# pizza = {"Сыр чеддар", "Грибы", "Соус", "Шпинат"}
# pizza.add("Помидоры")
# pizza.discard("Колбаса")
# pizza.discard("Шпинат")
# pizza.add("Базилик")
# pizza.discard("Сыр чеддар")
# pizza.add("Сыр мацарелла")
# print(pizza)
