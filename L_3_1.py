def my_del(arg_1, arg_2):
    res = arg_1/arg_2
    return res

arg_1 = int(input('Введите первое число: '))
arg_2 = int(input('Введите второе число: '))
if arg_2 != 0:
    print(my_del(arg_1, arg_2))
else:
    print('Делить на 0 нельзя')


