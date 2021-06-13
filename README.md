# Smart Wearable Tech Software

**🐍 Chunder's Crew 🐍**

## Contents

1. Aims
2. Overview
3. Data Acquisiton
4. Data Cleaning
5. Data Analysis
6. Database

## 0. Change Log

- 09/06 Added General overview of the project

## 1. Aims:

- Using the Data acquired from the labs, analyse the data and output a matching output to a spoken input

## 2. Overview

- blah blah can do later, copy from Project Plan

## 3. Data Acquisiton

### 3.1 Matplotlib Library in Python

- Matplotlib is a useful library for plotting graphs.
- To graph something in Python using Matplotlib, there are two lines of code we need:
- The first line is,

  ```python
    matplotlib.pyplot.plot(<x axis data>, <y axis data>)
  ```

- The second line is,

  ```python
    matplotlib.pyplot.show()
  ```

- Since it can be annoying to type out 'matplotlib.pyplot' every time we want to call something from the library we can simply state at the top:

  ```python
    from matplotlib import pyplot as plt
  ```

- This means that we can simply write 'plt' wherever we had 'matplotlib.pyplot'

  ```python
      plt.plot(<x axis data>, <y axis data>)
      plt.show()
  ```

- Now if we run the code using our normal command 'python3 <filename>.py', we should have a new window pop up with the graph.

  - Keep in mind the default graph type for matplotlib is a line graph. If we want another type of graph we will have to specify its type as follows:

  ```python
      plt.plot(kind='<graph type>', x='<x axis data>', y='<y axis data>')
  ```

#### 3.1.1 Known issues with Matplotlib and WSL (Windows Subsystem for Linux)

- There appears to be an issue with Matplotlib and WSL. More specifically, it seems to have issues with:

  ```python
      matplotlib.pyplot.show()
  ```

- Our workaround in `scatter.py` is to instead save a PNG of the plot in the same directory as `scatter.py` and open it.

### 3.2 Visualising Data Acquired from CSV files

#### 3.2.1 Formatting the CSV files

- We need to format the CSV files in such a way matplotlib will be able to plot.

##### Original Format of CSV files from oscilloscope

```csv
    x-axis,2,4
    Volt,second,second
    -4.9921875E+00,+36.2374E-03,-0.0E+00
    -4.9914063E+00,+30.2073E-03,-804.0E-06
    -4.9906250E+00,+30.2073E-03,-804.0E-06
    -4.9898438E+00,+34.2274E-03,-1.6080E-03
    -4.9890625E+00,+34.2274E-03,-804.0E-06
    ...
```

##### Modified Format of CSV files from oscilloscope

```csv
    x_axis,channel_2,channel_4
    -4.9921875,0.03624,0.0
    -4.9914063,0.03021,-0.0
    -4.990625,0.03021,-0.0
    -4.9898438,0.03423,-0.002
    -4.9890625,0.03423,-0.0
    ...
```

#### 3.2.1 Plotting the Data from the CSV Files

- There exists a file `scatter.py` in **src** which will take a CSV file and output a plot of the data.

  ```python
      filename = 'scope_0.csv' # CSV file to be plotted
  ```

  This will also save a high-quality png into the same directory as the 'scatter.py' file. This plot is generated \
  from the matplotlib library and looks like the plot below

![](docs/scope_0.png)

A line graph version of the same data can be seen below

![](docs/line_scope_0.png)

## 4. Data Cleaning

blah blah can do later, copy from Project Plan

### 4.1 Fast Fourier Transform (FFT)

- In layman's terms, the Fourier Transform is a mathematical operation that changes the domain (x-axis) of a signal from time to frequency

- Fast Fourier Transforms are a way to clean up our data and reduce the amount of noise present in out plots.

- The maths involved in an FFT is quie complex, and is left as an exercise to the reader

#### 4.1.1 Implementing FFT using Python

- Located in `src` is a file called `fft_example.py`. This file takes any of the csv files obtained from the labs and outputs a plot of the original function, its FFT and an inverse FFT with reduced noise. An example is shown below.

![](docs/fft_sample.png)

- However, it is in fact much easier to use the file `fft.ipynb` located in the `smart_wearable_tech` directory. This is a Jupyter Notebook, allowing for the division of code into small cells which can be individually run and debugged accordingly.

## 5. Data Analysis

blah blah can do later, copy from Project Plan

## 6. Database

### 6.1 Establishing a Word Bank

- At the commencement of this project, the team aimed to deliver a package which would detect and analyse any vocal vibrations, and consequently produce a corresponding text output.

- This scope has since been reduced due to the complex and irregular nature of the English lexicon; rather than documenting every phoneme of the spoken English language, we will focus on a select assortment of words. More specifically, the package will be designed to process the NATO Phonetic Alphabet.

#### 6.1.1 NATO Phonetic Alphabet (NPA)

- The NATO Phonetic Alphabet is the established phonetic alphabet for all military, civilian and amateur radio communications. It contains 26 words, substituting a unique codeword for each letter of the alphabet:

<p allign='center'>
  <em>Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-Ray, Yankee, Zulu. </em>
</p>

- Each codeword in the NPA was chosen to sound distinct from each other, and incorporates sounds common to English, French, and Spanish.

- The testing team will utilise their testing setup to acquire repetitions of sensor data for each of the codewords in the NPA. This data will be handed to the software team for processing, with the accumulation of processed data establishing a unique profile for corresponding codewords.
  - Subsequently, new signals acquired by the sensor will be subjected to a probability match against the codeword profiles to determine exactly which codeword was spoken, and hence produce an appropriate speech output.
