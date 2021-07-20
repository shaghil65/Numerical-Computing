import math
import scipy
import sympy as sym

eq = "-0.000000000050598*x**3+0.000000038292*x**2+0.000074363*x+0.0088318"
e1 = eval(eq)
der = sym.diff(eq, 'x')
s2= str(der)
def f(x):
    e = e1
    return e
def fDer(x):
    e = eval(str(s2))
    return e

def NR(x0,e,maxSteps):
    step = 1
    flag = 1
    condition = True
    while condition:
        if fDer(x0) == 0.0:
            break
        
        x1 = x0 - f(x0)/fDer(x0)
        print('N-%d   x1 = %0.8f    f(x1) = %0.8f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > maxSteps:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Converge')

x0 = input('Enter Initial Number: ')
x0 = float(x0)
NR(x0,0.000001,100)