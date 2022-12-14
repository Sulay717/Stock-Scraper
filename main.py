import urllib.request
import re

#Instructions
print("Please enter a stock ticker you are interested in")
print("If you are done enter 1")

#Essensial Needs
link = "https://finance.yahoo.com/quote/%s"
stockList = []

while True:
    Stock = input("Enter a stock ticker: ")
    if Stock == "1":
        break
    try:
        if int(Stock):
            print("Please enter a real stock Ticker")
    except:
        stockList.append(Stock)





for stock in stockList:
    site = link%stock
    print(site)



site = urllib.request .urlopen("https://finance.yahoo.com/")
search = re.findall()

line = site.decode.strip()