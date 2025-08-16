import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Chuck Akre's portfolio data as of Q1 2025
data = [
    {"Ticker": "MA", "Company": "Mastercard Inc", "Portfolio %": 17.56, "Shares Held": 3331076, "Value ($B)": 1.83, "Activity": "Reduced by 10.06%"},
    {"Ticker": "ORLY", "Company": "O'Reilly Automotive Inc", "Portfolio %": 11.90, "Shares Held": 12958650, "Value ($B)": 1.24, "Activity": "Reduced by 3.50%"},
    {"Ticker": "MCO", "Company": "Moody's Corp", "Portfolio %": 10.90, "Shares Held": 2435458, "Value ($B)": 1.13, "Activity": "Reduced by 20.90%"},
    {"Ticker": "V", "Company": "Visa Inc", "Portfolio %": 10.70, "Shares Held": 3175240, "Value ($B)": 1.11, "Activity": "Reduced by 2.95%"},
    {"Ticker": "KKR", "Company": "KKR & Co. Inc", "Portfolio %": 9.83, "Shares Held": 8847564, "Value ($B)": 1.02, "Activity": "Reduced by 13.96%"},
    {"Ticker": "BN", "Company": "Brookfield Corp", "Portfolio %": 9.62, "Shares Held": 19094021, "Value ($B)": 1.00, "Activity": "Added 0.66%"},
    {"Ticker": "ROP", "Company": "Roper Technologies Inc", "Portfolio %": 8.22, "Shares Held": 1449188, "Value ($B)": 0.854, "Activity": "Reduced by 2.21%"},
    {"Ticker": "CSGP", "Company": "CoStar Group Inc", "Portfolio %": 7.09, "Shares Held": 9313592, "Value ($B)": 0.738, "Activity": "No change"},
    {"Ticker": "AMT", "Company": "American Tower Corp", "Portfolio %": 5.42, "Shares Held": 2589192, "Value ($B)": 0.563, "Activity": "Reduced by 52.95%"},
    {"Ticker": "DHR", "Company": "Danaher Corp", "Portfolio %": 3.50, "Shares Held": 1775400, "Value ($B)": 0.364, "Activity": "No change"},
    {"Ticker": "ABNB", "Company": "Airbnb Inc", "Portfolio %": 3.35, "Shares Held": None, "Value ($B)": None, "Activity": "Added 10.13%"},
    {"Ticker": "CCCS", "Company": "CCC Intelligent Solutions", "Portfolio %": 1.15, "Shares Held": None, "Value ($B)": None, "Activity": "Added 23.49%"},
    {"Ticker": "KMX", "Company": "CarMax Inc", "Portfolio %": None, "Shares Held": None, "Value ($B)": None, "Activity": "Reduced by 69.24%"},
    {"Ticker": "DBRG", "Company": "DigitalBridge Group Inc", "Portfolio %": None, "Shares Held": None, "Value ($B)": None, "Activity": "Reduced by 78.46%"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Fetch live prices using yfinance
def get_live_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.info['regularMarketPrice']
        return price
    except:
        return "N/A"

# Add live prices to the DataFrame
df["Live Price ($)"] = df["Ticker"].apply(lambda x: get_live_price(x) if pd.notna(x) else "N/A")

# Streamlit App
st.title("Chuck Akre Portfolio Dashboard")
st.markdown("### 📈 Portfolio with Live Prices")
st.dataframe(df[["Ticker", "Company", "Portfolio %", "Shares Held", "Value ($B)", "Live Price ($)", "Activity"]])

# Pie Chart for Portfolio Allocation
st.markdown("### 🧮 Portfolio Allocation by Stock")
allocation_df = df.dropna(subset=["Portfolio %"])
fig1, ax1 = plt.subplots()
ax1.pie(allocation_df["Portfolio %"], labels=allocation_df["Ticker"], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Bar Chart for Recent Activity
st.markdown("### 📉 Recent Activity")
activity_counts = df["Activity"].value_counts()
fig2, ax2 = plt.subplots()
activity_counts.plot(kind='bar', ax=ax2, color='skyblue')
ax2.set_ylabel("Number of Stocks")
ax2.set_title("Recent Portfolio Activity")
st.pyplot(fig2)
