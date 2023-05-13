import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt
from scipy.optimize import minimize

def G(x):
    return np.exp(-x**2)
def F(x):
    return scipy.special.erfi(x)*G(x)

delta=500
wg=266.0
a=10.0
b=1.0

def B(x,wg,a):
    return b*a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def D(x,wg,a):
    return -2.0*b*a*(G((x-delta)/wg)-G((x+delta)/wg))

data = loadtxt("C:/Users/yusuke/OneDrive/ドキュメント/codes/python/bavll/data/t-davll3.txt")
xx = data[:,0]
yy = data[:,1]
r=0
ini=-3000
fin=3000
d=1.00
s=int((fin-ini)/d)
x = np.arange(ini,fin,d)
y = np.arange(ini,fin,d)
z = np.arange(ini,fin,d)
for i in range(0,s):
    y[i]=B(x[i],wg,a)
for i in range(0,s):
    z[i]=D(x[i],wg,a)

plt.grid()
plt.plot(x, y, linewidth=1, color="black")
plt.plot(x, z, linewidth=1, color="red")
plt.plot(xx,yy)
plt.show()
