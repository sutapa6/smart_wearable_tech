# Data 📊

This section describes how the team has organised our data and where to retrieve specific files and plots. blah blah blah

## Future Improvements

- Instead of having data sorted by Labs, it will be better to sort by words. E.g. 'Alpha', 'Bravo' etc.
- Naming convention for files should be changed to include:

  1. The word it represents
  2. The date the data was collected
  3. Who the test subject was ? Maybe include a naming convention such as initials. (AM = Akira, AK=Andrew, etc)

  - Maybe something like `apple_07/25_AM.csv` ? Discuss on Sunday 07/04

## Audio 🔈

- This directory contains the .wav files generated from csv data acquired during Labs.

## Lab\_# ⚡

- This directory contains call data obtained and processed from the corresponding lab. It is divided into two sections, `Raw` and `Filtered`

  ### Raw

  - Raw data obtained from lab sessions in the form of a CSV file.

  ### Filtered

  - Filtered version of the raw csv files. Divided into two sections, `Bandpass` and `FFT`.

    #### Bandpass

    - Filtered data using the method of applying a Bandpass filter.
    - Source file: `bandpass.ipynb`

    #### FFT

    - Filtered data using the method of applying an FFT.
    - Source file: `fft.ipynb`

## Plots 📈

- This is where all the plots generated are stored.
- They are divided into Lab numbers and then into categories. The four categories currently in place are:

  1. `Bandpass_filtered_plots`
  2. `FFT_comparison_plots`
  3. `Line_plots`
  4. `Spectrograms`

  ### Bandpass_filtered_plots

  - Plot generated of data after a bandpass filter has been applied.
  - Source file: `bandpass.ipynb`

  ### FFT_comparison_plots

  - Plot generated of data after an FFT has been applied.
  - Source file: `fft.ipynb`

  ### Line_plots

  - Plot generated of raw data obtained from labs.
  - Source file: `fft.ipynb`

  ### Spectrograms

  - Spectrogram generated of raw data obtained from labs.
  - Source file: `spectrogram.ipynb`



