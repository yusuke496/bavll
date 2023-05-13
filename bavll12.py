import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt
from lmfit import Model
import os



def G(x):
    return np.exp(-x**2)
def F(x):
    return 2/sqrt(np.pi)*scipy.special.dawsn(x)

path=os.path.dirname(os.path.abspath(__file__))
path2 = input("type directory name:")
path2 = "/" + path2 + "/"
path = path + path2
#print(path)

path_1=path+"4cm.txt"
path_2=path+"4_5cm.txt"
path_3=path+"5cm.txt"
path_4=path+"6cm.txt"
path_5=path+"7cm.txt"

data1 = loadtxt(path_1)
x1 = data1[:,0]
y1 = data1[:,1]

data2 = loadtxt(path_2)
x2 = data2[:,0]
y2 = data2[:,1]

data3 = loadtxt(path_3)
x3 = data3[:,0]
y3 = data3[:,1]

data4 = loadtxt(path_4)
x4 = data4[:,0]
y4 = data4[:,1]

data5 = loadtxt(path_5)
x5 = data5[:,0]
y5 = data5[:,1]

def B1(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def B2(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def B3(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def B4(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def B5(x,delta,wg,a,c,x0):
    return a*(-2.0*F((x-x0)/wg)+(F(((x-x0)+delta)/wg)+F(((x-x0)-delta)/wg)))+c
def D(x,delta,wg,a,c,x0):
    return -2.0*a*(G(((x-x0)-delta)/wg)-G(((x-x0)+delta)/wg))+c

gmodel1 = Model(B1)
gmodel2 = Model(B2)
gmodel3 = Model(B3)
gmodel4 = Model(B4)
gmodel5 = Model(B5)
#gmodel = Model(D)
result1 = gmodel1.fit(y1,x=x1,delta=2200,wg=700,a=5,c=1.0,x0=0.1)
result2 = gmodel2.fit(y2,x=x2,delta=1500,wg=700,a=2,c=1.0,x0=0.1)
result3 = gmodel3.fit(y3,x=x3,delta=1000,wg=700,a=1,c=1.0,x0=0.1)
result4 = gmodel4.fit(y4,x=x4,delta=500,wg=700,a=0.5,c=1.0,x0=0.1)
result5 = gmodel5.fit(y5,x=x5,delta=50,wg=700,a=0.1,c=1.0,x0=0.1)
print(result1.fit_report())
print(result2.fit_report())
print(result3.fit_report())
print(result4.fit_report())
print(result5.fit_report())
#plt.title("BAVLL spectroscopy")
plt.xlabel("frequency (MHz)")
plt.ylabel("signal (V)")
plt.xlim(-6000, 6000)
plt.ylim(-10, 10)
plt.grid()
#plt.plot(x1, y1, color="black",label="0.3220$T$")
#plt.plot(x2, y2, color="red",label="0.2780$T$")
#plt.plot(x3, y3, color="blue",label="0.2408$T$")
#plt.plot(x4, y4, color="green",label="0.1820$T$")
#plt.plot(x5, y5, color="magenta",label="0.1440$T$")
#plt.plot(x,B4(x,1100,0,0))
plt.plot(x1, result1.best_fit, linewidth=1, color="gray",label="fit1")
plt.plot(x2, result2.best_fit, linewidth=1, color="gray",label="fit2")
plt.plot(x3, result3.best_fit, linewidth=1, color="gray",label="fit3")
plt.plot(x4, result4.best_fit, linewidth=1, color="gray",label="fit4")
plt.plot(x5, result5.best_fit, linewidth=1, color="gray",label="fit5")
plt.legend(loc="upper left")
plt.show()
