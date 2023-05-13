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

wg=500.0
a=10.0
b=1.0

def B(x,delta,a):
    return b*a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def D(x,delta,a):
    return -2.0*b*a*(G((x-delta)/wg)-G((x+delta)/wg))

r=0
ini=-3000
fin=3000
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
    y0[i]=B(x[i],100,a)
for i in range(0,s):
    y1[i]=B(x[i],200,a)
for i in range(0,s):
    y2[i]=B(x[i],500,a)
for i in range(0,s):
    y3[i]=B(x[i],1000,a)
for i in range(0,s):
    y4[i]=B(x[i],1500,a)
for i in range(0,s):
    y5[i]=B(x[i],2000,a)


plt.grid()
plt.xlabel('frequency(MHz)')
plt.ylabel('Signal(V)')
plt.plot(x, y0, linewidth=1, color="black",label="Δωz/ΔωD=0.2")
plt.plot(x, y1, linewidth=1, color="red",label="Δωz/ΔωD=0.4")
plt.plot(x, y2, linewidth=1, color="blue",label="Δωz/ΔωD=1")
plt.plot(x, y3, linewidth=1, color="green",label="Δωz/ΔωD=2")
plt.plot(x, y4, linewidth=1, color="magenta",label="Δωz/ΔωD=3")
plt.plot(x, y5, linewidth=1, color="cyan",label="Δωz/ΔωD=4")
plt.legend(loc='upper right')
plt.show()
