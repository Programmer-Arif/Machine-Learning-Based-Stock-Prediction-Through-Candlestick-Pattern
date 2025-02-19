# Step 3: Handle NaN values

import pandas as pd

df = pd.read_csv('AMZN_analyzed_file.csv')

df.dropna(inplace=True)

df.to_csv('AMZN_ready_file.csv', index=False)
