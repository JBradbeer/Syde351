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
	x23 = y[3]

	
	b15 = 0.2
	k23 = 2
	b25 = 0.2
	m24 = 1

	j14 = 1 + m24*x23**2
	mod = (h14/j14)*x23*m24

	dh14 = -b15*h14/j14 - mod*p24/m24
	dtheta = h14/j14
	dp24 = mod*h14/j14 - k23*x23 - p24/m24
	dx23 = p24/m24
	return [dh14, dtheta, dp24, dx23]

time = np.linspace(0.0, 20.0, 100)
yinit = [10, 0, 0, .5]
y = odeint(model, yinit, time)

counter = 0
label_name = ["h14", "theta", "p24", "x23"]
ylabel = ['Angular Momentum', 'Angle of rotation', 'Momentum', 'Displacement']

for i < 4:
	plt.plot(time, y[:, counter], label = label[counter])
	plt.xlabel('t')
	plt.ylabel(ylabel(counter))
	plt.legend()
	plt.show()
	i += 1

