from scipy.integrate import cumtrapz
def from_acc_to_vel(acc,fs):
    return cumtrapz(acc)*1/fs
    
