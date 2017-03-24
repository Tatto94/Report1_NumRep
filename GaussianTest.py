from MyGaussianPdf import MyGaussianPdf
import numpy as np
import matplotlib.pyplot as plt

gauss= MyGaussianPdf(1, 0.2, 0, 6)

yrand , xrand =gauss.gaussianRand()


a=gauss.integralNumeric()
b=gauss.integralAnalytic()
error= abs(a-b)/b
print(a)
print(b)
print(error)






