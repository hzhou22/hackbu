import requests

class Data:

    def getStockData(self, stock_name):
        stock_data = requests.get('https://www.alphavantage.co/query?'
            'function=TIME_SERIES_DAILY&'
            'symbol=' + stock_name + '&'
            'apikey=f5f6bcd710b04091bab2fa73f226d1e5')
        json_stock_data = stock_data.json()
        return json_stock_data

    def getNewsData(self):
        news_data = requests.get('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2018-02-10&'
           'sortBy=popularity&'
           'apiKey=f5f6bcd710b04091bab2fa73f226d1e5')
        json_news_data = news_data.json()
        return json_news_data

    def getDailyChange(self, stock_data):
        daily_change_data = {}
        for day in stock_data["Time Series (Daily)"]:
            daily_change_data[day] = float(stock_data[day]["1. open"]) - float(stock_data[day]["4. close"])
        return daily_change_data
