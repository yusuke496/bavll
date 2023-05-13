import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt
from lmfit import Model



def G(x):
    return np.exp(-x**2)
def F(x):
    return scipy.special.erfi(x)*G(x)

data = loadtxt("23.txt")
x = data[:,0]
y = data[:,1]
data = loadtxt("22.txt")
x0 = data[:,0]
y0 = data[:,1]
data = loadtxt("1.txt")
x1 = data[:,0]
y1 = data[:,1]
data = loadtxt("0.txt")
x2 = data[:,0]
y2 = data[:,1]

b=1
#wg=700

def B(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def D(x,delta,wg,a,c,x0):
    return -2.0*a*(G(((x-x0)-delta)/wg)-G(((x-x0)+delta)/wg))+c

gmodel = Model(B)
#gmodel = Model(D)
result = gmodel.fit(y,x=x,delta=500,wg=800,a=60,c=1,x0=0.1)

print(result.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
plt.xlim(-3000, 3000)
plt.ylim(-40, 40)
plt.grid()
plt.plot(x, y, ".", markersize=1, color="black",label="2200Gauss")
plt.plot(x1, y1, ".", markersize=1, color="blue",label="1800Gauss")
plt.plot(x0, y0, ".", markersize=1, color="green",label="1300Gauss")
plt.plot(x2, y2, ".", markersize=1, color="magenta",label="800Gauss")
plt.plot(x, result.best_fit, linewidth=1, color="red",label="fit")
plt.legend()
plt.show()
