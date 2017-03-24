from ExponentialDecay import ExponentialDecay
import numpy as np
import matplotlib.pyplot as plt
import math

#creating the PDF
pdf= ExponentialDecay(2.2, 0, 100)

i=0
taus=[0]*500
while i<len(taus):
      lifetimes= pdf.cumulatRand()
      taus[i]= np.mean(lifetimes)
      i=i+1


plt.hist(lifetimes, bins=50)
plt.title("Exponential Decay data")
plt.xlabel("Decay Time")
plt.ylabel("Number of Events")
plt.show()

#printing estimates on an histagram
plt.hist(taus, bins=50)
plt.title("Estimates of the Lifetime")
plt.xlabel("Estimated Lifetime")
plt.ylabel("Frequency")
plt.show()

#estimate of lifetime with relative error
est=np.mean(taus)
standDev=np.std(taus)
error=standDev/(math.sqrt(len(taus)))

print("Estimated lifetime", est)

print("Error on the estimate", error)

print("Error on a single measurement", standDev)
