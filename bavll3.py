import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt
from scipy.optimize import minimize

data = loadtxt("C:/Users/yusuke/Documents/codes/python/bavll.dat")
x = data[:,0]
y = data[:,1]
z = [0 for i in range(0,len(x))]
b=1.0

def G(x):
    return np.exp(-x**2)
def F(x):
    return integrate.quad(lambda y:np.exp(y**2),0,x)[0]*G(x)*2/math.sqrt(3.1415926)
def B(x,delta,wg,a):
    return b*a*(-2.0*F(x/wg)+(F((x+delta)/wg)+F((x-delta)/wg)))
def R(delta,wg,a):
    for i in range(0,len(x)):
        z[i]=B(x[i],delta,wg,a)
    r=0
    for i in range(0,len(x)):
        r+=(y[i]-z[i])**2
    return r

delta=1000.0
wg=1000.0
a=9.0
r1=100000.0
r2=100000.0
r3=100000.0
step=1
for i in range(0,len(x)):
    z[i]=B(x[i],delta,wg,a)

while r1>R(delta,wg,a):
    r1=R(delta,wg,a)
    a=a+step
    print(r1)
while r2>R(delta,wg,a):
    r2=R(delta,wg,a)
    delta=delta-step
    print(r2)
while r3>R(delta,wg,a):
    r3=R(delta,wg,a)
    wg=wg-step
    print(r3)
plt.plot(x, y, ".", color="red")
plt.plot(x, z, linewidth=1, color="black")
plt.show()
print(R(delta,wg,a),a,wg,delta)
