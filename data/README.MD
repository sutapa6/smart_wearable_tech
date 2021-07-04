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

<table>
  <tr>
    <th>Name & Description</th>
    <th>Data Types</th>
    <th>Exceptions</th>
  </tr>
  <tr>
    <td><code>csv_format</code><br /><br />Given a CSV filename, format the CSV in a way Matplotlib can plot.</td>
    <td><b>Parameters:</b><br /><code>filename</code><br /><br /><b>Return Type:</b><br /><code>None<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Filename entered is not a valid file</li>
      </ul>
    </td> 
  </tr>
  <tr>
     <td><code>line_plot</code><br /><br />Takes a csv file and plots a line graph based off the data given. It then 
    saves this file under data/Plots/Lab_{lab_num}/scope_{scope_num}.png</td>
    <td><b>Parameters:</b><br /><code>filename</code><br /><br /><b>Return Type:</b><br /><code>None<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Filename entered is not a valid file</li>
      </ul>
    </td> 
  </tr>
  <tr>
     <td><code>fft_plot</code><br /><br />Takes a csv file and plots a the FFT of the data given. </td>
    <td><b>Parameters:</b><br /><code>filename</code><br /><br /><b>Return Type:</b><br /><code>None<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Filename entered is not a valid file</li>
      </ul>
    </td> 
  </tr>
  <tr>
     <td><code>fft_comparison_plot</code><br /><br />Takes a csv file and plots a line graph, the FFT and the resulting inverse FFT.of the data given. It then saves this file under data/Plots/FFT_comparison_plots/Lab_{lab_num}/scope_{scope_num}.png. </td>
    <td><b>Parameters:</b><br /><code>filename</code><br /><br /><b>Return Type:</b><br /><code>None<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Filename entered is not a valid file</li>
      </ul>
    </td> 
  </tr>
    <tr>
     <td><code>write_wav</code><br /><br />Takes a csv file and creates a .wav file. It then saves this file under data/Audio/Lab_{lab_num}/scope_{scope_num}.wav. </td>
    <td><b>Parameters:</b><br />(<code>data</code><br />
    <code>filename</code><br /> <code>framerate</code><br /><code>amplitude</code>)<br /> <b>Return Type:</b><br /><code>None<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Filename entered is not a valid file</li>
      </ul>
    </td> 
  </tr>
  </tr>
    <tr>
     <td><code>band_pass_filter</code><br /><br />Takes a signal and applies a bandpass filter to it. Returns a filtered signal. </td>
    <td><b>Parameters:</b><br />(<code>signal</code>)<br /> <b>Return Type:</b><br /><code>any<code></td>
    <td>
      <b>InputError</b> when any of:
      <ul>
        <li>Signal entered is not a valid file</li>
      </ul>
    </td> 
  </tr>

  <tr>
  </table>


