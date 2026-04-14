from portfolio import run_portfolio

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

result = run_portfolio(
    tickers=tickers,
    start="2023-01-01",
    end="2024-01-01"
)

print("OPTIMAL WEIGHTS")
for t, w in zip(result["tickers"], result["weights"]):
    print(t, round(w, 3))

print("\nReturn:", result["return"])
print("Vol:", result["volatility"])
print("Sharpe:", result["sharpe"])