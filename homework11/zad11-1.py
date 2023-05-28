#!/usr/bin/python3
import math
import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 20, 250, 1.0, 0.1

t = np.linspace(0, T, num = Nt+1, dtype=float)
x = np.linspace(0, L, num = Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = D * dt / (dx * dx)
print( "r = {}".format(4))
assert r < 0.5

u = np.empty((Nx+1, Nt+1), dtype=float)

# initial condition, t = 0
u[:,0] = 2 * x * x + 3

u[0,:] = 0.1
u[Nx,:] = 2.0

for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

print(u)
plt.title("1D heat equation")
plt.xlabel("time")
plt.ylabel("x")
plt.imshow(u[:,::3], cmap="hot", interpolation="nearest")

plt.colorbar()
plt.show()
input()