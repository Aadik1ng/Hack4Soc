import yfinance as yf

# Fetch historical data for a stock (example: 'TATAMOTORS.NS' for Tata Motors on NSE)
data = yf.download('TATAMOTORS.NS', start='2023-01-01', end='2024-01-31')
print(data.tail())