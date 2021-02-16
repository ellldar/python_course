# TRY - EXCEPT - FINALLY - RAISE

# Task 1

# values = input("Введите значения через пробел: ").split(' ')
# print(values)
# try:
#     res = sum(int(v) for v in values)
# except ValueError:
#     res = "".join(values)
# finally:
#     print(res)

# Task 2

# users = {1: 'maksat', 2: 'urmat', 3: 'samat', 4: 'kanat', 5: 'brat', 6: 'svat'}
# users = {value: key for key, value in users.items()}
# try:
#     username = input("Введите имя пользователя: ")
#     user_id = users[username]
#     print(f"ID пользователя - {user_id}")
# except KeyError:
#     print("Введенного юзера нет в базе данных")
# else:
#     print("Добрый день, {}".format(username))
# finally:
#     print("Спасибо!")

# Task 3

# try:
#     age = int(input("Введите свой возраст: "))
#     if not age > 0:
#         raise Exception("Ваш возраст должен быть больше 0")
# except ValueError:
#     print("Введите возраст в числовом формате")
# else:
#     print(f"Ваш возраст {age}")

# Task from the previous exercise

students = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91},
    'Olga': {'history': 92, 'math': 96, 'literature': 81},
    'Nik': {'history': 84, 'math': 85, 'literature': 87},
    'Pedro': {'history': 97, 'math': 85, 'literature': 93}
}

mydict_ = {key: key2
           for key, value in students.items()
           for key2, value2 in value.items()
           if value[key2] == max(value.values())
           }

print(mydict_)