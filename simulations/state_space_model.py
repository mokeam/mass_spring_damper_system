import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Parameters defining the system
c = 4 # Damping constant
k = 2 # Stiffness of the spring
m = 20 # Mass
F = 5 # Applied Force
F_t = np.ones(202)*F

# Simulation Parameters
start_time = 0
stop_time = 100
increment = 0.5
time = np.arange(start_time, stop_time + 1, increment)

# System matrices
A = [[0, 1], [-k/m, -c/m]]
B = [[0], [1/m]]
C = [[1, 0]]
system = sig.StateSpace(A, B, C, 0)

# Step response for the system
time, y, x = sig.lsim(system, F_t, time)
x1 = x[:, 0]
x2 = x[:, 1]

plt.plot(time, x1, time, x2)
plt.title('Simulation of a Mass Spring Damper System')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.grid()
plt.show()