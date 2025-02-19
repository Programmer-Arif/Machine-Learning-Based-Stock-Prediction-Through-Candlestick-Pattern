# Step 2: Calculate Technical Indicators 
# vi) -------------------------  STD  --------------------------

import pandas as pd

df = pd.read_csv('PLDR_analyzed_file.csv')

# STD Calculation
std_period = 20
std = df['Close'].rolling(window=std_period).mean()


# Add the technical indicator to the dataframe
df['STD'] = std

print(df[['STD']])

df.to_csv('PLDR_analyzed_file.csv', index=False)