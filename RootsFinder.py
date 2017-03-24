import numpy as np
import math
import matplotlib.pyplot as plt


#creating the objects Polynomial, Exponential and SinCos, these are the three functions that the code can find the roots of, once the interval of interest is selected by the user
#each of these objects has methods that enable to find the y-value of the function given a specific x-value and to find the value of the derivative of the function for a given x-value




class Polynomial:
      
#defining the polynomial object, it has the four constant coefficients as arguments
     def __init__(self, a_coeff, b_coeff, c_coeff, d_coeff):
         self.a_coeff= a_coeff
         self.b_coeff= b_coeff
         self.c_coeff= c_coeff
         self.d_coeff= d_coeff


#method for evaluating the function
     def __calcY__(self, x):
         return self.calcY(x)


     def calcY(self, x):
         y= self.a_coeff*(x*x*x)+ self.b_coeff*(x*x)+ self.c_coeff*x+ self.d_coeff
         return y
  


     
     def findInt(self, c, d):
         inter=[]
         step=0.1
         i=1
         while i<((d-c)/step):
               x=c+(i*step)
               prod= self.calcY(x)*self.calcY((x-step))
               if prod < 0:
                  inter.append((x-step))
                  inter.append(x)
               else:
                  continue
         return inter       



          
         
#method for finding the derivative   

     def derivative(self,x):
         der= 3*(self.a_coeff)*(x*x)+ 2*(self.b_coeff)*x+(self.c_coeff) 
         return der       
#=======================================================================
#defining the exponential object, it has a constant that is added to te exponential as argument

class Exponential:

      def __init__(self, const):
         self.const= const

#method for finding the value of the function
      def __calcY__(self, x):
          return self.calcY(x)


      def calcY(self, x):
          y= math.exp(x)+ self.const
          return y






#method for finding the derivative of the function  

      def derivative(self, x):
          der= math.exp(x) 
          return der
#===================================================================================
#defining the sin(omega1*x)*cos(omega2*x) object, it takes the values of the frequencies as arguments 


class SinCos:

      def __init__(self, omega1, omega2):
         self.omega1= omega1
         self.omega2= omega2

#method for finding the value of the function
      def __calcY__(self, x):
          return self.calcY(x)


      def calcY(self, x):
          y= math.sin((self.omega1)*x)*math.cos((self.omega2)*x)
          return y




  
     
#implementing a method which finds the derivative of the function
      def derivative(self, x):
          der= self.omega1*math.cos(self.omega1*x)*math.cos(self.omega2*x)-self.omega2*math.sin(self.omega2*x)*math.sin(self.omega1*x)
          return der    
  
#======================================================================================
# implementing the bisection algorithm to find the roots, Bisection is an object which has the extrema of the range of interest as properties 

class Bisection:
     
      def __init__(self, function):
         self.function= function
     
#implementing a method which looks for the root of the function in the given interval by iteratively finding the middle point of the interval and using that value as one of the extrema of the interval for the next step
#the middle point takes the place of either the minimum of the interval or the maxiumum, depending on which side of the middle point the function changes sign  
      def Bisect(self,a,b):
          n=0
          x1=a
          x2=b
          while (abs(x2-x1))>0.00001:
                xmid= 0.5*(x1+x2)
                prod= self.function.calcY(x1)*self.function.calcY(xmid)     #by looking at the sign of this product, the code checks on which side of the middle point the function changes sign and updates the                                                                               interval accordingly
                n=n+1
                if prod<0:
                   x2=xmid
                elif prod>0:
                   x1=xmid
                else:
                   x1=xmid
                   break 
          return xmid ,n
          
 

#==========================================================
#implementing the Newton-Raphson Method

class NewtonRaphson:
     
     def __init__(self, function):
         self.function= function
