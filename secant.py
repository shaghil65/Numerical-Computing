import math
print('Enter  First Element Of The Interval : ')
x0 = float(input()) 
print('Enter Second Element  Of The Interval : ')
x1 = float(input())    
print("Please Enter Your Equation : ")
equation = input()
N=50
def f(x): 
    e = eval(equation)
    return e 
def secant(x0,x1,toll,N):
    step = 1
    condition = True
    print('n \t x2 \t\t f(x2)')
    while condition:
        if f(x0) == f(x1):
            break
        
        x2 = x0 - ((x1-x0)*f(x0))/( f(x1) - f(x0) )
        print('%d \t %0.8f \t %0.8f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
              
        if step > N:
            print('Not Converge')
            break  
        condition = abs(f(x2)) > toll
    print('\n Required root is: %0.8f' % x2)

secant(x0,x1,0.0001,N)