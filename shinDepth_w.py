import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cts


Ne = 1.2e18
v_col = 500e6
rad = 12e-3

e_o = cts.epsilon_0
w = np.linspace(1e6,50e9,1000000)
fo = 152e6
wo = 2*cts.pi*fo
f1 = 141e6
w1 = 2*cts.pi*f1

cond0 = (Ne*cts.elementary_charge*cts.elementary_charge)/(cts.electron_mass*v_col)
print("sigma0 = ", "{:.4e}".format(cond0))


fig = plt.figure(1)
plt.xscale("log")
plt.yscale("log")

wps = [61.799e9, 3.08995e11, 480e9, 61.799e10]
wp = 61.779e9
# for wp in wps:
print("wp", "{:.4e}".format(wp))
ereal = 1-(((wp*wp)/(v_col*v_col))/(1+((w*w)/(v_col*v_col))))
erealPrint = 1-(((wp*wp)/(v_col*v_col))/(1+((wo*wo)/(v_col*v_col))))
erealPrint1 = 1-(((wp*wp)/(v_col*v_col))/(1+((w1*w1)/(v_col*v_col))))
print("\tepsilon.real", "{:.4e}".format(erealPrint))
eimag = (((wp*wp)/(v_col))/(1+((w*w)/(v_col*v_col))))/w
eimagPrint = (((wp*wp)/(v_col))/(1+((wo*wo)/(v_col*v_col))))/wo
eimagPrint1 = (((wp*wp)/(v_col))/(1+((w1*w1)/(v_col*v_col))))/w1
print("\tepsilon.imag", "{:.4e}".format(eimagPrint))
nimag = np.sqrt((np.sqrt((ereal*ereal)+(eimag*eimag))-ereal)/2)
nimagPrint = np.sqrt((np.sqrt((erealPrint*erealPrint)+(eimagPrint*eimagPrint))-erealPrint)/2)
nimagPrint1 = np.sqrt((np.sqrt((erealPrint1*erealPrint1)+(eimagPrint1*eimagPrint1))-erealPrint1)/2)

nrealPrint = np.sqrt((np.sqrt((erealPrint*erealPrint)+(eimagPrint*eimagPrint))+erealPrint)/2)
nrealPrint1 = np.sqrt((np.sqrt((erealPrint1*erealPrint1)+(eimagPrint1*eimagPrint1))+erealPrint1)/2)
print("\tnreal@","{:.4e}".format(fo)," = " ,"{:.4e}".format(nrealPrint))
print("\tnreal@","{:.4e}".format(f1)," = " ,"{:.4e}".format(nrealPrint1))

print("\tnimag@","{:.4e}".format(fo)," = " ,"{:.4e}".format(nimagPrint))
print("\tnimag@","{:.4e}".format(f1)," = " ,"{:.4e}".format(nimagPrint1))
delta = cts.c/(w*nimag)
deltaPrint = cts.c/(wo*nimagPrint)
deltaPrint1 = cts.c/(w1*nimagPrint1)
print("\tdelta@","{:.4e}".format(fo)," = " ,"{:.4e}".format(deltaPrint))
print("\tdelta@","{:.4e}".format(f1)," = " ,"{:.4e}".format(deltaPrint1))
print("\tratio@","{:.4e}".format(fo)," = " ,deltaPrint/rad)
print("\tratio@","{:.4e}".format(f1)," = " , deltaPrint1/rad)
print("")
# plot the function
plt.plot(w,delta, label = "$\omega$p="+"{:.4e}".format(wp))


plt.axvline(x=wo, color='b', linestyle='--')

# plt.title(r"$\omega$p = "+"{:.2e}".format(wp)+r" rad/seg, $\nu$_col = "+"{:.2e}".format(v_col)+" 1/seg")
# plt.title("Profundidad de penetracion [$\delta$]")
plt.title("Profundidad de penetracion [$\delta$]")

plt.legend()
plt.autoscale
plt.grid(True,which="both")

plt.xlabel("$\omega$")
plt.ylabel("$\delta$")


fig = plt.figure(2)
plt.xscale("log")

ratios = [0.41348687283325036, 0.21292383053791855, 0.10645941656550853, 0.08268800684781734, 0.05322939595738451, 0.041343857076740806, 0.008268762049189412, 0.00413438087824871]
wps2 = [6.1799e+10, 1.2000e+11, 2.4000e+11, 3.0900e+11, 4.8000e+11, 6.1799e+11, 3.0900e+12, 6.1799e+12]

_ = plt.plot(wps2, ratios)
plt.title("Ratios en funcion de [$\omega$p]")
plt.axvline(x=61.799e9, color='g', linestyle='--')

plt.autoscale
plt.grid(True,which="both")

plt.xlabel("$\omega$")
plt.ylabel("ratio")

# plt.show()