import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt
from lmfit import Model



def G(x):
    return np.exp(-x**2)
def F(x):
    return integrate.quad(lambda y:np.exp(y**2),0,x)[0]*G(x)*2/math.sqrt(3.1415926)

data = loadtxt("bavll.dat")
x = data[:,0]
y = data[:,1]

b=1

def B(x,delta,wg,a):
    return a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def D(x,delta,wg,a):
    return -2.0*a*(G((x-delta)/wg)-G((x+delta)/wg))

#gmodel = Model(B)
gmodel = Model(D)
result = gmodel.fit(y,x=x,delta=1000,wg=1000,a=10)

print(result.fit_report())
plt.plot(x, y, ".", color="black")
plt.plot(x, result.best_fit, linewidth=1, color="red")
plt.show()
