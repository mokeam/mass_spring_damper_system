import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initialization
start_time = 0
stop_time = 100
increment = 0.5

# Initial condition
x_init = [0,0]

time = np.arange(start_time, stop_time + 1, increment)

# Function that returns dx/dt

def first_order_diff(x, t):
	c = 4 # Damping constant
	k = 2 # Stiffness of the spring
	m = 20 # Mass
	F = 5 # Applied Force

	# State variables
	x1 = x[0]
	x2 = x[1]

	x1_dot = x2
	x2_dot = (F - c * x2 - k * x1) / m

	x_dot = [x1_dot, x2_dot]
	return x_dot

if __name__ == '__main__':
	# Solve ODE
	x = odeint(first_order_diff, x_init, time)

	x1 = x[:,0]
	x2 = x[:,1]

	# Plot the results
	plt.plot(time, x1)
	plt.plot(time, x2)
	plt.title('Simulation of a Mass Spring Damper System')
	plt.xlabel('time')
	plt.ylabel('x(t)')
	plt.legend(["x1: Position", "x2: Velocity"])
	plt.grid()
	plt.show()