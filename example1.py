a = int(input('Введите a = '))
b = int(input('Введите b = '))
if b == a * a:
    print (f'{a}, {b} -> да')  # или такой вариант ((b == a * a) or (a == b * b)):
elif a == b * b:                                              #  and
    print (f'{b}, {a} -> да')
else:
    print (f'{a}, {b} -> нет')


# ТЕРНАРНЫЙ ОПЕРАТОР
# a = int(input('Введите a = '))
# b = int(input('Введите b = '))
# ptint('yes' if (b == a * a) or (a == b * b)) else 'no')