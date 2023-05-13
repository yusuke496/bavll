import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

data = loadtxt("shielding.txt")
x = data[:,0]
y = data[:,1]

plt.xlabel("B apply (Gauss)")
plt.ylabel("shielding coefficient")
plt.grid()
plt.plot(x,y,".",color="black")
plt.show()
