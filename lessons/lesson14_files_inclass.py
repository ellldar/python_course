# READ FROM A FILE

# f = open('file.txt')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line.replace('\n', ''))

# # This is strange but it also works
# for line in f:
#     print(line)

# f.close()

# try:
#     with open('file.txt') as file:
#         for line in file:
#             print(line.rstrip())
# except IOError:
#     print('No such file')

# Playing with CSV

import csv

# filename = 'users.csv'

# users = [
#     ['tom', 23], ['eric', 34], ['bobby', 24]
# ]

# with open(filename, 'w', newline='') as file:
#     writer = csv.writer(file)
#     for row in users:
#         writer.writerow(row)

# with open(filename, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0], '\t|\t', row[1])

# DictReader

# data = [
#     {'name': 'Liana', 'age': 3, 'sex': 'female'},
#     {'name': 'Idris', 'age': 2, 'sex': 'male'},
#     {'name': 'Mariko', 'age': 1, 'sex': 'female'}
# ]

# with open('kids.csv', 'w') as file:
#     columns = ['name', 'age', 'sex']
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(data)

# with open('kids.csv', 'r') as file:
#     print(file.read())

# IN-CLASS TASKS

# Task 1

# file1 = 'numbers.txt'
# file2 = 'squares.txt'
#
# with open(file1, 'w') as file:
#     for num in range(1,21):
#         file.write(str(num) + '\n')
#
# with open(file1, 'r') as f1, open(file2, 'w') as f2:
#     for line in f1:
#         res = int(line) ** 2
#         f2.write(str(res) + '\n')

# Task 2

try:
    with open('usernames.txt', 'a') as file:
        while True:
            name = input("Введите имя пользователя: ")
            if name.lower() == 'end':
                break
            file.write(name + '\t' + str(len(name)) + '\n')
except IOError:
    print("Error with file handling occured!")

print("File is closed!" if file.closed else "File is not closed!")