import pandas as pd

def csv_format(lab_num: int, scope_num: int):
    '''
    Format oscilloscope files for easier manipulation and plotting
    Inputs:
        lab_num (int)       Lab number of the scope to be formatted
        scope_num (int)     scope number of the file to be formatted
    Outputs:
        csv file, formatted inplace
    '''

    # Load csv file
    df = pd.read_csv(f'data/Lab_{lab_num}/Raw/scope_{scope_num}.csv')

    # Rename columns
    cols = list(df.columns)
    for header in cols:
        if 'axis' in header:
            df.rename({header: 'time'}, axis=1, inplace=True)
        elif 'channel' not in header:
            df.rename({header: 'channel_' + header}, axis=1, inplace=True)

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
    t0 = df['time'][0]
    if t0 < 0:
        df['time'] = df['time'].astype(float) - t0


    # Save modified csv to a new file, display first 10 rows
    df.to_csv(f'data/Lab_{lab_num}/modified_scope_{scope_num}.csv', index=False)