import yfinance as yf 
import streamlit as st
from PIL import Image
from urllib.request import urlopen

st.title("Crptocurrency Daily Prices-")
st.header("Dashboard-")



#Defining Variables-

Bitcoin="BTC-USD"
Ethereum="ETH-USD"
Ripple="XRP-USD"
BitcoinCash="BCH-USD"

#Access  data from Yahoo Finance-
BTC_Data=yf.Ticker(Bitcoin)
ETH_Data=yf.Ticker(Ethereum)
XRP_Data=yf.Ticker(Ripple)
BCH_Data=yf.Ticker(BitcoinCash)

#Fetch History Data from Yahoo Finance-
BTCHis=BTC_Data.history(period="max")
ETHHis=ETH_Data.history(period="max")
XRPHis=XRP_Data.history(period="max")
BCHHis=BCH_Data.history(period="max")

#Fetch Crptocurrency data for the dataframe-
BTC=yf.download(Bitcoin, start='2022-02-15', end='2022-02-18')
ETH=yf.download(Ethereum,start='2022-02-15',end='2022-02-18')
XRP=yf.download(Ripple,start='2022-02-15',end='2022-02-18')
BCH=yf.download(BitcoinCash,start='2022-02-15',end='2022-02-18')

#Bitcoin-
st.write("BITCOIN ($)")
imageBTC=Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))

#Display image-
st.image(imageBTC)
#Display dataframe-
st.table(BTC)
#Display a chart -
st.bar_chart(BTCHis.Close)

#Ethereum-
st.write("Etherum($)")
imageETH=Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))

#Display image-
st.image(imageETH)
#Display dataframe-
st.table(ETH)
#Display a chart -
st.bar_chart(ETHHis.Close)

#Ripple-
st.write("RIPPLE($)")
imageXRP=Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))

#Display image-
st.image(imageXRP)
#Display dataframe-
st.table(XRP)
#Display a chart -
st.bar_chart(XRPHis.Close)

#BitcoinCash-
st.write("BITCOIN CASH ($)")
imageBCH=Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))

#Display image-
st.image(imageBCH)
#Display dataframe-
st.table(BCH)
#Display a chart -
st.bar_chart(BCHHis.Close)


st.header("Thank You Pankaj Sir ")