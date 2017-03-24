from MyMatrix import MyMatrix
import numpy as np

data= np.loadtxt("testData.txt")

data2=np.loadtxt("SimultaneousVector.txt")
SimVect=np.matrix(data2)

data3= np.loadtxt("SimultaneousMatrix.txt")

matr= MyMatrix(10,3)
matr.set_matrix(data)

matr2=np.matrix([[1,4,2],[2, 7, 1]])
matr3=np.matrix([[1,2],[1,2],[1,2]])
matr4=matr2*matr3

SimulMatr=np.matrix(data3)

invMatrix= np.linalg.inv(SimulMatr)

SimVectTr=np.transpose(SimVect)

coeffs=


print(SimVect)

#print(coeffs)
print(matr2)
print(matr)



