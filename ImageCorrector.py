
#this code improves the quality of images that have been corrupted during their digitalisation process by the misalignement of their lines 

#importing classes that will be uesd thourhout the program
import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
from numpy import fft


#reading the image of interest as a matrix so that it is possible identify its lines as rows of data
im= misc.imread("desync4.pgm")

#showing the image to the user
plt.imshow(im, cmap=plt.cm.gray)
plt.show()


#creating a copy of ther original image, this will be the image whose lines are shifted back to the correct positions and that is shown to the user at the end
shiftedIm=np.copy(im)

#finding the length of the lines of the image
lenLine=len(im[1,:])

#implementing a function which finds the shift between two adjacent lines by computing the product of their fourier transforms and then converting it into real space
def ShiftFinder (a=list, b=list):
    f1=fft.fft(a)
    f2=fft.fft(b)
    vect= f1*(np.conj(f2))
    corr=fft.ifft(vect)
    shift= np.argmax(corr)
    return shift

###################################################################################################


#implementing the main part of the code: the shift of each line with respect to the 2 above it and 4 below it is computed, so that it can be shifted back to the correct position      
i=2
while i<(len(im[:,1])-4):
    

#finding the shifts
       shift=ShiftFinder(shiftedIm[i-1,:], im[i,:])
       shift0= ShiftFinder(shiftedIm[i-2,:], im[i,:])  
       shift2= ShiftFinder(im[i+1,:], im[i,:])  
       shift3= ShiftFinder(im[i+2,:], im[i,:]) 
       shift4= ShiftFinder(im[i+3,:], im[i,:])
       shift5= ShiftFinder(im[i+4,:], im[i,:])                         
      


#implementing a method that checks whether the line of interest is shifted by a significant amount with respect to lines in each proximity (excluding the one diretly above it) if it is not, then the line is left unchanged
       
       if shift2<2:
          shift=0

       elif shift3<2:
            shift=0
           
       elif shift4<2:
            shift=0
      
       elif shift0<2:
            shift=0
           
       elif shift5<2:
            shift=0 
   
 #implementing an algorithm which identifies the parts of a line which are expected to correspond to random noise and substitutes them with the elements of the line above         
       j=0
       while j<lenLine:
             shiftedIm[i,j]=im[i,(j-shift)]
             if j>(lenLine-shift):
                shiftedIm[i,j]=shiftedIm[i-1,j]
             if j<shift:
                  shiftedIm[i,j]=shiftedIm[i-1,j]
             else:
                 shiftedIm[i,j]=shiftedIm[i,j]
               
             j=j+1
       i=i+1


#plotting the corrected image
plt.imshow(shiftedIm, cmap=plt.cm.gray)
plt.show()



   

