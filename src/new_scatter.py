# This updated scatter.py file is to format CSV files from Lab_2, which only
# contain two columns (x axis and channel_2)

import pandas as pd
import matplotlib.pyplot as plt
import csv
from PIL import Image
import os

# The file to be graphed
filename = 'data/Lab_2/scope_4.csv'

# Formats CSV file in a way matplotlib can plot


def csv_format(filename):
    r = csv.reader(open(filename))
    lines = list(r)

    # 1) Convert header to names that matplotlib will like
    lines[0][0] = 'x_axis'
    lines[0][1] = 'channel_2'

    # 2) Remove second row (second, volt, volt)
    del lines[1:3]

    # 3 Change Scientific Notation to decimal
    for row in lines:
        if row[0] == '' and row[1] == '' and row[2] == '':
            del row

        if row[0] != "x_axis":
            row[0] = float(row[0])

        if row[1] != "channel_2" and row[1] != '':
            row[1] = float(row[1])

    # Writes new formatted csv to the file, ready for plotting
    writer = csv.writer(open(filename, 'w'))
    writer.writerows(lines)

    pass


csv_format(filename)
df = pd.read_csv(filename)
df.plot(kind='scatter', x='x_axis', y='channel_2')  # scatter plot
# plt.show() should display the plot, but wsl hates it
# instead, generate the plot as a png and save it in the current directory
image_name = filename.replace(".csv", ".png")
plt.savefig(image_name, dpi=300)

# Open the image of the plot
cwd = os.getcwd()
#image = Image.open(f"{cwd}/{image_name}")
# image.show()
