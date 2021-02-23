# Task 1

# with open('task1.txt', 'w') as file:
#     data = list([num for num in range(1,11)])
#     for d in data:
#         file.write(str(d) + '\n')
#
# with open('task1.txt', 'r') as file:
#     for num in range(5):
#         print(file.readline().rstrip())
#
# print("File is closed!" if file.close else "File is not closed!")

# Task 2

# with open('task2.txt', 'w') as file:
#     data = list([num for num in range(1,11)])
#     for d in data:
#         file.write(str(d) + '\n')
#
# with open('task2.txt', 'r') as file:
#     for line in file:
#         print(line, end='')
#
# print("File is closed!" if file.closed else "File is not closed!")

# Task 3

# from random import random
#
# with open('task3.txt', 'w+') as file:
#     data = list([int(random() * 20) for _ in range(10)])
#     for d in data:
#         file.write(str(d) + '\n')
#     file.seek(0)
#     for line in file:
#         print(line, end='')

# Task 4

# data = ['First Sentence', 'Second Sentence', 'Some other stuff', 'More data']
#
# try:
#     with open('task4.txt', 'w+') as file:
#         for d in data:
#             file.write(d + '\n')
#         file.seek(0)
#         print("Количество строк:", len(file.readlines()))
# except IOError:
#     print("File open error!")

# Task 5

from random import random

try:
    with open('task5.txt', 'w+') as file:
        data = [int(random() * 20) for _ in range(10)]
        for d in data:
            file.write(str(d) + '\n')
        file.seek(0)
        read_data = file.read().rsplit()
        nums = list(map(int, read_data))
        max_num, min_num = max(nums), min(nums)
        with open('task6.txt', 'w') as file2:
            file2.write(str(max_num) + '\n')
            file2.write(str(min_num) + '\n')
except IOError:
    print("File open error!")