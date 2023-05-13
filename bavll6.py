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

data = loadtxt("bavll3.dat")
x = data[:,0]
y = data[:,1]

wg=950

def B(x,delta,a,b,c,x0,gamma):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+b*(x-x0)/((x-x0)**2+gamma**2)+c

gmodel = Model(B)
result = gmodel.fit(y,x=x,delta=900,a=5,b=1000,c=1,x0=0.1,gamma=200)

print(result.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
plt.xlim(-1500, 1500)
plt.ylim(-10, 10)
plt.grid()
plt.plot(x, y, ".", markersize=1, color="black")
plt.plot(x, result.best_fit, linewidth=1, color="red")
plt.show()
