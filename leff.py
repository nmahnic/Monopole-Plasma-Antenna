import scipy.constants as cts
from scipy.special import jv
import math

skinDepth = 5.31e-3
cond = 14.54
ro = 12e-3
l = 450e-3
f = 152e6
w = 2*cts.pi*f
c = cts.c

k = (1/skinDepth)*(1-1j)
u = ((k**2)/(cond*w*-1j)).real

phi = (w*l)/c
print(phi)
yw = (1-math.cos(phi))/(phi*math.sin(phi))

yw2 = (2*(math.sin(phi/2)**2))/(phi*math.sin(phi))


print("yw={:e}".format(yw))
print("yw2={:e}".format(yw2))
