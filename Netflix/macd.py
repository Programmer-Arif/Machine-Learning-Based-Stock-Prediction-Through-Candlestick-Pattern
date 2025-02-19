# Step 2: Calculate Technical Indicators 
# These are mathematical calculation based on historical price,volume, or open interest data that are used 
# to predict future price movement.


# i) --------------------------  MACD  --------------------------

# pandas - A powerful library for data manipulation and analysis.
# In this case it helps to load, manipulate, and organize stock data in a dataframe.
import pandas as pd

df = pd.read_csv('NFLX_stock_data.csv')

# MACD Calculation
ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
macd_line = ema_12 - ema_26
signal_line = macd_line.ewm(span=9, adjust=False).mean()
macd_hist = macd_line - signal_line

# Add the technical indicator to the dataframe
df['MACD'] = macd_line
df['Signal'] = signal_line
df['Histogram'] = macd_hist

print(df[['MACD', 'Signal', 'Histogram']])

del df['Signal']
del df['Histogram']

df.to_csv('NFLX_analyzed_file.csv', index=False)