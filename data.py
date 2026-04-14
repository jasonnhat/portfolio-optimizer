import yfinance as yf
import pandas as pd


def get_price_data(tickers, start, end):

    # ensure list format
    if isinstance(tickers, str):
        tickers = [tickers]

    all_series = []

    for t in tickers:

        try:
            df = yf.download(
                t,
                start=start,
                end=end,
                auto_adjust=True,
                progress=False,
                threads=False   # ✅ IMPORTANT FIX for Streamlit stability
            )

            if df.empty:
                print(f"SKIP: {t}")
                continue

            close = df["Close"].copy()
            close.name = t

            all_series.append(close)

        except Exception as e:
            print(f"ERROR {t}: {e}")
            continue

    if len(all_series) == 0:
        raise ValueError("No data downloaded from Yahoo Finance")

    data = pd.concat(all_series, axis=1)

    # clean data
    data = data.dropna()
    data = data.sort_index()

    return data