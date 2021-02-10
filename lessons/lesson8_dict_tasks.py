# HOMEWORK

# Task 1

# mydict = {1: "hello", 2: "world", 3: "kyrgyzstan", 4: "amazing"}
# print(mydict.get(3))

# Task 2

# mydict = {1: "hello", 2: "world", 3: "kyrgyzstan", 4: "amazing"}
# removed = mydict.pop(4)
# print(removed)

#Task 3

# mydict = {1: "hello", 2: "world", 3: "kyrgyzstan", 4: "amazing"}
# # mydict.update({3922: "karakol"})
# # mydict.setdefault(3922, "karakol")
# mydict[3922] = "karakol"
# print(mydict)

# Task 4

# mydict = {1: "hello", 2: "world", 3: "kyrgyzstan", 4: "amazing"}
# mydict.clear()
# print(mydict)

# Task 5

# mydict = {"apple": "алма", "pear": "алмурут", "garlic": "сарымсак", "cucumber": "бадыран"}
# print(", ".join(mydict.keys()))

# Task 6

# mydict = {"apple": "алма", "pear": "алмурут", "garlic": "сарымсак", "cucumber": "бадыран"}
# mydict2 = mydict.copy()
# print(mydict2)

# Task 7

# mydict = {"apple": "алма", "pear": "алмурут", "garlic": "сарымсак", "cucumber": "бадыран"}
# for key in mydict.keys():
#     print(key)

# Task 8

# mydict = {"apple": "алма", "pear": "алмурут", "garlic": "сарымсак", "cucumber": "бадыран"}
# for value in mydict.values():
#     print(value)

# Task 9

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# print("Before\t: ", a)
# for key, value in a.items():
#     if a[key] % 2 == 0:
#         a[key] = 2
# print("After\t: ", a)

# Task 10

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3, 'f': 5, 'g': None}
# print("Before\t:", a)
# for key, value in list(a.items()):
#     if a[key] is None:
#         a.pop(key)
# print("After\t:", a)

# Task 11

# pricelist = {"стол": 100, "стул": 50, "диван": 500, "кровать": 800, "комод": 200, "зеркало": 150, "плита": 170}
# for key, value in pricelist.items():
#     pricelist[key] /= 5
# print(pricelist)

#  Task 12

# fruits = {"яблоки": 60, "виноград": 123, "лимон": 101, "мандарин": 85, "апельсин": 170, "груша": 85}
# for key, value in list(fruits.items()):
#     if fruits[key] % 2 == 0:
#         fruits.pop(key)
# print(fruits)

# Task 13
#
# mydict = {"apple": "алма", "pear": "алмурут", "garlic": "сарымсак", "cucumber": "бадыран"}
# newdict = {}
# for key, value in mydict.items():
#     newdict.setdefault(value, key)
# mydict = newdict.copy()
# del newdict
# print(mydict)

# Task 14

# fruits = {"яблоки": 60, "виноград": 123, "лимон": 101, "мандарин": 85, "апельсин": 170, "груша": 85}
# total = sum(list(fruits.values()))
# print(total)

# Task 15

list_ = [1, 2, 3]
dict1 = dict({1: 1, 2: 2, 3: 3})
dict2 = {1: 1, 2: 2, 3: 3}
dict3 = dict.fromkeys(list_, 0)
for item in [dict1, dict2, dict3]:
    print(item, "is of type", type(item))