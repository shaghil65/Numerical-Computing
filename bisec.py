import math
def f(x):
#x^3 - 0.165x^2 + 0.0003993
    f1 = -0.000000000050598*x**3+0.000000038292*x**2+0.000074363*x+0.0088318
    return f1
def bisection(a,b,toll):
    i = 1
    condition = True
    while condition:
        c = (a + b)/2
        print('N-%d, pn = %0.15f & f(pn) = %0.15f' % (i, c, f(c)))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        i = i + 1
        condition = abs(f(c)) > toll
    print('\nRequired Root is : %0.10f' % c)

a = input('First Num: ')
b = input('Second Num: ')
toll = input('Tolerance:  ')
a = float(a)
b = float(b)
toll = float(toll)
if f(a) * f(b) > 0.0:
    print('False values')
else:
    bisection(a,b,toll)