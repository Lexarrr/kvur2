from math import sqrt

baddata = True
while baddata == True:
    try:
        a = int(input('Введите а: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        baddata = False
    except ValueError:
        print('Не удалось получить данные!!!')

D = (b*b) - (4*a*c)

if D>0:
    d = sqrt(D)
    x1 = ((-b) + d / (2 * a))
    x2 = ((-b) - d / (2 * a))
    print(f'Уравнение имеет два корня X1 = {x1}, X2 = {x2}.')

elif D == 0:
    x1 = (-b) / (2 * a)
    print(f'Уравнение имеет один корень X1 = {x1}.')
else:
    print('Уравнение не имеет корней')


