{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa240\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\'a0streamlit\'a0as\'a0st\
import\'a0pandas\'a0as\'a0pd\
import\'a0matplotlib.pyplot\'a0as\'a0plt\
import\'a0yfinance\'a0as\'a0yf\
\
#\'a0Chuck\'a0Akre's\'a0portfolio\'a0data\'a0as\'a0of\'a0Q1\'a02025\
data\'a0=\'a0[\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"MA",\'a0"Company":\'a0"Mastercard\'a0Inc",\'a0"Portfolio\'a0%":\'a017.56,\'a0"Shares\'a0Held":\'a03331076,\'a0"Value\'a0($B)":\'a01.83,\'a0"Activity":\'a0"Reduced\'a0by\'a010.06%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"ORLY",\'a0"Company":\'a0"O'Reilly\'a0Automotive\'a0Inc",\'a0"Portfolio\'a0%":\'a011.90,\'a0"Shares\'a0Held":\'a012958650,\'a0"Value\'a0($B)":\'a01.24,\'a0"Activity":\'a0"Reduced\'a0by\'a03.50%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"MCO",\'a0"Company":\'a0"Moody's\'a0Corp",\'a0"Portfolio\'a0%":\'a010.90,\'a0"Shares\'a0Held":\'a02435458,\'a0"Value\'a0($B)":\'a01.13,\'a0"Activity":\'a0"Reduced\'a0by\'a020.90%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"V",\'a0"Company":\'a0"Visa\'a0Inc",\'a0"Portfolio\'a0%":\'a010.70,\'a0"Shares\'a0Held":\'a03175240,\'a0"Value\'a0($B)":\'a01.11,\'a0"Activity":\'a0"Reduced\'a0by\'a02.95%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"KKR",\'a0"Company":\'a0"KKR\'a0&\'a0Co.\'a0Inc",\'a0"Portfolio\'a0%":\'a09.83,\'a0"Shares\'a0Held":\'a08847564,\'a0"Value\'a0($B)":\'a01.02,\'a0"Activity":\'a0"Reduced\'a0by\'a013.96%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"BN",\'a0"Company":\'a0"Brookfield\'a0Corp",\'a0"Portfolio\'a0%":\'a09.62,\'a0"Shares\'a0Held":\'a019094021,\'a0"Value\'a0($B)":\'a01.00,\'a0"Activity":\'a0"Added\'a00.66%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"ROP",\'a0"Company":\'a0"Roper\'a0Technologies\'a0Inc",\'a0"Portfolio\'a0%":\'a08.22,\'a0"Shares\'a0Held":\'a01449188,\'a0"Value\'a0($B)":\'a00.854,\'a0"Activity":\'a0"Reduced\'a0by\'a02.21%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"CSGP",\'a0"Company":\'a0"CoStar\'a0Group\'a0Inc",\'a0"Portfolio\'a0%":\'a07.09,\'a0"Shares\'a0Held":\'a09313592,\'a0"Value\'a0($B)":\'a00.738,\'a0"Activity":\'a0"No\'a0change"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"AMT",\'a0"Company":\'a0"American\'a0Tower\'a0Corp",\'a0"Portfolio\'a0%":\'a05.42,\'a0"Shares\'a0Held":\'a02589192,\'a0"Value\'a0($B)":\'a00.563,\'a0"Activity":\'a0"Reduced\'a0by\'a052.95%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"DHR",\'a0"Company":\'a0"Danaher\'a0Corp",\'a0"Portfolio\'a0%":\'a03.50,\'a0"Shares\'a0Held":\'a01775400,\'a0"Value\'a0($B)":\'a00.364,\'a0"Activity":\'a0"No\'a0change"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"ABNB",\'a0"Company":\'a0"Airbnb\'a0Inc",\'a0"Portfolio\'a0%":\'a03.35,\'a0"Shares\'a0Held":\'a0None,\'a0"Value\'a0($B)":\'a0None,\'a0"Activity":\'a0"Added\'a010.13%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"CCCS",\'a0"Company":\'a0"CCC\'a0Intelligent\'a0Solutions",\'a0"Portfolio\'a0%":\'a01.15,\'a0"Shares\'a0Held":\'a0None,\'a0"Value\'a0($B)":\'a0None,\'a0"Activity":\'a0"Added\'a023.49%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"KMX",\'a0"Company":\'a0"CarMax\'a0Inc",\'a0"Portfolio\'a0%":\'a0None,\'a0"Shares\'a0Held":\'a0None,\'a0"Value\'a0($B)":\'a0None,\'a0"Activity":\'a0"Reduced\'a0by\'a069.24%"\},\
\'a0\'a0\'a0\'a0\{"Ticker":\'a0"DBRG",\'a0"Company":\'a0"DigitalBridge\'a0Group\'a0Inc",\'a0"Portfolio\'a0%":\'a0None,\'a0"Shares\'a0Held":\'a0None,\'a0"Value\'a0($B)":\'a0None,\'a0"Activity":\'a0"Reduced\'a0by\'a078.46%"\}\
]\
\
#\'a0Convert\'a0to\'a0DataFrame\
df\'a0=\'a0pd.DataFrame(data)\
\
#\'a0Fetch\'a0live\'a0prices\'a0using\'a0yfinance\
def\'a0get_live_price(ticker):\
\'a0\'a0\'a0\'a0try:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0stock\'a0=\'a0yf.Ticker(ticker)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0price\'a0=\'a0stock.info['regularMarketPrice']\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return\'a0price\
\'a0\'a0\'a0\'a0except:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return\'a0"N/A"\
\
#\'a0Add\'a0live\'a0prices\'a0to\'a0the\'a0DataFrame\
df["Live\'a0Price\'a0($)"]\'a0=\'a0df["Ticker"].apply(lambda\'a0x:\'a0get_live_price(x)\'a0if\'a0pd.notna(x)\'a0else\'a0"N/A")\
\
#\'a0Streamlit\'a0App\
st.title("Chuck\'a0Akre\'a0Portfolio\'a0Dashboard")\
st.markdown("###\'a0\uc0\u55357 \u56520 \'a0Portfolio\'a0with\'a0Live\'a0Prices")\
st.dataframe(df[["Ticker",\'a0"Company",\'a0"Portfolio\'a0%",\'a0"Shares\'a0Held",\'a0"Value\'a0($B)",\'a0"Live\'a0Price\'a0($)",\'a0"Activity"]])\
\
#\'a0Pie\'a0Chart\'a0for\'a0Portfolio\'a0Allocation\
st.markdown("###\'a0\uc0\u55358 \u56814 \'a0Portfolio\'a0Allocation\'a0by\'a0Stock")\
allocation_df\'a0=\'a0df.dropna(subset=["Portfolio\'a0%"])\
fig1,\'a0ax1\'a0=\'a0plt.subplots()\
ax1.pie(allocation_df["Portfolio\'a0%"],\'a0labels=allocation_df["Ticker"],\'a0autopct='%1.1f%%',\'a0startangle=90)\
ax1.axis('equal')\
st.pyplot(fig1)\
\
#\'a0Bar\'a0Chart\'a0for\'a0Recent\'a0Activity\
st.markdown("###\'a0\uc0\u55357 \u56521 \'a0Recent\'a0Activity")\
activity_counts\'a0=\'a0df["Activity"].value_counts()\
fig2,\'a0ax2\'a0=\'a0plt.subplots()\
activity_counts.plot(kind='bar',\'a0ax=ax2,\'a0color='skyblue')\
ax2.set_ylabel("Number\'a0of\'a0Stocks")\
ax2.set_title("Recent\'a0Portfolio\'a0Activity")\
st.pyplot(fig2)\
\
}