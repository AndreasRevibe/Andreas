import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

m= np.array([0.002, 0.003, 0.004, 0.005, 0.006])
steps=200
f=np.linspace(100,140,steps)
ff=120
w_ff = 2*math.pi*ff
w=2*math.pi*f
g=9.81
k_f=m*w_ff**2
d_e_t=0.58       #Ns/m
d_m=0.2071       #Ns/m

d=np.array([0.178, 0.211, 0.245, 0.286, 0.312])
k_t=np.array([4.83, 6.42, 7.84, 9.37, 10.3])
R_coil=np.array([215.6, 236.7, 254.2, 271.8, 282.3])
R_load=R_coil

z_max=0.002   #Amplitude limit [m]

C = 12




g_ms = C*g*np.sqrt(2)

Z = np.zeros((len(m),steps))
V_rms = np.zeros((len(m), steps))
Power = np.zeros((len(m), steps))
loss_factor=0.5



# Displacement Amplitude & Power Output
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)


for j in range(0, len(m)):
    for i in range(0, steps):
        Z[j,i] = (g_ms*m[j]*1000)/math.sqrt((k_f[j]-m[j]*w[i]**2)**2+(d[j]*w[i])**2)
        if Z[j,i] > z_max*1000:
            Z[j,i] = z_max*1000
        V_rms[j,i] = ((Z[j,i]/1000)*w[i]*k_t[j])/math.sqrt(2)
        Power[j,i] = loss_factor*1000*(((R_load[j]/(R_load[j]+R_coil[j]))*V_rms[j,i])**2)/R_load[j]
        # Z2[j, i] = (g_ms[j]*m*1000)/math.sqrt((k_f2-m*w[i]**2)**2+(d*w[i])**2)
    ax4.plot(f, Z[j, :], '-', label='Magnet Mass = ' + str(m[j]*1000).format('%f0.2') + 'g', linewidth=1)
    ax5.plot(f, Power[j, :], '-', label='Magnet Mass = ' + str(m[j]*1000).format('%f0.2') + 'g', linewidth=1)
    # ax4.plot(f, Z2[j, :], '-', label=C[j], linewidth=1)
fig4.suptitle('Frequency Response', fontsize=20)
plt.xlabel('Frequency [Hz]', fontsize=18)
plt.ylabel('Amplitude [mm]', fontsize=16)
plt.legend()
fig5.suptitle('Power Output at 12G RMS Steady State Analysis', fontsize=14)
plt.xlabel('Frequency [Hz]', fontsize=10)
plt.ylabel('Power [mW]', fontsize=10)
ax5.grid(b=True, which='major', linestyle='solid')
ax5.grid(b=True, which='minor', linestyle='solid', linewidth=0.5)
plt.legend()



plt.show()
