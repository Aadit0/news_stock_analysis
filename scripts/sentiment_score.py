from textblob import TextBlob
import pandas as pd

news = pd.read_csv('data/combinedNews.csv')

def getSentiment(text):
    return TextBlob(text).sentiment.polarity

news['Sentiment'] = news['Combined_News'].apply(getSentiment)
news.to_csv('data/newsSentiment.csv')
print(news.head())