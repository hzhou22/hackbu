import data
import requests

def getInfoDict():
    testStockData = data.getStockData("AAPL")
    testNewsData = data.getNewsData("Apple")
    dailyChange = data.getDailyChange(testStockData)
    return(data.getDailyNews(dailyChange, testNewsData))
