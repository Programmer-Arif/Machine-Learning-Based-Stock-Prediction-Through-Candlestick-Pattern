# Step 2: Calculate Technical Indicators 
# iii) --------------------------  EMA  --------------------------

import pandas as pd

df = pd.read_csv('PLDR_analyzed_file.csv')

# EMA Calculation
ema_period = 20
ema = df['Close'].ewm(span=ema_period, adjust=False).mean()


# Add the technical indicator to the dataframe
df['EMA'] = ema

print(df[['EMA']])

df.to_csv('PLDR_analyzed_file.csv', index=False)