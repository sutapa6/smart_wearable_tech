# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from format_csv import csv_format

plt.rcParams['figure.figsize'] = [20, 10]
plt.rcParams.update({'font.size': 18})

# give path to data
scope_num = 10
lab_num = 2
data = f'data/Lab_{lab_num}/scope_{scope_num}.csv'

''' There are two ways we can define the plotting functions
    1) def plot(filename)
    2) def plot (lab_num, scope_num)

'''


def line_plot(data):
    '''
        Takes a csv file and plots a line graph based off the data given. It then 
        saves this file under data/Plots/Lab_{lab_num}/scope_{scope_num}.png

        Arguments:
            filename (str)    - name of the csv file to be plotted

        Exceptions:
            InputError  - Occurs when   1) filename is not a string
                                        2) filename does not exist
                                        3) filename is not a csv file

        Return Value:
            None 
    '''
    df = pd.read_csv(data, delimiter=',', skiprows=0)
    csv_format(data)
    dt = 1
    t = df['x_axis']
    f = df['channel_2']
    # Plot a line graph from the data
    plt.plot(t, f, LineWidth=1, label="scope_0 raw")
    plt.xlabel('Time (s)')
    plt.ylabel('Volatage (V)')
    plt.legend()

    # save raw scope as png in data/plots
    image_path = f'data/Plots/Lab_{lab_num}/Line_plots/scope_{scope_num}.png'
    plt.savefig(image_path, dpi=300, bbox_inches='tight', transparent=False)

    plt.show()

    pass


def fft_plot(data):
    '''
        Takes a csv file and plots a the FFT of the data given. 

        Arguments:
            filename (str)    - name of the csv file toe be plotted

        Exceptions:
            InputError  - Occurs when   1) filename is not a string
                                        2) filename does not exist
                                        3) filename is not a csv file

        Return Value:
            None 
    '''
    df = pd.read_csv(data, delimiter=',', skiprows=0)
    csv_format(data)
    dt = 1
    t = df['x_axis']
    f = df['channel_2']

    n = len(t)
    fhat = np.fft.fft(f, n)
    PSD = fhat * np.conj(fhat)/n
    freq = (1/(dt*n)) * np.arange(n)
    L = np.arange(1, np.floor(n/2), dtype='int')

    fig, axs = plt.subplots(2, 1)

    plt.sca(axs[0])
    plt.plot(t, f, color='b', LineWidth=2, label="Clean")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Volts(V)")
    plt.legend()

    plt.sca(axs[1])
    plt.plot(freq[L], PSD[L], color='c', LineWidth=2, label="Noisy")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Volts(V)")
    plt.legend()

    plt.show()

    pass


def fft_comparison_plot(data):
    '''
        Takes a csv file and plots a line graph, the FFT and the resulting inverse FFT
        of the data given. It then saves this file under data/Plots/FFT_comparison_plots/Lab_{lab_num}/scope_{scope_num}.png

        Arguments:
            filename (str)    - name of the csv file to be plotted

        Exceptions:
            InputError  - Occurs when   1) filename is not a string
                                        2) filename does not exist
                                        3) filename is not a csv file

        Return Value:
            None 
    '''
    df = pd.read_csv(data, delimiter=',', skiprows=0)
    csv_format(data)
    dt = 1
    t = df['x_axis']
    f = df['channel_2']

    n = len(t)
    fhat = np.fft.fft(f, n)
    PSD = fhat * np.conj(fhat)/n
    freq = (1/(dt*n)) * np.arange(n)
    L = np.arange(1, np.floor(n/2), dtype='int')

    indices = PSD > 0.00005
    PSDclean = PSD * indices
    fhat = indices * fhat
    ffilt = np.fft.ifft(fhat)

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

    # save raw scope as png in data/plots
    image_path = f'data/Plots/Lab_{lab_num}/FFT_comparison_plots/scope_{scope_num}.png'
    plt.savefig(image_path, dpi=300, bbox_inches='tight', transparent=False)

    plt.show()

    pass


if __name__ == "__main__":
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams.update({'font.size': 18})

    scope_num = 10
    lab_num = 2
    data = f'data/Lab_{lab_num}/scope_{scope_num}.csv'

    csv_format(data)
    df = pd.read_csv(data, delimiter=',', skiprows=0)
    dt = 1
    t = df['x_axis']
    f = df['channel_2']

    line_plot(data)
    fft_plot(data)
    fft_comparison_plot(data)
