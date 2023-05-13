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

b=1
a=18.59
wg=403

def B(x,delta,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def D(x,delta,wg,a,c,x0):
    return -2.0*a*(G(((x-x0)-delta)/wg)-G(((x-x0)+delta)/wg))+c

gmodel = Model(B)
#gmodel = Model(D)
result = gmodel.fit(y,x=x,delta=500,c=1,x0=0.1)

print(result.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
plt.xlim(-3000, 3000)
plt.ylim(-40, 40)
plt.grid()
plt.plot(x, y, ".", markersize=1, color="black")
plt.plot(x, result.best_fit, linewidth=1, color="red")
plt.show()
