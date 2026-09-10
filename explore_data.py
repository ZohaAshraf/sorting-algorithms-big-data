import pandas as pd
import os

# The 4 files we chose in Step 2, based on check_sizes.py output
files = ['2015.csv', '2016.csv', '2017.csv', '2018.csv']
folder = './data'

total_rows = 0
columns = None
chunk_memory_mb = None

for filename in files:
    path = os.path.join(folder, filename)
    print(f'Processing {filename}...')

    for i, chunk in enumerate(pd.read_csv(path, chunksize=1_000_000)):
        total_rows += len(chunk)

        # Grab columns and memory footprint just once, from the very first chunk
        if columns is None:
            columns = list(chunk.columns)
            chunk_memory_mb = chunk.memory_usage(deep=True).sum() / 1e6
            print(f'  Columns ({len(columns)}): {columns}')
            print(f'  Memory footprint of one chunk: {chunk_memory_mb:.2f} MB')

        if i % 5 == 0:
            print(f'  ...chunk {i}, running total rows: {total_rows:,}')

print(f'\nTOTAL ROWS across all 4 files: {total_rows:,}')