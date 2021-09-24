import numpy as np
import matplotlib.pyplot as plt

# Parameters defining the system
c = 4 # Damping constant
k = 2 # Stiffness of the spring
m = 20 # Mass
F = 5 # Applied Force

# Simulation Parameters
start_time = 0
stop_time = 100
T_s = 0.5
N = int((stop_time - start_time)/T_s) 
x1 = np.zeros(N+2)
x2 = np.zeros(N+2)
x1[0] = 0 # Initial Position
x2[0] = 0 # Initial Speed

a11 = 1
a12 = T_s
a21 = -(T_s * k) / m
a22 = 1 - (T_s * c) / m

b1 = 0
b2 = T_s / m

# Simulation
for k in range(N+1):
	x1[k+1] = a11 * x1[k] + a12 * x2[k] + b1 * F
	x2[k+1] = a21 * x1[k] + a22 * x2[k] + b2 * F

# Plot the simulation results
time = np.arange(start_time, stop_time + 2 * T_s, T_s)

plt.plot(time, x1)
plt.plot(time, x2)
plt.title('Simulation of a Mass Spring Damper System')
plt.xlabel('time [s]')
plt.ylabel('x(t)')
plt.grid()
plt.legend(["x1: Position", "x2: Velocity"])
plt.show()