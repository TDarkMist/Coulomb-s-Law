import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import scienceplots
from matplotlib import animation
from matplotlib.animation import PillowWriter
from Field import ElectricField, Potential
from PointCharge import PointCharge

plt.style.use(['science', 'grid', 'dark_background'])
plt.rcParams['text.usetex'] = False  # critical override

_ = np.linspace(-3, 3, 60)

x,y = np.meshgrid(_, _)

q1 = -1.67639134 * 10**-4
q2 = 1.67639134 * 10**-4

x0, y0 = 0, 0
x1, y1 = -1, 0

R = 0.1

dt = 0.001

p1 = PointCharge(position=(x0,y0),charge=q2,velocity=(0,0),mass=1000)
p2 = PointCharge(position=(x1,y1),charge=q1,velocity=(0,15.90364744),mass=1)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

scat1 = ax.scatter(p1.pos[0], p1.pos[1], s=10, c='b', zorder=0)
scat2 = ax.scatter(p2.pos[0], p2.pos[1], s=10, c='r', zorder=0)


#Electric field

#Ex1, Ey1 = ElectricField(p1.q, x, y, p1.pos[0], p1.pos[1])
#Ex2, Ey2 = ElectricField(p2.q, x, y, p2.pos[0], p2.pos[1])

#Ex = Ex1 + Ex2
#Ey = Ey1 + Ey2

#strm = ax.streamplot(x, y, Ex, Ey, color='white', density=1.5)
"""
#Potential of the particles
V = Potential(p1.q, x, y, p1.pos[0], p1.pos[1]) + Potential(p2.q, x, y, p2.pos[0], p2.pos[1])
cf = ax.contourf(x, y, V, levels=100)
"""
#in the animation for the electric field
"""
   
    V = Potential(p1.q, x, y, p1.pos[0], p1.pos[1]) + Potential(p2.q, x, y, p2.pos[0], p2.pos[1])
    cf = ax.contour(x, y, V, levels=100)
 
"""
######

def animate(i):

    #global strm

    p1.apply_force_from(p2, dt)
    p2.apply_force_from(p1, dt)
    p1.update_position(dt)
    p2.update_position(dt)

    scat1.set_offsets([p1.pos[0], p1.pos[1]])
    scat2.set_offsets([p2.pos[0], p2.pos[1]])

    #Ex1, Ey1 = ElectricField(p1.q, x, y, p1.pos[0], p1.pos[1])
    #Ex2, Ey2 = ElectricField(p2.q, x, y, p2.pos[0], p2.pos[1])

    #Ex = Ex1 + Ex2
    #Ey = Ey1 + Ey2

    #strm = ax.streamplot(x, y, Ex, Ey, color='white', zorder=10, density=1.5)

    return scat1, scat2,

ani = animation.FuncAnimation(fig,animate,interval=50,frames=600)
ani.save('animation.gif', writer=PillowWriter(fps=50))
