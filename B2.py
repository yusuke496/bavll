import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

data = loadtxt("B2.txt")
x = data[:,0]
y = data[:,1]
errx = data[:,2]
erry = data[:,3]
plt.xlim(0,3500)
#plt.ylim(0,1600)
plt.xlabel("B apply (Gauss)")
plt.ylabel("B actual (Gauss)")
#plt.grid()
plt.errorbar(x,y,xerr=errx,yerr=erry,fmt="o",color="black")
plt.show()
