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
    f = f.rename(columns=({'x-axis': 'x_axis'}))
    f = f.rename(columns=({'2': 'channel_2'}))
    f = f.drop([0], axis=0)

    # Removes rows containing empty values
    i = 1
    while f["channel_2"][i] != f["channel_2"][i]:
        f = f.drop([i], axis=0)
        i += 1

    keep_col = ['x_axis', 'channel_2']
    new_f = f[keep_col]

    # Overwriting existing csv file with formatted csv
    new_f.to_csv(filename, index=False)

    pass
