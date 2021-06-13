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

plt.rcParams['figure.figsize'] = [20, 10]
plt.rcParams.update({'font.size': 18})

df = pd.read_csv('data/Lab_2/scope_0.csv', delimiter=',', skiprows=0)

# Create a simple signal with two frequencies
dt = 1
t = df['x_axis']
f = df['channel_2']  # Sum of two frequencies

plt.plot(t, f, LineWidth=1, label="Clean")
plt.legend()


# %%
# Compute the Fast Fourier Transform (FFT)

n = len(t)
fhat = np.fft.fft(f, n)
PSD = fhat * np.conj(fhat)/n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype='int')

fig, axs = plt.subplots(2, 1)

plt.sca(axs[0])
plt.plot(t, f, color='k', LineWidth=2, label="Clean")
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="Noisy")
plt.xlabel("Frequency (Hz)")
plt.legend()


# %%
indices = PSD > 0.0025
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
