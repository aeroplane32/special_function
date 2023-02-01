import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import scipy.integrate as si

x=np.linspace(-5,5,500)

y1=np.heaviside(x+1,0.5)-np.heaviside(x-1,0.5)
w1=scipy.fft.fft(y1)
plt.subplot(231)
plt.plot(x,y1)
plt.subplot(234)
plt.plot(x,w1)


y2=np.sinc(x)
y3=np.array(500)
for xi in range(0,499):
    y3[xi]=si.quad(np.sinc,x[xi]-1,x[xi]+1)
#y3=np.convolve(y1,y2)

plt.subplot(232)
plt.plot(x,y2)

plt.subplot(233)
plt.plot(np.linspace(-10,10,999),y3)
plt.show()
