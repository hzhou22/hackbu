import data

def main():
    apple = data.getStockData("AAPL")
    print(apple)
    appleName = data.getCompanyName("AAPL")
    print(appleName)
    newsData = data.getNewsData(appleName)
    print(newsData)
    asdf = data.getDailyChange(apple)
    print(asdf)
main()
