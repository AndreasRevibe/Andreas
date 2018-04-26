import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

m= 0.006
steps=200
f=np.linspace(53,73,steps)
ff=63
w_ff = 2*math.pi*ff
w=2*math.pi*f
g=9.81
k_f=m*w_ff**2
d_e_t=0.58       #Ns/m
d_m=0.2071       #Ns/m
d=d_e_t+d_m
k_t=5
R_coil=100
R_load=1000

z_max=0.002   #Amplitude limit [m]

C = np.linspace(5, 10, 5)
g_ms = C*g*np.sqrt(2)

Z = np.zeros((len(g_ms),steps))
V_rms = np.zeros((len(g_ms), steps))
Power = np.zeros((len(g_ms), steps))

# Theoretical optimal damping
d_e = np.zeros(len(C))
P_max = np.zeros(len(C))

for k in range(0, len(C)):
    d_e[k]=m*w_ff*np.sqrt((g_ms[k]/(w_ff**2*z_max))**2)-d_m
    P_max[k]=1000*((1/2)*m*w_ff**2*z_max*(g_ms[k]/w_ff-z_max*d_m/m))
fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.plot(C,d_e)
fig1.suptitle('Optimal electric damping', fontsize=20)
plt.xlabel('G', fontsize=18)
plt.ylabel('d_e [Ns/m]', fontsize=16)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(C, P_max)
fig2.suptitle('Maximum Power Output', fontsize=20)
plt.xlabel('G', fontsize=18)
plt.ylabel('P [mW]', fontsize=16)

d_e_loop=np.linspace(0,1.5,50)

P_max_loop=np.zeros((len(C),len(d_e_loop)))
d_e_min=np.zeros(len(C))
P_max_d_e_min = np.zeros(len(C))

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
for h in range(0, len(C)):
    for l in range(0, len(d_e_loop)):
        P_max_loop[h,l] = 1000*(d_e_loop[l]*g_ms[h]**2/(8*w_ff**2*((d_e_loop[l]/(2*m*w_ff))+(d_m/(2*m*w_ff)))**2))
    ax3.plot(d_e_loop, P_max_loop[h, :], label = str(C[h]).format('%f0.2') + ' G')
    d_e_min[h] = m*w_ff*np.sqrt((g_ms[h]/(w_ff**2*z_max))**2)-d_m
    P_max_d_e_min[h] = 1000*(d_e_min[h]*g_ms[h]**2/(8*w_ff**2*((d_e_min[h]/(2*m*w_ff))+(d_m/(2*m*w_ff)))**2))
ax3.plot(d_e_min, P_max_d_e_min,'+')
fig3.suptitle('Maximum Power Output', fontsize=20)
plt.xlabel('d_e [Ns/m]', fontsize=18)
plt.ylabel('P [mW]', fontsize=16)
plt.legend()

# Second Mass
# k_f2=25266.19
# Z2 = np.zeros((len(g_ms), steps))


# Displacement Amplitude & Power Output
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)


for j in range(0, len(g_ms)):
    for i in range(0, steps):
        Z[j,i] = (g_ms[j]*m*1000)/math.sqrt((k_f-m*w[i]**2)**2+(d*w[i])**2)
        if Z[j,i] > z_max*1000:
            Z[j,i] = z_max*1000
        V_rms[j,i] = ((Z[j,i]/1000)*w[i]*k_t)/math.sqrt(2)
        Power[j,i] = 1000*(((R_load/(R_load+R_coil))*V_rms[j,i])**2)/R_load
        # Z2[j, i] = (g_ms[j]*m*1000)/math.sqrt((k_f2-m*w[i]**2)**2+(d*w[i])**2)
    ax4.plot(f, Z[j, :], '-', label=str(C[j]).format('%f0.2') + ' G', linewidth=1)
    ax5.plot(f, Power[j, :], '-', label=str(C[j]).format('%f0.2') + ' G', linewidth=1)
    # ax4.plot(f, Z2[j, :], '-', label=C[j], linewidth=1)
fig4.suptitle('Frequency Response', fontsize=20)
plt.xlabel('Frequency [Hz]', fontsize=18)
plt.ylabel('Amplitude [mm]', fontsize=16)
plt.legend()
fig5.suptitle('Power Output', fontsize=20)
plt.xlabel('Frequency [Hz]', fontsize=18)
plt.ylabel('Power [mW]', fontsize=16)
plt.legend()


# np.savetxt("ampy_MagCir_dual_0_2g_80_Hz.csv", [Z[0,:],f] , delimiter=",", fmt= '% .4f')
# np.savetxt("ampy_MagCir_dual_0_4g_80_Hz.csv", [Z[1, :], f], delimiter=",", fmt='% .4f')
# np.savetxt("ampy_MagCir_dual_0_6g_80_Hz.csv", [Z[2, :], f], delimiter=",", fmt='% .4f')
# np.savetxt("ampy_MagCir_dual_0_8g_80_Hz.csv", [Z[3, :], f], delimiter=",", fmt='% .4f')
# np.savetxt("ampy_MagCir_dual_1_0g_80_Hz.csv", [Z[4, :], f], delimiter=",", fmt='% .4f')







