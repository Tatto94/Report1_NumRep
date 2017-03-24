import numpy as np
import math
class MyGaussianPdf:

#constructor
    def __init__(self, mean, width, minX, maxX):
       self.mean= mean
       self.width= width
       self.minX= minX
       self.maxX= maxX

#primitive access methods
    def get_width(self):
        return self.width

    def get_mean(self):
        return self.mean

    def get_minX(self):
        return self.minX

    def get_maxX(self):
        return self.maxX


#evaluating values of the function
    def __calcY__(self,x):
        return self.calcY(x)


    def calcY(self, x):
        y= math.exp(-(x-self.get_mean())*(x-self.get_mean())/(2*self.get_width()*self.get_width()))
        return y
        


    def __fmax__(self):
        return self.fmax

    def fmax(self):
        bigX= self.calcY(self.get_mean())
        fmax= bigX+1
        return fmax


    def gaussianRand(self):
        i=1
        rand= []
        xrand= []
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

        return yrand,xrand

    
    

    def integralNumeric(self):
        i=1
        bigY=self.calcY(self.get_mean())
        count=0
        xvec=[0]*500000
        binn=(self.maxX-self.minX)/500000
        while i<500000:
              xvec[i]=(self.minX)+(i*binn)
              i=i+1
        j=0
        while j<500000:
              rand= np.random.uniform(0, bigY)
              yval= self.calcY(xvec[j])
              if yval>rand:
                 count=count+1
              else:
                 count=count
              j=j+1 
        ratio=count/500000
        bigArea= bigY*(self.maxX-self.minX)
        integral=ratio*bigArea
        return integral        
    

    def integralAnalytic(self):
        integral= math.sqrt(2*math.pi)*self.width
        return integral
 
