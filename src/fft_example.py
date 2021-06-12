# An example of how a fft works using a sum of sine waves with added noise
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

# Create a simple signal with two frequencies
dt = 0.001
t = np.arange(0, 1, dt)
f = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*16*t)  # Sum of two frequencies
f_clean = f
f = f+2.5*np.random.randn(len(t))  # Add some random noise

plt.plot(t, f, color='c', LineWidth=1.5, label="Noisy")
plt.plot(t, f_clean, color='k', LineWidth=2, label="Clean")
plt.xlim(t[0], t[-1])
plt.legend()
plt.show()


# %%
# Compute the Fast Fourier Transform (FFT)

n = len(t)
fhat = np.fft.fft(f, n)  # Compute the FFT
PSD = fhat * np.conj(fhat)/n  # Power spectrum
freq = (1/(dt*n)) * np.arange(n)  # x axis of frequencies
L = np.arange(1, np.floor(n/2), dtype='int')

fig, axs = plt.subplots(2, 1)

plt.sca(axs[0])
plt.plot(t, f, color='c', LineWidth=1.5, label="Noisy")
plt.plot(t, f_clean, color='k', LineWidth=2, label="Clean")
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="Noisy")
plt.xlim(freq[L[0]], freq[L[-1]])
plt.xlabel("Frequency (Hz)")
plt.legend()

plt.show()


# %%
indices = PSD > 100
PSDclean = PSD * indices
fhat = indices * fhat
ffilt = np.fft.ifft(fhat)


# %%
fig, axs = plt.subplots(3, 1)

plt.sca(axs[0])
plt.plot(t, f, color='c', LineWidth=1.5, label="Noisy")
plt.plot(t, f_clean, color='k', LineWidth=2, label="Clean")
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='k', LineWidth=2, label="Filtered")
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="Noisy")
plt.plot(freq[L], PSDclean[L], color='k', LineWidth=1.5, label="Filtered")
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()


# %%
