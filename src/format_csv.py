import os
import csv


def csv_format(file_path: str):
    r = csv.reader(open(file_path))
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
    writer = csv.writer(open(file_path, 'w'))
    writer.writerows(lines)

    pass
