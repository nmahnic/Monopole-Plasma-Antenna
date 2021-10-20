import scipy.constants as cts
from scipy.special import jv
import cmath

skinDepth = 5.31e-3
cond = 14.54
ro = 12e-3

f = 152e6
w = 2*cts.pi*f

k = (1/skinDepth)-(w/cts.c)*1j
a = (k*ro).real
print("k={:.3e}".format(k))
print("kro={:.3e}".format(k*ro))
print("a={:.3e}".format(a))
u = ((k**2)/(cond*w*-1j)).real

print("u={:.3e}".format(u))

jo = jv(0,a)
j1 = jv(1,a)
print("Jo({:2.3f}".format(a)+")={:2.4e}".format(jo))
print("J1({:2.3f}".format(a)+")={:2.4e}".format(j1))

rs = (a)/(2*cts.pi*ro**2*cond*j1)

print("rs={:.4f}".format(rs))

ls = (u*(1+jo))/(2*cts.pi*a*j1)

print("ls={:.6e}".format(ls))