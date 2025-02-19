# Machine-Learning-Based-Stock-Prediction-Through-Candlestick-Pattern
Predicting stock using machine learning model

<h2>Overview</h2>

This project focuses on predicting stock trends using machine learning models based on candlestick patterns. The stocks analyzed include:

<ul>
    <li>Amazon (AMZN)</li>
    <li>Apple (AAPL)</li>
    <li>Netflix (NFLX)</li>
    <li>Putnam Sustainable Leaders (PSL)</li>
    <li>Sony (SONY)</li>
    <li>Tesla (TSLA)</li>
    <li>Wearable Devices (WLDS)</li>
</ul>

<h2>Data Collection</h2>

Historical stock data is downloaded from Yahoo Finance (yfinance) for the past 10 years. The dataset includes daily stock prices and additional technical indicators for feature engineering.

<h2>Feature Engineering</h2>

The following technical indicators were extracted from the historical stock data:

<ul>
    <li>Moving Average (MA)</li>
    <li>Exponential Moving Average (EMA)</li>
    <li>Moving Average Convergence Divergence (MACD)</li>
    <li>Relative Strength Index (RSI)</li>
    <li>Standard Deviation (STD)</li>
    <li>Simple Moving Average (SMA)</li>
    <li>Bollinger Bands (Lower & Upper)</li>
</ul>

<h2>Machine Learning Models Used</h2>

Multiple models were trained to predict stock movements:

<ul>
    <li>K-Nearest Neighbors (KNN)</li>
    <li>Random Forest Classifier</li>
    <li>Support Vector Machine (SVM)</li>
    <li>XGBoost (Extreme Gradient Boosting)</li>
</ul>

<h2>Project Workflow</h2>

<b>Data Preprocessing:</b> Download stock data, handle missing values, normalize features.

<b>Feature Engineering:</b> Extract technical indicators for better model performance.

<b>Model Training & Evaluation:</b> Train models and evaluate using accuracy, precision, recall, and F1-score.

<b>Prediction & Visualization:</b> Predict future stock movements and visualize trends.

<h2>Dependencies</h2>

Ensure you have the following libraries installed:

pip install yfinance pandas numpy scikit-learn xgboost matplotlib seaborn

<h2>Results</h2>

The models were evaluated using accuracy metrics, and results indicate that XGBoost and Random Forest performed best for predicting stock movements based on candlestick patterns.
