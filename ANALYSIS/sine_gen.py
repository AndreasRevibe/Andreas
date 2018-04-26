import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def generate_velocity_vector(f_min, f_max, df, dt, num_periods, g_rms):
    freq = np.arange(f_min, f_max+df, df)
    print(freq)
    a = []
    t_tot = 0
    t_change_freq = []
    for f in freq:
        T = 1/f
        t = np.arange(0, num_periods*T, dt)
        t_change_freq.append(t_tot)
        t_tot = t_tot + num_periods*T

        a.extend(g_rms*np.sqrt(2)*np.sin(2*np.pi*f*t)/(2*np.pi*f))

    t = np.linspace(0, 1, len(a))*t_tot

    a = np.asarray(a)
    print(np.shape(t))
    print(np.shape(a))

    return(t, a, t_change_freq, freq)

g=12
g_val=9.81*g

(t, v, t_change_freq, freq) = generate_velocity_vector(f_min=100, f_max=140, df=0.5, dt=0.0001, num_periods=120, g_rms=g_val)
"""
with open('sine_sweep_12g_100_140Hz.csv','w') as textfile:
    for i in range(len(t)):
        textfile.write(str(t[i])+','+str(v[i])+'\n')
"""
t_sim_02 = []
V_sim_02 = []
t_sim_04 = []
V_sim_04 = []
t_sim_06 = []
V_sim_06 = []
t_sim_08 = []
V_sim_08 = []
t_sim_10 = []
V_sim_10 = []

with open('2g_Voltage_Sweep.csv', 'r') as textfile:
    header = next(textfile)
    for line in textfile:
        line = line.split(',')
        t_sim_02.append(float(line[0]))
        V_sim_02.append(float(line[1]))

with open('3g_Voltage_Sweep.csv', 'r') as textfile2:
    header = next(textfile2)
    for line in textfile2:
        line = line.split(',')
        t_sim_04.append(float(line[0]))
        V_sim_04.append(float(line[1]))

with open('4g_Voltage_Sweep.csv', 'r') as textfile3:
    header = next(textfile3)
    for line in textfile3:
        line = line.split(',')
        t_sim_06.append(float(line[0]))
        V_sim_06.append(float(line[1]))

with open('5g_Voltage_Sweep.csv', 'r') as textfile4:
    header = next(textfile4)
    for line in textfile4:
        line = line.split(',')
        t_sim_08.append(float(line[0]))
        V_sim_08.append(float(line[1]))

with open('6g_Voltage_Sweep.csv', 'r') as textfile5:
    header = next(textfile5)
    for line in textfile5:
        line = line.split(',')
        t_sim_10.append(float(line[0]))
        V_sim_10.append(float(line[1]))

t_sim_02 = np.asarray(t_sim_02)
V_sim_02 = np.asarray(V_sim_02)
t_sim_04 = np.asarray(t_sim_04)
V_sim_04 = np.asarray(V_sim_04)
t_sim_06 = np.asarray(t_sim_06)
V_sim_06 = np.asarray(V_sim_06)
t_sim_08 = np.asarray(t_sim_08)
V_sim_08 = np.asarray(V_sim_08)
t_sim_10 = np.asarray(t_sim_10)
V_sim_10 = np.asarray(V_sim_10)

t_settle = 0.5
delta_t_meas = 1

dt_sim_02 = t_sim_02[1]-t_sim_02[0]
dt_sim_04 = t_sim_04[1]-t_sim_04[0]
dt_sim_06 = t_sim_06[1]-t_sim_06[0]
dt_sim_08 = t_sim_08[1]-t_sim_08[0]
dt_sim_10 = t_sim_10[1]-t_sim_10[0]

print(len(t_sim_02))
R_load_2g = 215.6
R_load_3g = 236.7
R_load_4g = 254.2
R_load_5g = 271.8
R_load_6g = 282.3

V_rms_02 = []
V_rms_04 = []
V_rms_06 = []
V_rms_08 = []
V_rms_10 = []

print(t_change_freq)
for t_start in t_change_freq:
    n_start = np.argmin(abs(t_sim_02 - (t_start + t_settle)))
    n_stop = np.argmin(abs(t_sim_02 - (t_start + t_settle + delta_t_meas)))
    print('Start: ', n_start,' Stop: ', n_stop)
    print('Start: ', t_sim_02[n_start],' Stop: ', t_sim_02[n_stop])
    V_rms_02.append(np.sqrt(np.mean(V_sim_02[n_start:n_stop]**2)))
    V_rms_04.append(np.sqrt(np.mean(V_sim_04[n_start:n_stop]**2)))
    V_rms_06.append(np.sqrt(np.mean(V_sim_06[n_start:n_stop]**2)))
    V_rms_08.append(np.sqrt(np.mean(V_sim_08[n_start:n_stop]**2)))
    V_rms_10.append(np.sqrt(np.mean(V_sim_10[n_start:n_stop]**2)))

V_rms_02 = np.asarray(V_rms_02)
V_rms_04 = np.asarray(V_rms_04)
V_rms_06 = np.asarray(V_rms_06)
V_rms_08 = np.asarray(V_rms_08)
V_rms_10 = np.asarray(V_rms_10)

print(V_rms_02)

loss_factor = 0.5

P_02 = loss_factor*(0.5*V_rms_02)**2/R_load_2g*1000
P_04 = loss_factor*(0.5*V_rms_04)**2/R_load_3g*1000
P_06 = loss_factor*(0.5*V_rms_06)**2/R_load_4g*1000
P_08 = loss_factor*(0.5*V_rms_08)**2/R_load_5g*1000
P_10 = loss_factor*(0.5*V_rms_10)**2/R_load_6g*1000

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(freq, P_02, '-', label='Magnet Mass = ' + str(2).format('%f0.2') + 'g', linewidth=1)
ax1.plot(freq, P_04, '-', label='Magnet Mass = ' + str(3).format('%f0.2') + 'g', linewidth=1)
ax1.plot(freq, P_06, '-', label='Magnet Mass = ' + str(4).format('%f0.2') + 'g', linewidth=1)
ax1.plot(freq, P_08, '-', label='Magnet Mass = ' + str(5).format('%f0.2') + 'g', linewidth=1)
ax1.plot(freq, P_10, '-', label='Magnet Mass = ' + str(6).format('%f0.2') + 'g', linewidth=1)

fig1.suptitle('Power as a function of Magnet Mass and Frequency at 12 G_Rms', fontsize=14)
plt.xlabel('Frequency [Hz]', fontsize=10)
plt.ylabel('Power [mW]', fontsize=10)
ax1.grid(b=True, which='major', linestyle='solid')
ax1.grid(b=True, which='minor', linestyle='solid', linewidth=0.5)
ax1.minorticks_on()
plt.legend()
plt.show()

"""
ff = 60
w_ff = 2*math.pi*ff
y=0.001

t=np.linspace(0,2,5000)
v=np.zeros(5000)

for i in range( 0, len(t)):
    v[i]=w_ff*y*math.cos(w_ff*t[i])

with open('sine_60Hz.csv','w') as textfile:
    for i in range(len(t)):
        textfile.write(str(t[i])+','+str(v[i])+'\n')




plt.plot(t,v)
plt.show()"""
