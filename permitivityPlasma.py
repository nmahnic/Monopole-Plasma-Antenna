from math import pi
import matplotlib.pyplot as plt
import numpy as np

wp = 61.799e9
v_col = 500e6

w = np.linspace(0,1000000000000,1000000)
wo = 152e6*2*pi

er = 1-((wp*wp)/(w*(w-v_col*1j)))
erPrint = 1-((wp*wp)/(wo*(wo-v_col*1j)))

print("\tpermitivity = ", "{:.4e}".format(erPrint))

# setting the axes at the centre
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.set_xscale('log')
ax.set_yscale('log')

plt.ylim([0.1,10e4])

# plot the function
plt.plot(w,abs(er.real), 'r',label = '$Re\{-\epsilon_{r}\}$')
plt.plot(w,abs(er.imag), 'g',label = '$Img\{-\epsilon_{r}\}$')


plt.axvline(x=wp, color='k', linestyle='--')
plt.axvline(x=(152e6*2*pi), color='b', linestyle='--')

plt.grid(True,which="both")
plt.title(r"$\omega$p = "+"{:.2e}".format(wp)+r" rad/seg, $\nu$_col = "+"{:.2e}".format(v_col)+" 1/seg")
plt.xlabel(r"$\omega$")
plt.ylabel(r"$\|\epsilon_{r}\|$")
plt.legend()

# show the plot
plt.show()