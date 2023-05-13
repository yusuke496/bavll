import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt
import math
from numpy import exp,loadtxt,pi,sqrt

def G(x):
    return np.exp(-x**2)
def F(x):
    return 2/sqrt(np.pi)*scipy.special.dawsn(x)

ini=-10
fin=10
d=0.1
s=int((fin-ini)/d)
x = np.arange(ini,fin,d)
plt.gca().xaxis.set_minor_locator(tick.MultipleLocator(0.5))
plt.gca().yaxis.set_minor_locator(tick.MultipleLocator(0.05))
plt.grid(which='minor')
#plt.grid()
plt.plot(x,G(x),linewidth=1)
plt.plot(x,F(x),linewidth=1)
plt.show()
