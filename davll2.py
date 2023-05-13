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
    return 2/sqrt(np.pi)*scipy.special.dawsn(x)

wg=717.0
a=5.27
b=1.0

def B(x,delta,a):
    return b*a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def D(x,delta,a):
    return -2.0*b*a*(G((x-delta)/wg)-G((x+delta)/wg))

r=0
ini=-4000
fin=4000
d=1.00
s=int((fin-ini)/d)
x = np.arange(ini,fin,d)
y0 = np.arange(ini,fin,d)
y1 = np.arange(ini,fin,d)
y2 = np.arange(ini,fin,d)
y3 = np.arange(ini,fin,d)
y4 = np.arange(ini,fin,d)
y5 = np.arange(ini,fin,d)
for i in range(0,s):
    y0[i]=B(x[i],57,a)
for i in range(0,s):
    y1[i]=B(x[i],154,a)
for i in range(0,s):
    y2[i]=B(x[i],485,a)
for i in range(0,s):
    y3[i]=B(x[i],763,a)
for i in range(0,s):
    y4[i]=B(x[i],1560,a)
for i in range(0,s):
    y5[i]=B(x[i],2000,a)

plt.grid()
plt.xlabel('frequency(MHz)')
plt.ylabel('Signal(V)')
plt.ylim(-10,10)
#plt.plot(x, y5, linewidth=1, color="cyan",label="Δωz/ΔωD=4")
plt.plot(x, y4, linewidth=1, color="black",label="Δωz=1560")
plt.plot(x, y3, linewidth=1, color="red",label="Δωz=763")
plt.plot(x, y2, linewidth=1, color="blue",label="Δωz=485")
plt.plot(x, y1, linewidth=1, color="green",label="Δωz=154")
plt.plot(x, y0, linewidth=1, color="magenta",label="Δωz=57")
plt.legend(loc='upper right')
plt.show()
