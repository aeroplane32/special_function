import numpy as np
import matplotlib.pyplot as plt

def fc(x,n):
    y=np.ones(500)
    for m in range(1,n+1):
        y = y + 2*np.sinc(m/2)*np.cos(np.pi*x/4*m)
    return y

def dfs(T):
    t=np.linspace(-5,5,500)
    x=np.arange(-100,100)*2*np.pi/T
    y=8/T*np.sinc(2*x)
    plt.plot(t,8/T*np.sinc(2*t))
    plt.stem(x,y)

plt.subplot(221)
dfs(8)

plt.grid(axis='both',linewidth=0.5)
plt.xlim((-2,2))
plt.ylabel('cn')
plt.title('T=8')

plt.subplot(222)
dfs(32)
plt.grid(axis='both',linewidth=0.5)
plt.xlim((-2,2))
plt.ylabel('cn')
plt.title('T=32')

plt.subplot(223)
dfs(80)
plt.grid(axis='both',linewidth=0.5)
plt.xlim((-2,2))
plt.ylabel('cn')
plt.title('T=80')

plt.subplot(224)
dfs(160)
plt.grid(axis='both',linewidth=0.5)
plt.xlim((-2,2))
plt.ylabel('cn')
plt.title('T=160')

plt.show()
