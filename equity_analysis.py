import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stocks = ['AAPL', 'MSFT', 'NVDA', 'AMZN']


print("Downloading stock data...")

raw_data = yf.download(
    stocks,
    start='2025-01-01',
    end='2026-01-01'
)


close_prices = raw_data['Close']

print(close_prices.head())


returns = close_prices.pct_change()


volatility = returns.std() * np.sqrt(252)

print("\nAnnualized Volatility:")
print(volatility)


plt.figure(figsize=(12,6))

for stock in stocks:
    plt.plot(close_prices[stock], label=stock)

plt.title("Technology Stock Price Trends")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("charts/stock_price_trends.png")

plt.close()


plt.figure(figsize=(8,5))

plt.bar(volatility.index, volatility.values)

plt.title("Volatility Comparison")
plt.xlabel("Stocks")
plt.ylabel("Volatility")
plt.grid(True)

plt.savefig("charts/volatility_comparison.png")

plt.close()


aapl_prices = close_prices['AAPL']

ma20 = aapl_prices.rolling(20).mean()
ma50 = aapl_prices.rolling(50).mean()



plt.figure(figsize=(12,6))

plt.plot(aapl_prices, label='AAPL Price')
plt.plot(ma20, label='20-Day MA')
plt.plot(ma50, label='50-Day MA')

plt.title("Moving Average Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("charts/moving_average_strategy.png")

plt.close()



correlation = returns.corr()

print("\nCorrelation Matrix:")
print(correlation)


close_prices.to_csv("data/closing_prices.csv")
returns.to_csv("data/daily_returns.csv")


print("\nProject completed successfully!")
print("Charts saved in charts folder.")
print("CSV files saved in data folder.")