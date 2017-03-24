#importing the packages necessary to perform mathematical operations and plotting the functions
import numpy as np
import math
import matplotlib.pyplot as plt

#determining the size of a step
step= 0.001        
#determining the maximum of the charge distribution function h
h=1

#constructing the function that represents the charge distribution, for each x value it gives the value of p(x), the value of h is set previously, the value of the charge distribution at 4+step is guessed so that evaluating the electric field and the voltage in the ranhe [0,4] 

def chargeDist(x):
    calcx=0
    if 1<=x<2:
       calcx= h
    if 2<=x<3:
       calcx=-h
    if x>(4+step):
       print("The x value is outside the boundaries [0,4]",x)
    if 0<= x <1 or 3<= x <=(4+step):
       calcx=0
    return calcx




#constructing the x-array against which electric field and voltage will be plotted
xarray=[]
i=0
while i<((4/step)+1):
      x=i*step
      xarray.append(x)
      i=i+1 



#implementing the Euler method to perform the numerical integration of the charge distribution

y=0
yVect= []
i=0
x=0
while i<((4/step)+1):
    x= i*step
    y=y+(step*chargeDist(x))
    yVect.append(y)
    i=i+1





#implementing the fourth order Runge-Kutta method to perform the numerical integration of the charge distribution

i=0
x=0
y=0
yVect2=[]
while i<((4/step)+1):
      x= i*step
      k1=chargeDist(x)
      k2=chargeDist(x+(0.5*step))
      k3=k2
      k4=chargeDist(x+step)
      y=y+(step*((k1/6)+(k2/3)+(k3/3)+(k4/6)))
      yVect2.append(y)
      i=i+1


#plotting the electric field in the range [0,4]
plt.plot(xarray,yVect,"r")
plt.title("Electric Field computed using the Euler Method")
plt.xlabel("x")
plt.ylabel("Electric Field")
plt.show()



#plotting the electric field in the range [0,4] obtained using the RK-4 method
plt.plot(xarray,yVect,"b")
plt.title("Electric Field computed using the RK-4 Method")
plt.xlabel("x")
plt.ylabel("Electric Field")
plt.show()

   

#implementing the Euler method to find the voltage V(x) (the values of E(x) that are used are those in yVect2, because it is assumed to be more precise)
i=0
x=0
y=0
VoltVect=[]
while i<((4/step)+1):
       x= i*step
       y=y-(step*yVect2[i])
       VoltVect.append(y)
       i=i+1
 

#plotting the voltage V(x) computed using the Euler method
plt.plot(xarray, VoltVect, "r")
plt.title("Voltage computed using the Euler method")
plt.xlabel("x")
plt.ylabel("Voltage")
plt.show()


#implementing the RK4  method to find the voltage V(x) (the values of E(x) that are used are those in yVect2 
#Note:because the value of the electric field at the midpoints in between the steps is not known, those values are extrapolated from a line connecting the two points (i.e. a simple average of starting and final point is evaluated)     
i=0
x=0
y=0
VoltVect2=[]
while i<((4/step)+1):
      #the last value of the Voltage array is computed using Euler because we do not have a successive step in the E-field array
      if i==(4/step):
         y =y-(step*yVect2[i])
         VoltVect2.append(y)
      else:
         k1=-yVect2[i]
         k2=-((yVect2[i+1]+yVect2[i])*0.5)
         k3=k2
         k4=-yVect2[i+1]
         y=y+(step*((k1/6.+(k2/3)+(k3/3)+(k4/6)))
         VoltVect2.append(y)
      i=i+1

#plotting the voltage V(x) computed using the RK-4 method
plt.plot(xarray, VoltVect2,"b")
plt.title("Voltage computed using the Euler and the RK-4 methods")
plt.xlabel("x")
plt.ylabel("Voltage")
plt.show()
