
import cmath
import scipy.constants as cts
from scipy.special import jv

#find the polar coordinates of complex number
a = (1/(2**.5))*(1+1j)
a=1-1j
print ("a=",cmath.polar(a)[0],cmath.polar(a)[1]*(360/(2*cts.pi)))
J0 = jv(0,a)
print ("Jo=",cmath.polar(J0)[0],cmath.polar(J0)[1]*(360/(2*cts.pi)))
print ("Jo=",J0)
J1 = jv(1,a)
print ("J1=",cmath.polar(J1)[0],cmath.polar(J1)[1]*(360/(2*cts.pi)))