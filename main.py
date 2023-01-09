import urllib.request
import re
import ssl

#Instructions
print("Please enter a stock ticker you are interested in")
print("If you are done enter 1")

#Essensial Needs
link = "https://finance.yahoo.com/quote/%s"
stockList = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

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
    ulink = link%stock
    print(ulink)
    site = urllib.request.urlopen(ulink,context=ctx).read()
    line = re.findall(b'href="(http[s]?://.*?)"', site)
    for line in site:
        print(line.decode())