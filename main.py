import data
import datainterpretation
import hackathonann

def main():
    stockInput = input("Enter a stock ticker: ")
    stockInfoDict = data.getInfoDict(stockInput)
    dataCollection = datainterpretation.KeywordCollection(stockInfoDict)
<<<<<<< HEAD
=======
    dayDictionary = dataCollection.getDayDictionary()
>>>>>>> 02d8dea054babf4dd1456fe63a05e88e141e1619

main()
