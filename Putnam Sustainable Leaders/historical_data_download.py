# yfinance - This is used to download historical data directly from Yahoo Finance.
# 'yfinance' makes it easy to access financial market data
# pip install yfinance - To install yfinance

import yfinance as yf

# Step 1: Download historical stock data for a specific ticker from Yahoo Finance over a given data range.
# The data includes Open, High, Low, Close prices and trading volumes.
ticker = 'PLDR'
stock_data = yf.download(ticker, start="2013-01-01", end="2023-01-01")


# Defining file name for CSV
file_name = f"{ticker}_stock_data.csv"

# Save data to CSV
stock_data.to_csv(file_name)

print(f"Stock data for {ticker} has been saved to {file_name}.")