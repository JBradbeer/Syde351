import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

j14 = 1
b15 = 0.2
mod = 1
k23 = 2
b25 = 0.2
m24 = 1

##############
## y0 = h14
## y1 = theta
## y2 = p24
## y3 = x23
##############

def model(y, t):
	dy0 = -b15*y[0]/j14 - mod*y[2]/m24
	dy1 = y[0]/j14
	dy2 = mod*y[0]/j14 - k23*y[3] - y[2]/m24
	dy3 = y[2]/m24
	return [dy0, dy1, dy2, dy3]

time = np.linspace(0.0, 20.0, 100)
yinit = [5, 0, 0, 2]
y = odeint(model, yinit, time)

plt.plot(time, y[:,0], label="1")
plt.plot(time, y[:,1], label="2") 
plt.plot(time, y[:,2], label="3")
plt.plot(time, y[:,3], label="4")

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
