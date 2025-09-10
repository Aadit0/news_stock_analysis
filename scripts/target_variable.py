import pandas as pd

def up_down(x):
    if x > 0:
        return 1
    else:
        return 0
    
combinedData = pd.read_csv('data/combinedData.csv')
combinedData = combinedData.drop(columns=['Unnamed: 0']) # Drop unnamed column

combinedData["AAPL_return"] = combinedData["AAPL"].pct_change()
combinedData["NVDA_return"] = combinedData["NVDA"].pct_change()
combinedData["AMD_return"] = combinedData["AMD"].pct_change()

combinedData["AAPL_movement"] = combinedData["AAPL_return"].apply(up_down)
combinedData["NVDA_movement"] = combinedData["NVDA_return"].apply(up_down)
combinedData["AMD_movement"] = combinedData["AMD_return"].apply(up_down)

print(combinedData[["Date", "Sentiment", "AAPL", "AAPL_return", "AAPL_movement"]].head(10))

combinedData.to_csv('data/finalData.csv', index=False) 