#implementing a method that looks for the root of the function in the given interval by computing where the tangents of the curve intersect the x-axis 
     def NewRaph(self, a):
         x1=a
         n=0
         while (abs(self.function.calcY(x1))>0.00001):
               d= (-self.function.calcY(x1))/(self.function.derivative(x1)) 
               x1=x1+d
               n=n+1
         return x1, n 



#===============================================================
#implementing the Secant Method

class Secant:
    
      def __init__(self, function):
          self.function= function

          
#implementing a method that looks for the roots of the function by iteratively finding where the line connecting the points of the function at the extrema of the interval intersect the x-axis     
      def Sec(self, a, b):
          n=0
          x1=a
          x2=b
          while (abs(x2-x1))>0.00001:
                m= (self.function.calcY(x2)-self.function.calcY(x1))/(x2-x1)
                xmid= -(self.function.calcY(x2)/m)+x2
                n=n+1
                x1=x2
                x2=xmid
          return xmid ,n



#==========================================================================
#implementing an Hybrid Method as an object

class Hybrid:

      def __init__(self, function):
          self.function= function


#implementing a method which is an hybrid of the Secant and the Bisection methods
# this method looks for roots using the Secant technique, but if the root ends up outside the original interval (a,b) the method discards that value and looks for another one using the Bisection technique 
      def Hybr(self, a, b):
          n=0
          x1=a
          x2=b
          while (abs(x2-x1))>0.00001:
                xmidBis= 0.5*(x1+x2)
                m= (self.function.calcY(x2)-self.function.calcY(x1))/(x2-x1)
                xmidSec= -(self.function.calcY(x2)/m)+x2
                if a <xmidSec< b:
                   x1=x2
                   x2=xmidSec
                else:
                    prod= self.function.calcY(x1)*self.function.calcY(xmidBis)
                    if prod<0:
                       x2=xmidBis
                    elif prod>0:
                       x1=xmidBis
                    else:
                       x1=xmidBis
                       break
                n=n+1 
          return x1 ,n
          
       


#==========================================================================

#Guiding program
#This program asks the user to choose the function to find the roots of, choose an interval in which to look for a root and then computes it using the three standard methods plus the hybrid one

def main():
     

    type=(input("Enter type of function (exp, SinCos, poly) "))

# Creating the function, the code asks the user to choose one of the 3 functions, the arguments of the three objects are implied in the code

    if (type== 'poly'):
        function=  Polynomial(1, -2.1, -7.4, 10.2)
    elif (type=='exp'):
         function= Exponential(-2)
    elif (type== 'SinCos'):
         function= SinCos(3,1)
    else:
        print ("No functional form specified", type)
        quit() 


   #creating an array to plot the function in the interval -10, 10 
    xarray=[]
    plotFn=[]
    i=0
    step=0.01
    while i<(8/step):
          x=-4+(i*step)
          xarray.append(x)
          y= function.calcY(x)
          plotFn.append(y)
          i=i+1
    n=int(8/step)
    const=[0]*n

#the code plots the function allowing the user to choose a sensible interval in which to look for the root
    plt.plot(xarray, plotFn)
    plt.plot(xarray, const)
    plt.show()






# The codes asks the user to select the interval of interest

    Min=float((input("Enter the minimum extremum of the range: ")))
    Max=float((input("Enter the maximum extremum of the range: ")))
    



#Finding the value of the root and the number of iterations needed to estimate it with the four different techniques

    FoundRootsB= Bisection(function)
    FoundRootsNR= NewtonRaphson(function)
    FoundRootsHybrid= Hybrid(function)
    FoundRootsSec= Secant(function)


#printing the results, allowing the user to check for accuracy and efficiency    

    print("Bisection Method: ",FoundRootsB.Bisect(Min, Max))
    
    print("Newton-Raphson Method: ",FoundRootsNR.NewRaph(Min))
  
    print( "Secant Method: ", FoundRootsSec.Sec(Min, Max))

    print("Hybrid Method: ", FoundRootsHybrid.Hybr(Min, Max))

if __name__ == "__main__":
    main()
