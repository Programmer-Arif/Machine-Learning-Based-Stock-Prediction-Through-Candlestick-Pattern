# Step 2: Calculate Technical Indicators 
# vii) --------------------------  Upper Bollinger  --------------------------

import pandas as pd

df = pd.read_csv('AMZN_analyzed_file.csv')

# Upper Bollinger Calculation
ema_period = 20
ema = df['Close'].ewm(span=ema_period, adjust=False).mean()

std_period = 20
std = df['Close'].rolling(window=std_period).mean()

num_std = 2
upper_bollinger = ema + (std * num_std)


# Add the technical indicator to the dataframe
df['Upper'] = upper_bollinger

print(df[['Upper']])

df.to_csv('AMZN_analyzed_file.csv', index=False)