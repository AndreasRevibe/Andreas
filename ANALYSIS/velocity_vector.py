import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("C:/Users/andre/Documents/GitHub/Andreas/Library")

from my_func import from_acc_to_vel
path = "G:/Min enhet/ReVibe Energy/R&D/Vibration data library/Applications/Blower/STIHL/local_meassurement/position_2/data/2_full_y_01.txt"

acc = []
time = []
with open(path,"r") as textfile:
    next(textfile)
    for line in textfile:
        #print(line)
        line=line.split(",")
        #acc = [float(el) for el in line]
        acc.append(float(line[1]))
        time.append(float(line[0]))

acc = np.asarray(acc)
time = np.asarray(time)
dt = (time[-1]-time[0])/len(time)
acc=10*acc*9.81

#dt=180/len(acc)
fs=1/dt
vel=from_acc_to_vel(acc,fs)
# vel=resample(vel,10,1)
t_tot = dt*len(acc)
t = np.linspace(0,1, len(acc))*t_tot

with open('C:/Users/andre/Documents/GitHub/code/ANALYSIS/Stihl_Pos2_y.csv','w') as textfile:
    for i in range(len(t)-1):
        textfile.write(str(t[i])+'\t'+str(vel[i])+'\n')


fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(211)
ax.plot(t[1:],vel)
ax_acc=fig.add_subplot(212)
ax_acc.plot(t,acc)
plt.show()
