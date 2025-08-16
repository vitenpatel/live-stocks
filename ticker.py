import streamlit as st
import yfinance as yf

st.title("📈 Live SPY Stock Price")

ticker = yf.Ticker("SPY")
price = ticker.info.get("regularMarketPrice", "N/A")
previous = ticker.info.get("previousClose", "N/A")
delta = price - previous if isinstance(price, float) and isinstance(previous, float) else "N/A"

st.metric(label="SPY Price", value=f"${price}", delta=f"${delta:.2f}" if isinstance(delta, float) else "N/A")
