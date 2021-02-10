# arr = []
# while True:
#     num = int(input("Введите число: "))
#     if num >= 0:
#         arr.append(num)
#     else:
#         break
# print(sum(arr))

import random

x = set()
for _ in range(0, 10):
    x.add(int(random.random() * 20 + 1))

print(x)