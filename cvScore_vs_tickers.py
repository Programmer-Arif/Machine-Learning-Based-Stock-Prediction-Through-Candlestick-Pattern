import matplotlib.pyplot as plt

# Define data
tickers = ['AAPL', 'AMZN', 'TSLA', 'SONY', 'WLDS', 'NFLX', 'PLDR']
knn_scores = [0.89, 0.79, 0.83, 0.87, 0.79, 0.81, 0.76]
svm_scores = [0.77, 0.84, 0.71, 0.76, 0.77, 0.82, 0.81]
rf_scores = [0.91, 0.86, 0.84, 0.86, 0.77, 0.79, 0.84]
xgb_scores = [0.80, 0.78, 0.73, 0.77, 0.79, 0.83, 0.75]

# Set the bar width
bar_width = 0.2

# Set the positions of the bars on the x-axis
r1 = range(len(tickers))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Create the bar graph
plt.bar(r1, knn_scores, width=bar_width, label='KNN')
plt.bar(r2, svm_scores, width=bar_width, label='SVM')
plt.bar(r3, rf_scores, width=bar_width, label='Random Forest')
plt.bar(r4, xgb_scores, width=bar_width, label='XGBoost')

# Set the x-axis tick labels
plt.xticks([r + 1.5 * bar_width for r in range(len(tickers))], tickers)

# Set the labels and title
plt.xlabel('Tickers')
plt.ylabel('Cross-validation Score')
plt.title('Comparison of Cross-validation Scores for Different Classifiers')

# Display the legend
plt.legend()

# Show the plot
plt.show()
