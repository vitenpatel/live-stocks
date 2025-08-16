import streamlit as st
import requests

# Streamlit UI
st.title("📈 Live SPY Stock Price (via Alpha Vantage)")

# User inputs API key
api_key = st.text_input("Enter your Alpha Vantage API Key:", type="password")

# Fetch live price if API key is provided
if api_key:
    symbol = "SPY"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data.get("Global Quote", {})
        price = quote.get("05. price", "N/A")
        previous_close = quote.get("08. previous close", "N/A")

        try:
            price_float = float(price)
            previous_float = float(previous_close)
            delta = price_float - previous_float
            st.metric(label="SPY Price", value=f"${price_float:.2f}", delta=f"${delta:.2f}")
        except:
            st.error("Error parsing price data.")
    else:
        st.error("Failed to fetch data from Alpha Vantage.")
else:
    st.info("Please enter your Alpha Vantage API key to view live data.")

