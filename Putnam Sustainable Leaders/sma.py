# Step 2: Calculate Technical Indicators 
# v) --------------------------  SMA  --------------------------

import pandas as pd

df = pd.read_csv('PLDR_analyzed_file.csv')

# SMA Calculation
sma_period = 20
sma = df['Close'].rolling(window=sma_period).mean()


# Add the technical indicator to the dataframe
df['SMA'] = sma

print(df[['SMA']])

df.to_csv('PLDR_analyzed_file.csv', index=False)