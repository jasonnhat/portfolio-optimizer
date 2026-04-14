import numpy as np

def sharpe_ratio(returns, rf=0.0):
    return (returns.mean() * 252 - rf) / (returns.std() * np.sqrt(252))


def annual_return(equity):
    return equity.iloc[-1] ** (252/len(equity)) - 1


def volatility(returns):
    return returns.std() * np.sqrt(252)