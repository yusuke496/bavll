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

data = loadtxt("4cm.txt")
x = data[:,0]
y = data[:,1]

data = loadtxt("5cm.txt")
x1 = data[:,0]
y1 = data[:,1]

data = loadtxt("6cm.txt")
x2 = data[:,0]
y2 = data[:,1]

data = loadtxt("7cm.txt")
x3 = data[:,0]
y3 = data[:,1]

a=-5.03
wg=741
#wg=1000

def B(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def BB(x,delta,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def BBB(x,delta,wg,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def BBBB(x,delta,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def D(x,delta,wg,a,c,x0):
    return -2.0*a*(G(((x-x0)-delta)/wg)-G(((x-x0)+delta)/wg))+c

#gmodel = Model(B)
#gmodel = Model(BB)
#gmodel = Model(BBB)
gmodel = Model(BBBB)
#gmodel = Model(D)
#result = gmodel.fit(y,x=x,delta=2200,wg=1000,a=6,c=1,x0=0.1)
#result = gmodel.fit(y,x=x,delta=1000,a=60,c=1,x0=0.1)
#result = gmodel.fit(y,x=x,delta=1000,wg=700,c=1,x0=0.1)
result = gmodel.fit(y,x=x,delta=1000,c=1,x0=0.1)
print(result.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
#plt.xlim(-6000, 6000)
#plt.ylim(-50, 50)
plt.grid()
plt.plot(x, -y, color="black")
plt.plot(x1, -y1, color="red")
plt.plot(x2, -y2, color="blue")
plt.plot(x3, -y3, color="green")
plt.plot(x, -result.best_fit, linewidth=1, color="magenta")
plt.show()
