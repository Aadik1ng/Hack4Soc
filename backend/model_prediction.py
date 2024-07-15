import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = yf.download('TATAMOTORS.NS', start='2023-01-01', end='2024-01-31')

# Example: Calculate the moving average
data['MA50'] = data['Close'].rolling(50).mean()
data = data.dropna()

# Example: Calculate the RSI
delta = data['Close'].diff()
delta = delta[1:]
up = delta.copy()
down = delta.copy()
up[up<0] = 0
down[down>0] = 0
data['up'] = up
data['down'] = down
avg_gain = data['up'].rolling(window=14).mean()
avg_gain = avg_gain.dropna()
avg_loss = abs(data['down'].rolling(window=14).mean())
avg_loss = avg_loss.dropna()
rs = avg_gain/avg_loss
rsi = 100.0 - (100.0/(1.0+rs))
data['RSI'] = rsi


# Example: Calculate the MACD
exp1 = data['Close'].ewm(span=12, adjust=False).mean()
exp2 = data['Close'].ewm(span=26, adjust=False).mean()
macd = exp1-exp2
exp3 = macd.ewm(span=9, adjust=False).mean()
data['MACD'] = macd
data['Signal Line'] = exp3
data = data.dropna()

# Example: Calculate the Bollinger Bands
data['20 Day MA'] = data['Close'].rolling(window=20).mean()
data['20 Day STD'] = data['Close'].rolling(window=20).std()
data['Upper Band'] = data['20 Day MA'] + (data['20 Day STD'] * 2)
data['Lower Band'] = data['20 Day MA'] - (data['20 Day STD'] * 2)
data = data.dropna()


X = data[['MA50', 'RSI', 'MACD', 'Upper Band', 'Lower Band']]

y = data['Close']


model = LinearRegression()
model.fit(X, y)

# Make sure to not include the 'Close' column as it is what we're trying to predict
last_7_days_features = data[['MA50', 'RSI', 'MACD', 'Upper Band', 'Lower Band']][-30:]

predicted_prices_last_7_days = model.predict(last_7_days_features)

actual_prices_last_7_days = data['Close'][-30:]

# Print out the comparison
for actual, predicted in zip(actual_prices_last_7_days, predicted_prices_last_7_days):
    print(f"Actual: {actual}, Predicted: {predicted}")


mse = mean_squared_error(actual_prices_last_7_days, predicted_prices_last_7_days)
print(f"Mean Squared Error for the last 7 days: {mse}")

# Plotting the actual vs predicted prices for the last 7 days
plt.figure(figsize=(10, 5))
plt.plot(actual_prices_last_7_days.index, actual_prices_last_7_days, label='Actual Price')
plt.plot(actual_prices_last_7_days.index, predicted_prices_last_7_days, label='Predicted Price', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Actual vs Predicted Price for the Last 30 Days')
plt.legend()
plt.show()