import data
import datainterpretation
import hackathonann

def main():
    stockInput = input("Enter a stock ticker: ")
    stockInfoDict = data.getInfoDict(stockInput)
    dataCollection = datainterpretation.KeywordCollection(stockInfoDict)

main()
