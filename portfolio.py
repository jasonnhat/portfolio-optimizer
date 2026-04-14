import numpy as np
from data import get_price_data, compute_returns
from scipy.optimize import minimize

def run_portfolio(tickers, start, end, risk_free_rate=0.04):

    # -------------------
    # DATA
    # -------------------
    prices = get_price_data(tickers, start, end)
    prices = prices.dropna()

    returns = compute_returns(prices)

    # remove bad columns
    returns = returns.loc[:, returns.std() > 0]

    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    # -------------------
    # OPTIMIZATION
    # -------------------
    def get_portfolio_stats(weights):
        weights = np.array(weights)
        port_ret = np.sum(mean_returns * weights)
        port_vol = np.sqrt(weights.T @ cov_matrix @ weights)
        sharpe = (port_ret - risk_free_rate) / port_vol
        return port_ret, port_vol, sharpe

    def neg_sharpe(weights):
        return -get_portfolio_stats(weights)[2]

    n = len(mean_returns)
    init_guess = np.ones(n) / n

    bounds = [(0, 1)] * n
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

    result = minimize(
        neg_sharpe,
        init_guess,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    weights = result.x
    ret, vol, sharpe = get_portfolio_stats(weights)

    # -------------------
    # OUTPUT
    # -------------------
    output = {
        "tickers": list(mean_returns.index),
        "weights": weights,
        "return": ret,
        "volatility": vol,
        "sharpe": sharpe
    }

    return output