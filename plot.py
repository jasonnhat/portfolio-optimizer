import streamlit as st
import matplotlib.pyplot as plt

def plot_frontier(results, opt_ret, opt_vol):

    fig, ax = plt.subplots(figsize=(10, 6))

    sc = ax.scatter(
        results["vols"],
        results["returns"],
        c=results["sharpe"],
        cmap="viridis",
        alpha=0.3
    )

    plt.colorbar(sc, ax=ax, label="Sharpe Ratio")

    ax.scatter(
        opt_vol,
        opt_ret,
        color="red",
        marker="*",
        s=300,
        label="Optimal Portfolio"
    )

    ax.set_xlabel("Volatility")
    ax.set_ylabel("Return")
    ax.set_title("Efficient Frontier")
    ax.legend()

    st.pyplot(fig)