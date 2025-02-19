# Step 2: Calculate Technical Indicators 
# ii) --------------------------  RSI  --------------------------

import pandas as pd

df = pd.read_csv('PLDR_analyzed_file.csv')

# RSI Calculation
window_length = 14
delta = df['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=window_length).mean()
avg_loss = loss.rolling(window=window_length).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))


# Add the technical indicator to the dataframe
df['RSI'] = rsi

print(df[['RSI']])

df.to_csv('PLDR_analyzed_file.csv', index=False)