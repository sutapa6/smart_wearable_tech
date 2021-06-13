'''
    This is a completely working implementation of the FFT.
    To adjust the threshold value for the inverse FFT, adjust 
    the indices value (line 50).

'''
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.new_scatter import csv_format

plt.rcParams['figure.figsize'] = [20, 10]
plt.rcParams.update({'font.size': 18})

# give path to data
scope_num = 0
data = f'data/Lab_2/scope_{scope_num}.csv'

csv_format(data)
df = pd.read_csv(data, delimiter=',', skiprows=0)

# initialise data for anaysis
dt = 1
t = df['x_axis']
f = df['channel_2']  

plt.plot(t, f, LineWidth=1, label="scope_0 raw")
plt.xlabel('Time (s)')
plt.ylabel('Volatage (V)')
plt.legend()

# save raw scope as png in data/plots
image_path = f'data/Plots/Lab_2/scope_{scope_num}.png'
plt.savefig(image_path, dpi=300, bbox_inches='tight', transparent=False)


# %%
# Compute the Fast Fourier Transform (FFT)

n = len(t)
fhat = np.fft.fft(f, n)
PSD = fhat * np.conj(fhat)/n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype='int')

fig, axs = plt.subplots(2, 1)

plt.sca(axs[0])
plt.plot(t, f, color='k', LineWidth=2, label="scope_0 raw")
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="scope_0 fft")
plt.xlabel("Frequency (Hz)")
plt.legend()


# %%
indices = PSD > 0.02
PSDclean = PSD * indices
fhat = indices * fhat
ffilt = np.fft.ifft(fhat)


# %%
fig, axs = plt.subplots(3, 1)

plt.sca(axs[0])
plt.plot(t, f, color='c', LineWidth=1.5, label="Noisy")
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='k', LineWidth=2, label="Filtered")
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="Noisy")
plt.plot(freq[L], PSDclean[L], color='k', LineWidth=1.5, label="Filtered")
plt.legend()

plt.show()


# %%
