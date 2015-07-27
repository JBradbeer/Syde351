import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



##############
## y0 = h14 
## y1 = theta
## y2 = p24
## y3 = x23
##############

def model(y, t):
	h14 = y[0]
	theta = y[1]
	p24 = y[2]
	x23 = t

	
	b15 = 0.2
	k23 = 2
	b25 = 0.2
	m24 = 1

	j14 = 1 + m24*x23**2
	mod = (h14/j14)*x23*m24

	dh14 = -b15*h14/j14 - mod*p24/m24
	dtheta = h14/j14
	dp24 = mod*h14/j14 - k23*x23 - p24/m24
	return [dh14, dtheta, dp24]

x = np.linspace(-1.0, 1.0, 100)
yinit = [10, 0, 0]
y = odeint(model, yinit, x)

plt.plot(x, y[:,0], label="h14")
plt.xlabel('Position')
plt.ylabel('Angular Momentum')
plt.legend()
plt.show()

plt.plot(x, y[:,1], label="theta")
plt.xlabel('Position')
plt.ylabel('Angle of rotation')
plt.legend()
plt.show()

plt.plot(x, y[:,2], label="p24")
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.legend()
plt.show()

