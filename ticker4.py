import streamlit as st
import requests
import pandas as pd

# Streamlit UI
st.title("📊 SPY Stock Dashboard (Alpha Vantage + Streamlit Charts)")

# User inputs API key
api_key = st.text_input("Enter your Alpha Vantage API Key:", type="password")

# Fetch live price and historical data if API key is provided
if api_key:
    symbol = "SPY"

    # Live price
    quote_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    quote_response = requests.get(quote_url)

    if quote_response.status_code == 200:
        quote_data = quote_response.json()
        quote = quote_data.get("Global Quote", {})
        price = quote.get("05. price", "N/A")
        previous_close = quote.get("08. previous close", "N/A")

        try:
            price_float = float(price)
            previous_float = float(previous_close)
            delta = price_float - previous_float
            st.metric(label="SPY Price", value=f"${price_float:.2f}", delta=f"${delta:.2f}")
        except:
            st.error("Error parsing live price data.")
    else:
        st.error("Failed to fetch live price data.")

    # Historical data
    history_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}"
    history_response = requests.get(history_url)

    if history_response.status_code == 200:
        history_data = history_response.json()
        time_series = history_data.get("Time Series (Daily)", {})

        if time_series:
            df = pd.DataFrame.from_dict(time_series, orient='index')
            df.index = pd.to_datetime(df.index)
            df.sort_index(inplace=True)
            df = df.tail(30)
            df["adjusted_close"] = df["5. adjusted close"].astype(float)

            st.markdown("### 📉 SPY Historical Price (Last 30 Days)")
            st.line_chart(df["adjusted_close"])
        else:
            st.warning("No historical data found.")
    else:
        st.error("Failed to fetch historical data.")
else:
    st.info("Please enter your Alpha Vantage API key to view live and historical data.")
