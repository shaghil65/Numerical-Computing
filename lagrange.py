import numpy as np

def funLagrangeDynamically(arr, x):
  res = 0
  for i in range(len(arr)): 
    otherValues = []
    for j in range(len(arr)):
      if (i == j):
        xn = arr[i][0]
        iIndexForY = i
      else:
        otherValues.append(arr[j][0])
    q1 =1
    q2 = 1
    for o in range(len(otherValues)):
      q1 *= x- otherValues[o]
      q2 *= xn- otherValues[o]
    L = q1 / q2
    res += L*arr2D[iIndexForY][1]
  return print('Interpolated value at %.3f is %.3f.' % (x, res))

arr2D = np.array ([[5,12],[6,13],[9,14],[11,16]])
arr2D = np.array ([[0,0],[10,227.04],[15,362.78],[20,517.35],[22.5,602.97],[30,901.67]])
funLagrangeDynamically(arr2D,16)