#Voltage Import from ANSYS
R_load=500


# df = pd.read_excel('ANALYSIS/VRMS_MagCir_dual.xlsx', sheetname='VRMS')
# Freq=df['Frequency']
# RMS_0_2_60 = df['VRMS 0.2G 60']
# RMS_0_2_80 = df['VRMS 0.2G 80']
# RMS_0_4_60 = df['VRMS 0.4G 60']
# RMS_0_4_80 = df['VRMS 0.4G 80']
# RMS_0_6_60 = df['VRMS 0.6G 60']
# RMS_0_6_80 = df['VRMS 0.6G 80']
# RMS_0_8_60 = df['VRMS 0.8G 60']
# RMS_0_8_80 = df['VRMS 0.8G 80']
# RMS_1_0_60 = df['VRMS 1.0G 60']
# RMS_1_0_80 = df['VRMS 1.0G 80']
#
#
# P_Ansys_0_2_60 = np.zeros(len(Freq))
# P_Ansys_0_2_80 = np.zeros(len(Freq))
# P_Ansys_0_2 = np.zeros(len(Freq))
#
# P_Ansys_0_4_60 = np.zeros(len(Freq))
# P_Ansys_0_4_80 = np.zeros(len(Freq))
# P_Ansys_0_4 = np.zeros(len(Freq))
#
# P_Ansys_0_6_60 = np.zeros(len(Freq))
# P_Ansys_0_6_80 = np.zeros(len(Freq))
# P_Ansys_0_6 = np.zeros(len(Freq))
#
# P_Ansys_0_8_60 = np.zeros(len(Freq))
# P_Ansys_0_8_80 = np.zeros(len(Freq))
# P_Ansys_0_8 = np.zeros(len(Freq))
#
# P_Ansys_1_0_60 = np.zeros(len(Freq))
# P_Ansys_1_0_80 = np.zeros(len(Freq))
# P_Ansys_1_0 = np.zeros(len(Freq))
#
#
# for t in range(0,len(Freq)):
#     P_Ansys_0_2_60[t] = 1000*((RMS_0_2_60[t])**2)/R_load
#     P_Ansys_0_2_80[t] = 1000*((RMS_0_2_80[t])**2)/R_load
#     P_Ansys_0_2[t] = P_Ansys_0_2_60[t] + P_Ansys_0_2_80[t]
#
#     P_Ansys_0_4_60[t] = 1000*((RMS_0_4_60[t])**2)/R_load
#     P_Ansys_0_4_80[t] = 1000*((RMS_0_4_80[t])**2)/R_load
#     P_Ansys_0_4[t] = P_Ansys_0_4_60[t] + P_Ansys_0_4_80[t]
#
#     P_Ansys_0_6_60[t] = 1000*((RMS_0_6_60[t])**2)/R_load
#     P_Ansys_0_6_80[t] = 1000*((RMS_0_6_80[t])**2)/R_load
#     P_Ansys_0_6[t] = P_Ansys_0_6_60[t] + P_Ansys_0_6_80[t]
#
#     P_Ansys_0_8_60[t] = 1000*((RMS_0_8_60[t])**2)/R_load
#     P_Ansys_0_8_80[t] = 1000*((RMS_0_8_80[t])**2)/R_load
#     P_Ansys_0_8[t] = P_Ansys_0_8_60[t] + P_Ansys_0_8_80[t]
#
#     P_Ansys_1_0_60[t] = 1000*((RMS_1_0_60[t])**2)/R_load
#     P_Ansys_1_0_80[t] = 1000*((RMS_1_0_80[t])**2)/R_load
#     P_Ansys_1_0[t] = P_Ansys_1_0_60[t] + P_Ansys_1_0_80[t]
# fig5 = plt.figure()
# ax5 = fig5.add_subplot(111)
# ax6 = fig5.add_subplot(111)
# ax7 = fig5.add_subplot(111)
# ax8 = fig5.add_subplot(111)
# ax9 = fig5.add_subplot(111)
# power_0_2, = ax5.plot(Freq, P_Ansys_0_2, '-', linewidth=1, label = str(C[0]).format('%f0.2') + ' G')
# power_0_4, = ax6.plot(Freq, P_Ansys_0_4, '-', linewidth=1, label = str(C[1]).format('%f0.2') + ' G')
# power_0_6, = ax7.plot(Freq, P_Ansys_0_6, '-', linewidth=1, label = str(C[2]).format('%f0.2') + ' G')
# power_0_8, = ax8.plot(Freq, P_Ansys_0_8, '-', linewidth=1, label = str(C[3]).format('%f0.2') + ' G')
# power_1_0, = ax9.plot(Freq, P_Ansys_1_0, '-', linewidth=1, label = str(C[4]).format('%f0.2') + ' G')
#
#
# fig5.suptitle('Power', fontsize=20)
# ax5.legend(handles=[power_0_2, power_0_4, power_0_6, power_0_8, power_1_0])
# plt.xlabel('Frequency [Hz]', fontsize=18)
# plt.ylabel('Power [mW]', fontsize=16)



plt.show()
