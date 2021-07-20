import numpy as np

#matrix = np.array([[83,11,-4,95],[7,52,13,104],[3,8,29,71]])
matrix = np.array([[8,-3,2,45],[4,11,-1,71],[6,3,12,35]])

def funJacobi(matrix,e,x0=0,y0=0,z=0):
    n = 1
    isValueCheck = False
    a = np.delete(matrix, 3, 1)
    D = np.diag(abs(a))
    S = np.sum(abs(a), axis=1) - D

    if np.all(D>S):
        print('Matrix is diagonally dominant')
        isValueCheck = True
    else:
        print('Matrix is not diagonally dominant')
        isValueCheck = False
    if(isValueCheck):
        f1 = lambda x,y,z: (matrix[0][3] - matrix[0][1]*y - matrix[0][2]*z) / matrix[0][0] 
        f2 = lambda x,y,z: (matrix[1][3] - matrix[1][0]*x - matrix[1][2]*z) / matrix[1][1]
        f3 = lambda x,y,z: (matrix[2][3] - matrix[2][0]*x - matrix[2][1]*y) / matrix[2][2]

        x0 = 0
        y0 = 0
        z0 = 0
        count = 1
        condition = True

        while condition:
            x1 = f1(x0,y0,z0)
            y1 = f2(x0,y0,z0)
            z1 = f3(x0,y0,z0)
            print('%d\t%0.6f\t%0.6f\t%0.6f\n' %(count, x1,y1,z1))
            e1 = abs(x0-x1);
            e2 = abs(y0-y1);
            e3 = abs(z0-z1);
            
            count += 1
            x0 = x1
            y0 = y1
            z0 = z1
            
            condition = e1>e and e2>e and e3>e

        print('\nSolution: x=%0.6f, y=%0.6f and z = %0.6f\n'% (x1,y1,z1))

funJacobi(matrix,0.0001,0,0,0)