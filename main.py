import data
import datainterpretation
import hackathonann
import datetime

def main():
    stockInput = input("Enter a stock ticker: ")
    stockInfoDict = data.getInfoDict(stockInput)
    dataCollection = datainterpretation.KeywordCollection(stockInfoDict)
    dayDictionary = dataCollection.getDayDictionary()
    print(dayDictionary)

    neural_network = hackathonann.NN(2, 3, 1)

    i = 0
    for day in dayDictionary:
        if i = 0:
            today = dayDictionary[day]
        else if: i < dayDictionary.length()*2/3
            neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"], dayDictionary[day]["daily_change"], False)
        else:
            neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"], dayDictionary[day]["daily_change"], True)
main()
