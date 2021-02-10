import random

name = input("Введите имя: ")
num = int(random.random() * 20 + 1)
counter = 0
wannaPlay = input("Хотите играть (Да или Нет)? ").lower()
isPlaying = True if wannaPlay == 'да' else False
inputs = set()
while isPlaying:
    guess = int(input("Угадайте число от 1 до 20: "))
    counter += 1
    if guess in inputs:
        print(f"Число {guess} уже было! Введите другое число!")
        continue
    else:
        inputs.add(guess)
    if guess < 1 or guess > 20:
        print("Неправильный диапазон. Введите число от 1 до 20")
    elif guess == num:
        print(f"Отлично {name}! Вы угадали число {num}. Вам потребовалось {counter} попыток")
        wannaPlay = input("Хотите играть (Да или Нет)? ").lower()
        isPlaying = True if wannaPlay == 'да' else False
        if isPlaying:
            counter = 0
            num = int(random.random() * 20 + 1)
else:
    print("Спасибо за участие!")