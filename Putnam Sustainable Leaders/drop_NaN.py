# Step 3: Handle NaN values

import pandas as pd

df = pd.read_csv('PLDR_analyzed_file.csv')

df.dropna(inplace=True)

df.to_csv('PLDR_ready_file.csv', index=False)
