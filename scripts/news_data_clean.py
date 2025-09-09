import pandas as pd

news = pd.read_csv("data/Combined_News_DJIA.csv")

# Select only the 25 news columns
selected_columns = news.iloc[:, 2:27].astype(str)

# Combine each row into a single string
combined_news = selected_columns.apply(lambda row: ' '.join(row), axis=1)

# Create a new DataFrame with only the combined column
news_combined = pd.DataFrame({"Combined_News": combined_news})

# Save to CSV
news_combined.to_csv('data/combinedNews.csv', index=False)
