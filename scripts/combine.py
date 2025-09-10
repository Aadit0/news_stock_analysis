import pandas as pd

prices = pd.read_csv('data/closing_prices.csv')
sentiment = pd.read_csv('data/newsSentiment.csv')

combined = pd.merge(prices, sentiment, on='Date', how='inner')

combined.to_csv('data/combinedData.csv', index=False)
print(combined.head())