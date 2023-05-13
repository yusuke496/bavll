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

wg=100.0
a=10.0
b=1.0

def B1(x,delta,a):
    return b*a*(-2.0*F(x/wg))
def B2(x,delta,a):
    return b*a*((F((x+delta)/wg)+F((x-delta)/wg)))
def B(x,delta,a):
    return b*a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def D(x,delta,a):
    return -2.0*b*a*(G((x-delta)/wg)-G((x+delta)/wg))

r=0
ini=-2000
fin=2000
d=1.00
s=int((fin-ini)/d)
x = np.arange(ini,fin,d)
y0 = np.arange(ini,fin,d)
y1 = np.arange(ini,fin,d)
y2 = np.arange(ini,fin,d)
for i in range(0,s):
    y0[i]=B1(x[i],1000,a)
for i in range(0,s):
    y1[i]=-B2(x[i],1000,a)
for i in range(0,s):
    y2[i]=B(x[i],1000,a)



#plt.grid()
# Turn off tick labels
plt.ylim(-15,15)
plt.subplot(2, 1, 1)
plt.ylabel('arb.unit')
plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
plt.plot(x, y0, linewidth=1, color="black",label="$\chi_x$")
plt.legend()
plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
plt.plot(x, y1, linewidth=1,linestyle="dashed",color="black",label="$\chi_y$")
plt.legend()
plt.ylim(-15,15)
plt.subplot(2, 1, 2)
plt.xlabel('frequency(arb.unit)')
plt.ylabel('arb.unit')
plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
plt.plot(x, y2, linewidth=1, color="black",label="Differential")
plt.legend(loc='upper right')
plt.show()
