import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

J0 = jv(0,x)
plt.plot(x,J0, label=r'$J_0'+'(x)$')
J1 = jv(1,x)
plt.plot(x,J1, label=r'$J_1'+'(x)$')
m = 1/2
y = m*x
plt.plot(x,y, label=r'y(x)')

kro = 2.26-2.26j
# kro = 3.195962
print("Jo("+str(kro)+")={:2.4e}".format(jv(0,kro)))
print("J1("+str(kro)+")={:2.4e}".format(jv(1,kro)))

plt.ylim([-0.5,1])
plt.legend()
plt.grid()
# plt.show()
plt.savefig ("BesselFunctionOrder0_1.jpg")