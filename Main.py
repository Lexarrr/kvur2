baddata = True
while baddata == True:
    try:
        a = int(input('введите a: '))
        b = int(input('введите b: '))
        c = int(input('введите c: '))
        baddata = False

    except:
        print('not found')
D = (b*b) - (4*a*c)
if D>0:
    print('два корня')
elif D == 0:
    print('один корень')
else:
    print('нет корней')
