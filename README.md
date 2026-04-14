🚀 📊 Portfolio Optimizer (Quant Finance Project)
🔥 Overview

This project is a portfolio optimization and backtesting system built using Python and Streamlit.

It allows users to input stock tickers and generate an optimal portfolio allocation using Modern Portfolio Theory, then evaluate performance using historical backtesting.

🎯 Key Features
📊 Portfolio optimization (Sharpe ratio maximization)
💰 Backtesting using historical market data
⚖️ Benchmark comparison (Equal-weight portfolio)
📈 Equity curve visualization
🧮 Risk metrics (return, volatility, Sharpe ratio)
🎛 Interactive Streamlit dashboard
🧠 Methodology

The model is based on:

Modern Portfolio Theory

Steps:
Compute historical returns
Estimate:
Expected returns
Covariance matrix
Optimize weights by maximizing Sharpe ratio
Backtest portfolio performance
Compare with equal-weight benchmark
📊 Outputs
✔ Portfolio Allocation
Optimal weights per asset
✔ Performance Metrics
Expected return
Volatility
Sharpe ratio
✔ Backtest Results
Total return
Equity curve ($10,000 initial capital)
Benchmark comparison
🛠 Tech Stack
Python 🐍
Streamlit 📊
Pandas
NumPy
SciPy
Yahoo Finance API
📈 Example Output
Input:
AAPL, MSFT, NVDA, AMZN, TSLA

Period:
2023-01-01 → 2024-01-01
Result:
Optimized portfolio weights
Sharpe-maximized allocation
Backtest equity curve
Benchmark comparison
📉 Limitations
Uses historical data only (no predictive ML model)
No transaction costs included
No market regime detection
No walk-forward optimization (future improvement)
🚀 Future Improvements
Walk-forward optimization (hedge fund style)
Risk parity portfolio
Transaction cost modeling
Factor-based models (Fama-French)
Real-time data integration
👨‍💻 Author

Nhat Quang
Applied & Computational Mathematics Student (USF)

⭐ Project Goal

This project demonstrates:

Quantitative finance modeling
Portfolio optimization techniques
Data-driven decision making
End-to-end data science pipeline
