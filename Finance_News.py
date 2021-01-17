# Xavier Souffront
# 12/26/2020
# Finance News 

#Web Scrape for financial news

import yfinance as yf 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup 


url = "https://www.marketwatch.com/"
html = urlopen(url)
bs = BeautifulSoup(html.read(),"html.parser")

article = bs.find_all('a', class_="link")

for link in article: 
    if link.has_attr('href'):
        print(link.attrs['href'])
    
#Gathering Stock Data

tickerData = yf.Ticker('MSFT')
tickerDf = tickerData.history(period= '1d', start= '2010-1-1', end= '2020-1-25')

print(tickerDf)