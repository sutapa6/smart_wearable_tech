import pandas as pd

def csv_format(lab_num: int, scope_num: int, sensor_ch: int):
    '''
    Format oscilloscope files for easier manipulation and plotting
    Inputs:
        lab_num (int)       Lab number of the scope to be formatted
        scope_num (int)     scope number of the file to be formatted
    Outputs:
        save_path (str)     path to the formatted file from the root directory
    '''

    # Load csv file
    df = pd.read_csv(f'data/Lab_{lab_num}/Raw/scope_{scope_num}.csv')

    # Rename columns
    cols = list(df.columns)
    for header in cols:
        if 'axis' in header:
            df.rename({header: 'Time'}, axis=1, inplace=True)
        elif str(sensor_ch) in header:
            df.rename({header: 'Sensor'}, axis=1, inplace=True)
        else:
            df = df.drop(columns=[header])

    # Delete row with units (first row)
    df = df.drop(0)
    
    # Delete completley empty rows, and remove indexes from the csv
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)

    # Convert from scientific to float
    cols = list(df.columns)
    for header in cols:
        df[header].apply(lambda x: '%.7f' % x)

    # Correct any negative timestamps
    t0 = df['Time'][0]
    if t0 < 0:
        df['Time'] = df['Time'].astype(float) - t0


    # Save modified csv to a new file, display first 10 rows
    save_path = f'data/Lab_{lab_num}/Formatted/scope_{scope_num}.csv'
    df.to_csv(save_path, index=False)

    return str(save_path)

if __name__ == '__main__':
    # Specify the data to be formatted
    lab_num = 1
    scope_num = 5
    sensor_ch = 2

    # Call csv_format, display the first 10 rows of the formatted file
    filename = csv_format(lab_num, scope_num, sensor_ch)
    print(filename, type(filename))

    formatted = pd.read_csv(filename)
    formatted.head(10)