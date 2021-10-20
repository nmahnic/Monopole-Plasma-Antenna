import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cts

# 100 linearly spaced numbers
wp = 61.799e9
v_col = 500e6

e_o = cts.epsilon_0
w = np.linspace(0,1.0000e+12,1000000)
fo = 141e6

cond = (e_o*wp*wp)/(v_col+w*1j)

f = [152.34e6, 140.84e6]
for fo in f:
    condPrint = (e_o*wp*wp)/(v_col+(fo*2*cts.pi)*1j)
    print("\tcondMetalPlasma {:.4e}".format(fo), " ={:.4e}".format(condPrint))

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
plt.xscale("log")

# plot the function
plt.plot(w,cond.real, 'g', label = '$Re\{\sigma\}$')
plt.plot(w,-cond.imag, 'r', label = '$Img\{-\sigma\}$')
plt.axvline(x=wp, color='k', linestyle='--')
plt.axvline(x=(fo*2*cts.pi), color='b', linestyle='--')

plt.title(r"$\omega$p = "+"{:.2e}".format(wp)+r" rad/seg, $\nu$_col = "+"{:.2e}".format(v_col)+" 1/seg")
plt.legend()
plt.autoscale
plt.grid(True,which="both")

plt.xlabel("$\omega$")
plt.ylabel("$\sigma$")

plt.show()