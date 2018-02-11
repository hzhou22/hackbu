import requests

def getStockData(stock_name):
    stock_data = requests.get('https://www.alphavantage.co/query?'
        'function=TIME_SERIES_DAILY&'
        'symbol=' + stock_name + '&'
        'apikey=f5f6bcd710b04091bab2fa73f226d1e5')
    json_stock_data = stock_data.json()
    return json_stock_data

def getArticlesList(stock_name):
    complete_articles_list = []
    for i in range(5):
        news_data = requests.get('https://newsapi.org/v2/everything?'
            'q='+stock_name+'&'
            'from=2017-11-10&'
            'language=en&'
            'pageSize=100&'
            'page='+str(i+1)+'&'
            'sortBy=popularity&'
           'apiKey=f5f6bcd710b04091bab2fa73f226d1e5')
        json_news_data = news_data.json()
        complete_articles_list += json_news_data["articles"]
    return complete_articles_list

def getDailyChange(stock_data):
    daily_change_data = {}
    for day in stock_data["Time Series (Daily)"]:
        daily_change_data[day] = ((float(stock_data["Time Series (Daily)"][day]["1. open"]) - float(stock_data["Time Series (Daily)"][day]["4. close"])) / float(stock_data["Time Series (Daily)"][day]["1. open"]))
    return daily_change_data

def getDailyNews(daily_change_data, articles_list):
    final_dict = {}
    for day in daily_change_data:
        daily_change = daily_change_data[day]
        final_dict[day] = {}
        final_dict[day]["daily_change"] = daily_change
        final_dict[day]["articles"] = []
        for article in articles_list:
            if(article["publishedAt"][:10] == day):
                article_dict = {}
                article_dict["title"] = article["title"]
                article_dict["description"] = article["description"]
                final_dict[day]["articles"].append(article_dict)
    return final_dict

def getInfoDict(ticker):
    testStockData = getStockData(ticker)
    testCompanyName = getCompanyName(ticker)
    testNewsData = getArticlesList(testCompanyName)
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
