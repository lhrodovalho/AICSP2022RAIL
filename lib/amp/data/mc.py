import numpy as np
import matplotlib.pyplot as plt

def f0(filename):
	data = np.genfromtxt(filename, delimiter=",",skip_header=2)
	av_mean  = np.mean(data[:,1])
	av_std   = np.std(data[:,1])
	gbw_mean = np.mean(data[:,2])
	gbw_std  = np.std(data[:,2])
	pm_mean  = np.mean(data[:,3])
	pm_std   = np.std(data[:,3])
	vos_mean = np.mean(data[:,4])
	vos_std  = np.std(data[:,4])

	print()
	print(filename)
	print("av: ",f"{av_mean:.2E}",f"{av_std:.2E}")
	print("gbw: ",f"{gbw_mean:.2E}",f"{gbw_std:.2E}")
	print("pm: ",f"{pm_mean:.2E}",f"{pm_std:.2E}")
	print("vos:",f"{vos_mean:.2E}",f"{vos_std:.2E}")


f0("ampa_ac_df_mc_mis.csv")
f0("ampb_ac_df_mc_mis.csv")
f0("ampc_ac_df_mc_mis.csv")

data = np.genfromtxt("ampa_ac_df_mc_mis.csv", delimiter=",", skip_header=2)
a = data[:,4]
_ = plt.hist(a, bins='auto')
print(a)
print(np.std(a))
plt.show()
