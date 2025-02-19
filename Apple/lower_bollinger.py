# Step 2: Calculate Technical Indicators 
# viii) --------------------------  Lower Bollinger  --------------------------

import pandas as pd

df = pd.read_csv('AAPL_analyzed_file.csv')

# Lower Bollinger Calculation
ema_period = 20
ema = df['Close'].ewm(span=ema_period, adjust=False).mean()

std_period = 20
std = df['Close'].rolling(window=std_period).mean()

num_std = 2
lower_bollinger = ema - (std * num_std)


# Add the technical indicator to the dataframe
df['Lower'] = lower_bollinger

print(df[['Lower']])

df.to_csv('AAPL_analyzed_file.csv', index=False)