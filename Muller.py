import math

def f(x):
    return math.cos(x)-1.3*x

def Muller(x0 ,x1, x2,Tolerance):
    n = 0
    condition=True
    while(condition):
        h1 = x1-x0
        h2 = x0 - x2
        g = h2/h1
        c = f(x0)
        numer = g*f(x1) - f(x0)*(1+g) + f(x2)
        denom = g*h1**2*(1+g)
        a = numer/denom
        numer1 = f(x1) - f(x0) - a*h1**2
        b = numer1/h1
        if b < 0:
            root = (x0 - ((2*c)/(b - math.sqrt(b**2 - 4*a*c))))
        else:
            root = (x0 - ((2*c)/(b + math.sqrt(b**2 - 4*a*c))))
        print('N-%d   x0 = %0.8f   x1 = %0.8f   x2 = %0.8f    f(x0) = %0.8f     f(x1) = %0.8f      f(x2) = %0.8f    root = %0.8f' % (n,x0,x1,x2,f(x0),f(x1),f(x2),root))
        if root > x0:
            x0 = x1
            x1 = x2 
            x2 = root 
        if root < x0:
            x0 = x1
            x1 = x2 
            x2 = root 
        n = n + 1
        if(abs(f(root)) < Tolerance):
            condition = False

    print("The root is : ",root)
Muller(1,2,3,0.01)

