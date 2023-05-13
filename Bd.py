import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

data = loadtxt("Bd.txt")
x = data[:,0]
y = data[:,1]

errx = [0.1,0.1,0.1,0.1,0.1]
erry = [50,50,50,50,50]

plt.xlabel("distance (cm)")
plt.ylabel("B (Gauss)")
plt.ylim(0,3500)
plt.grid()
plt.errorbar(x,y,color="black")
plt.show()
