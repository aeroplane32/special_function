import numpy as np
import matplotlib.pyplot as plt

def fc(x,n):
    y=np.ones(500)
    for m in range(1,n+1):
        y = y + 2*np.sinc(m/2)*np.cos(np.pi*x/4*m)
    return y

def plotapprox(subplot, n):
    plt.subplot(subplot)
    y=fc(x,n)
    plt.plot(x,y)
    plt.grid(axis='both',linewidth=0.5)
    plt.xlim((-5,5))
    plt.ylabel('S[f](t)')
    plt.title('n={}'.format(n))

x=np.linspace(-5,5,500)
plt.subplot(221)
y=2*(np.heaviside(x+2,0.5)-np.heaviside(x-2,0.5))
plt.plot(np.linspace(-4,4,400),y[50:450])
plt.grid(axis='both',linewidth=0.5)
plt.xlim((-5,5))
plt.ylabel('f(t)')

plotapprox(222,3)
plotapprox(223,15)
plotapprox(224,100)

plt.show()

