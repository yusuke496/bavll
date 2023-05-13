import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

data = loadtxt("4cmBy.txt")
x = data[:,0]
y = data[:,1]

data = loadtxt("4_5cmBy.txt")
x0 = data[:,0]
y0 = data[:,1]

data = loadtxt("5cmBy.txt")
x1 = data[:,0]
y1 = data[:,1]

data = loadtxt("6cmBy.txt")
x2 = data[:,0]
y2 = data[:,1]

data = loadtxt("7cmBy.txt")
x3 = data[:,0]
y3 = data[:,1]

errx = [0.1,0.1,0.1,0.1]
erry = [50,50,50,50]

plt.xlabel("position (cm)")
plt.ylabel("B (Gauss)")
plt.grid()
plt.errorbar(x,y,xerr=errx,yerr=erry,color="black",label="d=4cm")
plt.errorbar(x0,y0,xerr=errx,yerr=erry,color="red",label="d=4cm")
plt.errorbar(x1, y1,xerr=errx,yerr=erry, color="blue",label="d=5cm")
plt.errorbar(x2, y2,xerr=errx,yerr=erry, color="green",label="d=6cm")
plt.errorbar(x3, y3,xerr=errx,yerr=erry, color="magenta",label="d=7cm")
#plt.legend(loc='upper right')
plt.show()
