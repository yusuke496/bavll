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
    return 2/sqrt(np.pi)*scipy.special.dawsn(x)

data = loadtxt("4mA.txt")
x = data[:,0]
y = data[:,1]

data = loadtxt("6mA.txt")
x1 = data[:,0]
y1 = data[:,1]

data = loadtxt("8mA.txt")
x2 = data[:,0]
y2 = data[:,1]

wg=761

def B(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def BB(x,delta,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def D(x,delta,wg,a,c,x0):
    return -2.0*a*(G(((x-x0)-delta)/wg)-G(((x-x0)+delta)/wg))+c

#gmodel = Model(B)
gmodel = Model(BB)
#gmodel = Model(D)
#result = gmodel.fit(y1,x=x1,delta=1000,wg=700,a=60,c=1,x0=0.1)
result = gmodel.fit(y1,x=x1,delta=1000,a=60,c=1,x0=0.1)
print(result.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
plt.xlim(-2000, 2000)
plt.ylim(-5, 5)
plt.grid()
plt.plot((x-50)/2, y/10, color="black",label="4mA")
plt.plot((x1-70)/2, y1/10, color="red",label="6mA")
plt.plot((x2-20)/2, y2/10, color="blue",label="8mA")
plt.legend()
#plt.plot(x, result.best_fit, linewidth=1, color="red")
plt.show()
