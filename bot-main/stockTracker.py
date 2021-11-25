# get user message
# strip '!' from string
# pass ticker in uppercase to yfinance Ticker()
# msft.info will return json object
import yfinance as yf

import pprint
def getStockPrice(msg):
    # Strip $ from front of user message
    # If there are numerical values in the user message, the user is not likely
    # looking up a stock, (most likely a dollar amount i.e. $123) so we send a money gif
    stockString = str(msg).split("$")[1]
    if (not stockString.isdigit()):
        try:
            stockObject = (yf.Ticker(stockString.upper()))
            #pprint.pprint(stockObject.info)
            currentPrice = stockObject.info['currentPrice']
            currency = stockObject.info['currency']
            closePrice = stockObject.info['previousClose']
            dollarChange = currentPrice - closePrice
            percentChange = (dollarChange / closePrice) * 100
            # print("dollarChange " + str(round(dollarChange, 2)))
            # print("percentChange " + str(round(percentChange, 2)))
            return (f'The current price of {stockString.upper()} is ${currentPrice} {currency}. Price change: ${round(dollarChange, 2)} Percent change: {round(percentChange, 2)}%')
        except KeyError:
            try:
                stockObject = (yf.Ticker(stockString.upper()))
                currentPrice = stockObject.info['regularMarketPrice']
                currency = stockObject.info['currency']
                dollarChange = stockObject.info['regularMarketChange']
                percentChange = (stockObject.info['regularMarketChangePercent']) * 100
                return (f'The current price of {stockString.upper()} is ${currentPrice} {currency}. Price change: ${round(dollarChange, 2)} Percent change: {round(percentChange, 2)}%')
                #return stockObject.info['regularMarketPrice']
            except:
                return './img/bender-broken.gif'
        except:
            return './img/bender-broken.gif'
        
    else: 
        return './img/bender-money.gif'
