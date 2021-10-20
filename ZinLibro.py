import math 
import numpy as np
import scipy.constants as cts

N = 15

def Si(x):
    total = 0
    for k in range(N):
        num = ((-1)**k)*(x**((2*k)+1))
        den = (2*k+1)*math.factorial(2*k+1)
        total = total + num/den
    return total

def Ci(x):
    total = 0
    C = round( (1.-math.gamma(1+1.e-8))*1.e14 )*1.e-6
    # C = math.e
    for k in range(1,N):
        num = ((-1)**k)*(x**(2*k))
        den = (2*k)*math.factorial(2*k)
        total = total + num/den
    return total + np.log(x) + C
    
def Cin(x):
    total = 0
    for k in range(1,N):
        num = ((-1)**(k+1))*(x**(2*k))
        den = (2*k)*math.factorial(2*k)
        total = total + num/den
    return total



fo = 141e6
depthSkin = 5.38e-3
cond = 16.37
lamda = 1.8
H = lamda/4
a = 13e-3
k = ((2*cts.pi)/lamda)
kH = k*H
# kH = pi/2         (para un monopolo de cuarto de onda)

C = round( (1.-math.gamma(1+1.e-8))*1.e14 )*1.e-6

x1 = k*((a**2 + H**2)**.5) + H
x2 = k*((a**2 + H**2)**.5) - H
x3 = k*a

R = 30/(math.sin(kH)**2)
Rterm1 = Cin(x1) + Cin(x2) - 2*Cin(x3)
Rterm2 = ((math.sin(2*kH))/2) * (((x1+x2)*(math.cos(x1)-math.cos(x2)))/(x1**2 + x2**2 + 2*(x3**2)))
Rterm3 = ((math.sin(kH))**2) * ((((x1+x2)*(math.sin(x1)+math.sin(x2)))/(x1**2 + x2**2 + 2*(x3**2)))-(math.sin(x3)/x3))

Rin = R * (Rterm1 + Rterm2 + Rterm3)
Rin2 = R * (Cin(2*kH) - ((math.sin(kH)**2)))

X = 30/(math.sin(kH)**2)
Xterm1 = Si(x1) + Si(x2) - 2*Si(x3)
Xterm2 = ((math.sin(2*kH))/2) * (((x1+x2)*(math.sin(x1)-math.sin(x2)))/(x1**2 + x2**2 + 2*(x3**2)))
Xterm3 = ((math.sin(kH))**2) * ((((x1+x2)*(math.cos(x1)+math.cos(x2)))/(x1**2 + x2**2 + 2*(x3**2)))-(math.cos(x3)/x3))

Xin = X * (Xterm1 - Xterm2 + Xterm3)
Xin2 = X * (Si(2*kH) - ((math.sin(kH)**2)/(k*a)))

print("Rin = ","{:2.4f}".format(Rin))
print("Rin @ a=0 = ","{:2.4f}".format(Rin2))
print("Xin = ","{:2.4f}".format(Xin))
print("Xin @ a=0 = ","{:2.4f}".format(Xin2))