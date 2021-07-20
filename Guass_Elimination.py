import numpy as np

def fundynamicFor(a):
    n=len(a)
    x = np.zeros(n)

    for i in range(n):
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - (ratio * a[i])[k]
    return a
    
print('--------------------------------------')

def backS(a):
    n = len(a)-1
    kvalue = np.zeros(n+1)
    for i in range(n,-1,-1):
        cons = a[i][n+1]
        if(i==n):
            kvalue[i] = cons/a[i][i]
        else:
            mid = 0
            for j in range(n,-1,-1):
                if(a[i][j] != 0. and a[i][j] != a[j][j]):
                    a_kvalue = kvalue[j]
                    a_cellvalue = a[i][j]*(-1)
                    mid = mid + (a_kvalue*a_cellvalue)
            kvalue[i] = (cons + mid) / a[i][i]
    return kvalue


eq_var1 = np.array([[25, 5, 1, 106.8],[64, 8, 1, 177.2],[144, 12, 1, 279.2]])
forward = fundynamicFor(eq_var1)
print(forward)

backward = backS(forward)
res = backward
print('Solution vector is',res)