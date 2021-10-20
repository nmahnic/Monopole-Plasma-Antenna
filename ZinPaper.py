import math 
import numpy as np
import scipy.constants as cts

a = 12e-3
d = 5.31e-3
cond = 14.54

N = 15

def num():
    total = 0
    for k in range(1,N):
        ter1 = (-1j/2)**(k)
        ter2 = 1/(math.factorial(k)**2)
        ter3 = (a/d)**(2*k)
        total = total + (ter1*ter2*ter3)
    return total

def den():
    total = 0
    for k in range(1,N):
        ter1 = (-1j/2)**(k)
        ter2 = 1/((math.factorial(k)**2)*(k+1))
        ter3 = (a/d)**(2*k)
        total = total + (ter1*ter2*ter3)
    return total

ro = .45/(cts.pi*a*a*cond)
zw = ro*num()/den()

print("ro={:2.4f}".format(ro))
print("zw={:2.4f}".format(zw))