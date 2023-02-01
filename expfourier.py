import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.grid(axis='both',linewidth=0.5)
circ = pat.Circle((0,0),radius=1,fill=False,ec='grey',lw=0.5)
ax1.add_patch(circ)
circ = pat.Circle((1/np.sqrt(2),1/np.sqrt(2)),radius=1,fill=False,ec='grey',lw=0.5)
ax1.add_patch(circ)
plt.arrow(0,0,1/np.sqrt(2),1/np.sqrt(2), head_width=0.1, length_includes_head=True)
plt.arrow(1/np.sqrt(2),1/np.sqrt(2),1/np.sqrt(2),-1/np.sqrt(2), head_width=0.1, length_includes_head=True)
plt.axis('equal')
plt.xlim((-2,3))


plt.show()