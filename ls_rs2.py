import scipy.constants as cts
from scipy.special import jv

skinDepth = 5.31e-3
cond = 14.54
ro = 12e-3

f = 152e6
w = 2*cts.pi*f

# k = (1/skinDepth)*(1-1j)
k = (1/skinDepth)-(w/cts.c)*1j
a = k*ro
print("k={:.3e}".format(k))
print("a={:.3e}".format(a))
u = ((k**2)/(cond*w*-1j)).real

print("u={:.3e}".format(u))

jo = jv(0,a)
j1 = jv(1,a)
print("Jo({:2.3f}".format(a)+")={:2.4e}".format(jo))
print("J1({:2.3f}".format(a)+")={:2.4e}".format(j1))

Zs = (a*jo)/(2*cts.pi*ro*cond*j1)

print("Zs={:.4e}".format(Zs))