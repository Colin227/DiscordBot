# get user message
# strip '!' from string
# pass ticker in uppercase to yfinance Ticker()
# msft.info will return json object
import yfinance as yf

import pprint
# pprint used for testing

def getStockPrice(msg):
    # Strip $ from front of user message
    # If there are numerical values in the user message, the user is not likely
    # looking up a stock, (most likely a dollar amount i.e. $123) so we send a money gif
    stockString = str(msg).split("$")[1]
    

    try:
        stockObject = (yf.Ticker(stockString.upper()))
        # pprint will display formatted stockObject
        #pprint.pprint(stockObject.info)
        symbol = stockObject.info['symbol']
        currentPrice = stockObject.info['currentPrice']
        currency = stockObject.info['currency']
        closePrice = stockObject.info['previousClose']
        dollarChange = currentPrice - closePrice
        percentChange = (dollarChange / closePrice) * 100
        stockDict = {
            'symbol': symbol,
            'currentPrice': currentPrice,
            'currency': currency,
            'closePrice': closePrice,
            'dollarChange': dollarChange,
            'percentChange': percentChange,
            'shortName' : stockObject.info['shortName'],
            'logo': stockObject.info['logo_url']
        }
        # print("dollarChange " + str(round(dollarChange, 2)))
        # print("percentChange " + str(round(percentChange, 2)))
        return stockDict
    
    # Canadian stocks were causing KeyErrors since stock price has different keys

    except KeyError:
        try:
            stockObject = (yf.Ticker(stockString.upper()))
            symbol = stockObject.info['symbol']
            currentPrice = stockObject.info['regularMarketPrice']
            currency = stockObject.info['currency']
            closePrice = stockObject.info['regularMarketPreviousClose']
            dollarChange = stockObject.info['regularMarketChange']
            percentChange = (stockObject.info['regularMarketChangePercent']) * 100

            stockDict = {
                'symbol': symbol,
                'currentPrice': currentPrice,
                'currency': currency,
                'closePrice': closePrice,
                'dollarChange': dollarChange,
                'percentChange': percentChange,
                'shortName' : stockObject.info['shortName'],
                'logo': stockObject.info['logo_url']
        }
            return stockDict
        except:
            return "STOCK_NOT_FOUND"
