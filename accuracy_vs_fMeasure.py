import pandas as pd

# Data for Accuracy Score and F-Measure
data = {
    "Ticker": ["AAPL", "AMZN", "TSLA", "SONY", "WLDS", "NFLX", "PLDR"],
    "SVM_Acc": [0.77, 0.84, 0.71, 0.76, 0.77, 0.82, 0.81],
    "KNN_Acc": [0.89, 0.79, 0.83, 0.87, 0.79, 0.81, 0.76],
    "RF_Acc": [0.91, 0.86, 0.84, 0.86, 0.77, 0.79, 0.84],
    "XGBoost_Acc": [0.80, 0.78, 0.73, 0.77, 0.79, 0.83, 0.75],
    "SVM_F": [0.77, 0.78, 0.88, 0.89, 0.75, 0.77, 0.74],
    "KNN_F": [0.88, 0.87, 0.83, 0.86, 0.88, 0.76, 0.74],
    "RF_F": [0.90, 0.87, 0.82, 0.74, 0.75, 0.83, 0.92],
    "XGBoost_F": [0.75, 0.78, 0.78, 0.85, 0.81, 0.89, 0.79]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the table
print("Accuracy Score and F-Measure table for different Tickers\n")
print(df)

# Optional: Save as an image
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
plt.title("Accuracy Score and F-Measure for Different Tickers")
plt.savefig("table_image.png", dpi=300)  # Save the table as an image
plt.show()
