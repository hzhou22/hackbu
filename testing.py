import data
import requests

def main():
    testData = data.Data()
    testStockData = testData.getStockData("MSFT")
    testNewsData = testData.getNewsData()
    testData.getDailyChange(testStockData)
main()
