import requests

def getStockData(stock_name):
    stock_data = requests.get('https://www.alphavantage.co/query?'
        'function=TIME_SERIES_DAILY&'
        'symbol=' + stock_name + '&'
        'apikey=f5f6bcd710b04091bab2fa73f226d1e5')
    json_stock_data = stock_data.json()
    return json_stock_data

def getNewsData(stock_name):
    news_data = requests.get('https://newsapi.org/v2/everything?'
        'q='+stock_name+'&'
        'from=2017-09-20&'
        'sortBy=popularity&'
       'apiKey=f5f6bcd710b04091bab2fa73f226d1e5')
    json_news_data = news_data.json()
    return json_news_data

def getDailyChange(stock_data):
    daily_change_data = {}
    for day in stock_data["Time Series (Daily)"]:
        daily_change_data[day] = ((float(stock_data["Time Series (Daily)"][day]["1. open"]) - float(stock_data["Time Series (Daily)"][day]["4. close"])) / float(stock_data["Time Series (Daily)"][day]["1. open"]))
    return daily_change_data

def getDailyNews(daily_change_data, json_news_data):
    final_dict = {}
    for day in daily_change_data:
        daily_change = daily_change_data[day]
        final_dict[day] = {}
        final_dict[day]["daily_change"] = daily_change
        final_dict[day]["articles"] = []
        for newsArticle in json_news_data["articles"]:
            if(newsArticle["publishedAt"][:10] == day):
                article_dict = {}
                article_dict["title"] = newsArticle["title"]
                article_dict["description"] = newsArticle["description"]
                final_dict[day]["articles"].append(article_dict)
    return final_dict

def getInfoDict(ticker):                                                                                                      # Drew: add string input and
    testStockData = getStockData(ticker)
    testCompanyName = getCompanyName(testStockData)
    testNewsData = getNewsData(testCompanyName)
    dailyChange = getDailyChange(testStockData)
    return getDailyNews(dailyChange, testNewsData)

def getCompanyName(ticker):
    companyNames = requests.get("http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)).json()
    removeList = ['Corporation', 'Inc.', 'Incorporated', 'Corp.', 'Inc', 'Corp', ', ']
    for company in companyNames['ResultSet']['Result']:
        if company['symbol'] == ticker:
            return_name = company['name']
            for suffix in removeList:
                return_name = return_name.replace(suffix, "")
            return return_name
