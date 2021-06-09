# Smart Wearable Tech Software

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

## 2.Overview

- blah blah can do later, copy from Project Plan

## 3. Data Acquisiton

- blah blah can do later, copy from Project Plan

### 3.1 Matplotlib Library in Python

- Matplotlib is a useful library for plotting graphs.
- To graph something in Python using Matplotlib, there are two lines of code we need:
- First,

  ```python
    matplotlib.pyplot.plot(<x axis data>, <y axis data>)
  ```

- Secondly,

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

### 3.2 Visualising Data Acquired from CSV files

- There exists a file `scatter.py` in **src** which will take a CSV file and output a plot of the data. \

  ```python
      filename = 'scope_0.csv' # CSV file to be plotted
  ```

  This will also save a high-quality png into the same directory as the 'scatter.py' file. This plot is generated \
  from the matplotlib library and looks like the plot below

![](scope_0.png)

## 4. Data Cleaning

blah blah can do later, copy from Project Plan

## 5. Data Analysis

blah blah can do later, copy from Project Plan
