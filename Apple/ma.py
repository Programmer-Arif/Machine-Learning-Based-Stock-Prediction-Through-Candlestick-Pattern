# Step 2: Calculate Technical Indicators 
# iV) --------------------------  MA  --------------------------

import pandas as pd

df = pd.read_csv('AAPL_analyzed_file.csv')

# MA Calculation
ma_period = 20
ma = df['Close'].rolling(window=ma_period).mean()



# Add the technical indicator to the dataframe
df['MA'] = ma

print(df[['MA']])

df.to_csv('AAPL_analyzed_file.csv', index=False)