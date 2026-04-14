import numpy as np
from scipy.optimize import minimize

def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate, tickers):

    def stats(w):
        w = np.array(w)
        ret = np.sum(mean_returns * w)
        vol = np.sqrt(w.T @ cov_matrix @ w)
        sharpe = (ret - risk_free_rate) / vol
        return ret, vol, sharpe

    def neg_sharpe(w):
        return -stats(w)[2]

    bounds = [(0,1)] * len(tickers)
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    init = [1/len(tickers)] * len(tickers)

    result = minimize(neg_sharpe, init, method="SLSQP",
                      bounds=bounds, constraints=constraints)

    w = result.x
    ret, vol, sharpe = stats(w)

    return w, ret, vol, sharpe