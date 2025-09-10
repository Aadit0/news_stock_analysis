import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
final_data = pd.read_csv("data/finalData.csv")

# Features (we’ll just use sentiment for now)
X = final_data[["Sentiment"]]

# Loop through each stock’s movement column
stocks = ["AAPL", "NVDA", "AMD"]

for stock in stocks:
    print(f"\n--- Training model for {stock} ---")
    
    # Target column for this stock
    y = final_data[f"{stock}_movement"]
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=False
    )
    
    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy for {stock}: {acc:.2f}")
