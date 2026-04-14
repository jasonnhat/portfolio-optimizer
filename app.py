import streamlit as st
import pandas as pd
import numpy as np
from data import get_price_data
from optimizer import optimize_portfolio

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Portfolio Optimizer",
    layout="wide"
)

# =========================
# TITLE
# =========================
st.title("📊 Portfolio Optimizer Dashboard")

st.markdown("Modern portfolio optimization + backtest system")

# =========================
# INPUT
# =========================
tickers_input = st.text_input(
    "Tickers (comma separated)",
    "AAPL,MSFT,NVDA,AMZN,TSLA"
)

start = st.date_input("Start date")
end = st.date_input("End date")

risk_free = 0.04
initial_capital = 10000

# =========================
# RUN
# =========================
if st.button("Run"):

    # -------------------------
    # PROCESS TICKERS
    # -------------------------
    tickers = [t.strip().upper() for t in tickers_input.split(",")]

    # -------------------------
    # GET DATA
    # -------------------------
    prices = get_price_data(tickers, start, end)

    if prices.empty:
        st.error("No data returned from Yahoo Finance")
        st.stop()

    # -------------------------
    # RETURNS
    # -------------------------
    returns = prices.pct_change().dropna()

    if len(returns) < 50:
        st.error("Not enough data for backtest")
        st.stop()

    # =========================
    # OPTIMIZATION
    # =========================
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    weights, ret, vol, sharpe = optimize_portfolio(
        mean_returns,
        cov_matrix,
        risk_free,
        tickers
    )

    # =========================
    # BACKTEST PORTFOLIO
    # =========================
    portfolio_returns = returns @ weights
    equity = (1 + portfolio_returns).cumprod()
    portfolio_value = initial_capital * equity

    # =========================
    # BENCHMARK
    # =========================
    equal_weights = np.ones(len(tickers)) / len(tickers)

    eq_returns = returns @ equal_weights
    eq_equity = (1 + eq_returns).cumprod()
    eq_value = initial_capital * eq_equity

    # =========================
    # HEADER
    # =========================
    st.markdown("## 📊 Portfolio Overview")

    # =========================
    # WEIGHTS
    # =========================
    st.markdown("### 📌 Optimal Weights")

    col1, col2 = st.columns(2)

    with col1:
        for t, w in zip(tickers, weights):
            st.write(f"**{t}**")

    with col2:
        for t, w in zip(tickers, weights):
            st.write(f"{w:.2%}")

    # =========================
    # METRICS
    # =========================
    st.markdown("### 📊 Model Metrics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Expected Return", f"{ret:.2%}")
    c2.metric("Volatility", f"{vol:.2%}")
    c3.metric("Sharpe Ratio", f"{sharpe:.2f}")

    # =========================
    # PORTFOLIO VALUE
    # =========================
    st.markdown("### 💰 Portfolio Value ($10,000)")

    st.line_chart(portfolio_value, use_container_width=True)

    st.metric(
        "Final Value",
        f"${portfolio_value.iloc[-1]:,.2f}",
        f"{portfolio_value.iloc[-1] - initial_capital:,.2f}"
    )

    # =========================
    # BACKTEST RESULTS
    # =========================
    st.markdown("### 📈 Backtest Results")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Return",
        f"{(portfolio_value.iloc[-1]/initial_capital - 1):.2%}"
    )

    c2.metric(
        "Volatility",
        f"{returns.std().mean() * np.sqrt(252):.2%}"
    )

    c3.metric(
        "Sharpe Ratio",
        f"{sharpe:.2f}"
    )

    # =========================
    # COMPARISON
    # =========================
    st.markdown("### ⚖️ Benchmark Comparison")

    st.line_chart({
        "Optimized Portfolio": portfolio_value,
        "Equal Weight": eq_value
    }, use_container_width=True)