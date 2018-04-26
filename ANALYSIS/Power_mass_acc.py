import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

m= 0.017
steps=200
f=np.linspace(50,90,steps)
ff=120
w_ff = 2*math.pi*ff
w=2*math.pi*f
g=9.81
k_f=m*w_ff**2
d_e_t=0.29      #Ns/m
d_m=0.124       #Ns/m
d=d_e_t+d_m

Z_m=np.linspace(0.001,0.09,10)    #Mechanical damping
Z_e_nom=0.02    #Electric damping


z_max=0.001   #Amplitude limit [m]

C = np.linspace(1, 10, 10)
g_ms = C*g*np.sqrt(2)

Z = np.zeros((len(g_ms),steps))

# Theoretical optimal damping
# d_e = np.zeros(len(C))
# P_max = np.zeros(len(C))
#
# for k in range(0, len(C)):
#     d_e[k]=m*w_ff*np.sqrt((g_ms[k]/(w_ff**2*z_max))**2)-d_m
#     P_max[k]=1000*((1/2)*m*w_ff**2*z_max*(g_ms[k]/w_ff-z_max*d_m/m))
# fig1=plt.figure()
# ax1=fig1.add_subplot(111)
# ax1.plot(C,d_e)
# fig1.suptitle('Optimal electric damping', fontsize=20)
# plt.xlabel('G', fontsize=18)
# plt.ylabel('d_e [Ns/m]', fontsize=16)

Z_e = np.zeros(len(C))
P_max = np.zeros(len(C))

# for k in range(0, len(C)):
#     Z_e[k]=(1/2)*np.sqrt((g_ms[k]/(w_ff**2*z_max))**2)-Z_m[h]
#     P_max[k]=1000*((m*Z_e[k]*(g_ms[k])**2)/(4*w_ff*(Z_m+Z_e[k])**2))
# fig1=plt.figure()
# ax1=fig1.add_subplot(111)
# ax1.plot(C,Z_e)
# fig1.suptitle('Optimal electric damping', fontsize=20)
# plt.xlabel('G', fontsize=18)
# plt.ylabel('Z_e [Ns/m]', fontsize=16)
#
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.plot(C, P_max)
# fig2.suptitle('Maximum Power Output', fontsize=20)
# plt.xlabel('G', fontsize=18)
# plt.ylabel('P [mW]', fontsize=16)

m_loop=np.linspace(0,0.05,100)

P_max_loop=np.zeros((len(C),len(m_loop)))
Z_e_min=np.zeros(len(C))
P_max_Z_e_min = np.zeros(len(C))

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
for h in range(0, len(C)):
    for l in range(0, len(m_loop)):
        # P_max_loop[h,l] = 1000*(m_loop[l]*g_ms[h]**2/(8*w_ff**2*((Z_e+d_m/(2*m*w_ff)))**2))
        Z_e_min[h]=(1/2)*np.sqrt((g_ms[h]/(w_ff**2*z_max))**2)-Z_m[h]
        P_max_loop[h,l] = 0.5*1000*((m_loop[l]*Z_e_min[h]*(g_ms[h])**2)/(4*w_ff*(Z_m[h]+Z_e_min[h])**2))
    ax3.plot(4000*m_loop, P_max_loop[h, :], label = str(C[h]).format('%f0.2') + ' G')
    # Z_e_min[h] = (1/2)*np.sqrt((g_ms[h]/(w_ff**2*z_max))**2)-Z_m
    # P_max_d_e_min[h] = 1000*(d_e_min[h]*g_ms[h]**2/(8*w_ff**2*((d_e_min[h]/(2*m*w_ff))+(d_m/(2*m*w_ff)))**2))
    # P_max_Z_e_min[h] = 1000*((m*Z_e_min*(g_ms[h])**2)/(4*w_ff*(Z_m+Z_e_min)**2))
# ax3.plot(Z_e_loop, P_max_Z_e_min,'+')
fig3.suptitle('Maximum Power Output', fontsize=20)
plt.xlabel('Energy Harvester Mass [g]', fontsize=18)
plt.ylabel('P [mW]', fontsize=16)
ax3.grid(b=True, which='major', linestyle='solid')
ax3.grid(b=True, which='minor', linestyle='dashed', linewidth=0.2)
ax3.minorticks_on()
plt.legend()

plt.show()
