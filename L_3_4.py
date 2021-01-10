def my_func(x, y):
    c = x**y
    return c

x = int(input('Введите целое положительное число: '))
if x > 0:
    y = int(input('Введите целое отрицательное число: '))
    if y < 0:
        print(f'Ответ: {my_func(x, y)}')
    else:
        print('Вы ввели неправильное число!')
else:
    print('Вы ввели неправильное число!')

def my_func1(x, y):
    c = 1
    for i in range(abs(y)):
        c *= x
    if y >= 0:
        return c
    else:
        return 1 / c

x = int(input('Введите целое положительное число: '))
if x > 0:
    y = int(input('Введите целое отрицательное число: '))
    if y < 0:
        print(f'Ответ: {my_func1(x, y)}')
    else:
        print('Вы ввели неправильное число!')
else:
    print('Вы ввели неправильное число!')