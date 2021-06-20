import pandas as pd


def csv_format(filename: str):
    '''
        Takes a csv file and formats it in such a way that can be 
        plotted using the matplotlib library. Essentially, this is changing 
        each header to not include hyphens (such as x-axis) or plain integers
        It also deletes any rows with empty values 

        Arguments:
            filename (str)    - name of the csv file to be plotted

        Exceptions:
            InputError  - Occurs when   1) filename is not a string
                                        2) filename does not exist
                                        3) filename is not a csv file

        Return Value:
            None 
    '''
    f = pd.read_csv(filename)
    keep_col = ['x_axis', 'channel_2']
    new_f = f[keep_col]
    new_f.to_csv(filename, index=False)
    '''
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
    '''
    pass
