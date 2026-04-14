import numpy as np

def monte_carlo(mean_returns, cov_matrix, tickers, n=5000):

    results = {
        "weights": [],
        "returns": [],
        "vols": [],
        "sharpe": []
    }

    for _ in range(n):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)

        port_ret = np.sum(mean_returns * weights)
        port_vol = np.sqrt(weights.T @ cov_matrix @ weights)
        sharpe = port_ret / port_vol

        results["weights"].append(weights)
        results["returns"].append(port_ret)
        results["vols"].append(port_vol)
        results["sharpe"].append(sharpe)

    return results