# Comprehension

# my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5}
# my_dict = {value: key for key, value in my_dict.items()}
# print(my_dict)

"""
1) Создайте список имён. Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв. Используйте list comprehension.
"""

names = ['Алмаз', 'Урмат', 'Максат', 'Азиз', 'Талант', 'Айбек', 'Жайнак', 'Айпери', 'Лиана', 'Марико', 'Идрис']
vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
names_with_vowels = [name for name in names if name[0].lower() in vowels]
print(names_with_vowels)

"""
2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
"""

# result = {key: {key1: value1 + 2 for key1, value1 in value.items()} for key, value in students.items()}

students = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
for key, value in students.items():
    students[key] = {key: value + 2 for key, value in value.items()}
print(students)

"""
3) Создайте список чисел от 1 до 10. Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка, в противном случае поместите в список утроенные значения чисел.
"""

list_ = list(range(1, 10))
nums_ = set(n ** 2 if n % 2 == 0 else n * 3 for n in list_)
print(list_)
print(nums_)