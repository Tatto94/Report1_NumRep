import numpy as np
import math
class ExponentialDecay:

#constructor
     def __init__(self,lifetime, minX, maxX):
        self.lifetime= lifetime
        self.minX= minX
        self.maxX= maxX

#evaluate values of the function
     def __calcY__(self,x):
         return self.calcY(x)


     def calcY(self,x):
         area= (self.lifetime)*(1-math.exp(-(self.maxX)/(self.lifetime)))
         y=(math.exp(-(x/self.lifetime)))/area
         return y


     def __fmax__(self):
        return self.amx

     def fmax(self):
         bigX= self.calcY(0)
         fmax= bigX+1
         return fmax


     def functRand(self):
         i=1
         rand= [] 
         xrand=[]
         yrand=[]
         while i<1000:
               rand0= np.random.uniform(0, 1)
               rand1= self.minX+(self.maxX-self.minX)*rand0
               rand2= np.random.uniform(0,1)
               rand3= rand2*self.fmax()   
               if rand3<self.calcY(rand1):
                  yrand.append(self.calcY(rand1))
                  xrand.append(rand1)
                  i=i+1
               else:
                  continue
         return xrand
         
          

     def cumulatRand(self):
         i=1
         xrandVect= []
         yrandVect=[]
         area= (self.lifetime)*(1-math.exp(-(self.maxX)/(self.lifetime)))
         while i<1000:
               rand=np.random.uniform(0,1)
               rand2= -(self.lifetime)*math.log(rand)
               yrandVect.append(self.calcY(rand2))
               xrandVect.append(rand2)
               i=i+1
         return xrandVect
 
