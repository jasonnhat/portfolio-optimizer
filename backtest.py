import numpy as np
import pandas as pd

def walk_forward_backtest(
    prices,
    window=252,
    rebalance_step=21,
    optimize_fn=None
):

    returns = prices.pct_change().dropna()

    portfolio_returns = []
    weight_history = []

    # ======================
    # SAFETY CHECK (IMPORTANT)
    # ======================
    if len(returns) < window:
        raise ValueError(
            f"Not enough data. Need at least {window} rows, got {len(returns)}"
        )

    i = window

    while i < len(returns):

        train = returns.iloc[i-window:i]

        mean_returns = train.mean() * 252
        cov_matrix = train.cov() * 252

        try:
            weights, _, _, _ = optimize_fn(mean_returns, cov_matrix)
        except:
            n = len(train.columns)
            weights = np.ones(n) / n

        weights = np.array(weights)
        weight_history.append(weights)

        end = min(i + rebalance_step, len(returns))
        test = returns.iloc[i:end]

        # ======================
        # EMPTY SAFETY CHECK
        # ======================
        if len(test) == 0:
            break

        port_ret = test @ weights
        portfolio_returns.append(port_ret)

        i += rebalance_step

    # ======================
    # FINAL CHECK (IMPORTANT FIX)
    # ======================
    if len(portfolio_returns) == 0:
        raise ValueError("Walk-forward failed: no test periods generated.")

    full_returns = pd.concat(portfolio_returns).sort_index()
    equity_curve = (1 + full_returns).cumprod()

    return full_returns, equity_curve, np.array(weight_history)

def max_drawdown(equity_curve):
    peak = equity_curve.cummax()
    drawdown = (equity_curve - peak) / peak
    return drawdown.min()