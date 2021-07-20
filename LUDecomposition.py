import numpy as np

A = np.array([[83.0,11.0,-4.0],[7.0,52.0,13.0],[3.0,8.0,29.0]])
B = np.array([95.0,104.0,71.0])

def LU(A):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if(A[i,k] !=0.0):
                lm = A[i,k]/A[k,k]
                A[i,k+1:n] -= lm*A[k,k+1:n]
                A[i,k] = lm
    return A

def Sol(A,B):
    n = len(A)
    for k in range(1, n):
        B[k] -= np.dot(A[k,0:k],B[0:k])
    B[n-1] = B[n-1]/A[n-1,n-1]
    for k in range(n-2,-1,-1):
        B[k] = (B[k] - np.dot(A[k,k+1:n],B[k+1:n]))/A[k,k]
    return B

AP = LU(A)
print(AP)

AS = Sol(AP,B)
print(AS)