print("Введите операцию для выполнения. Операторы: +, -, *, /, //, **. Пример: 5 + 6")
data = input("Введите операцию через пробел: ").split(' ')
num1 = int(data[0])
operation = data[1]
num2 = int(data[2])

if operation == '+':
    print(f"{num1} + {num2} =", num1 + num2)
elif operation == '-':
    print(f"{num1} - {num2} =", num1 - num2)
elif operation == '*':
    print(f"{num1} * {num2} =", num1 * num2)
elif operation == '/' or operation == '//':
    if num2 == 0:
        print("Ошибка! Делитель не может быть равен нулю!")
    elif operation == '/':
        print(f"{num1} / {num2} =", num1 / num2)
    else:
        print(f"{num1} // {num2} =", num1 // num2)
elif operation == '**':
    print(f"{num1} ** {num2} =", num1 ** num2)
else:
    print("Неверная операция!")