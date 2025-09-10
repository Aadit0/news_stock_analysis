import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

stocks = ['AAPL','NVDA','AMD']

end_date = datetime.today() - timedelta (days = 3650) # last 10 years
start_date = end_date - timedelta (days = 365)
print(end_date,start_date)

Cprice = pd.DataFrame() #create an empty data frame to store prices
Returns = pd.DataFrame() # create an empty data frame to store the returns

for stock in stocks:
    data = yf.download(stock,start=start_date,end=end_date)
    Cprice[stock] = data['Close']

Returns = Cprice.pct_change()

def up_down(x):
    if x > 0:
        return 1
    else:
        return 0
    
movement = Returns.applymap(up_down)

print(Cprice,Returns,movement)

# Save all outputs into data folder
Cprice.to_csv("data/closing_prices.csv")
Returns.to_csv("data/daily_Returns.csv")
movement.to_csv("data/movement_labels.csv")

