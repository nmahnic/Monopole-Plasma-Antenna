import scipy.constants as cts
from scipy.special import jv

skinDepth = 5.31e-3
cond = 14.54
ro = 12e-3

f = 152e6
w = 2*cts.pi*f

k = (1/skinDepth)*(1-1j)
u = ((k**2)/(cond*w*-1j)).real

print("u={:.4e}".format(u))

kroSqrt2 = (k*ro*(2**0.5))
a = kroSqrt2.real
print("kroSqrt2={:.4f}".format(kroSqrt2))

jo = jv(0,a)
j1 = jv(1,a)
print("Jo({:2.3f}".format(a)+")={:2.4e}".format(jo))
print("J1({:2.3f}".format(a)+")={:2.4e}".format(j1))

rs = (a)/(2*cts.pi*ro**2*cond*j1)

print("rs={:.4f}".format(rs))

ls = (u*(1+jo))/(2*cts.pi*a*j1)

print("ls={:.4e}".format(ls))