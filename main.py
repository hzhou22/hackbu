import data
import datainterpretation
import hackathonann
import datetime

def main():
    stockInput = input("Enter a stock ticker: ")
    stockInfoDict = data.getInfoDict(stockInput)
    dataCollection = datainterpretation.KeywordCollection(stockInfoDict)
    dayDictionary = dataCollection.getDayDictionary()
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======
    print(dayDictionary)
    
>>>>>>> 3b4ee2d49fcb80bf5adf8b27c0acd342af5d44c8
    neural_network = hackathonann.NN(2, 3, 1)
>>>>>>> c2aa4f13158d52751b0a716e437b76cfedcb5a95

    i = 0
    for day in dayDictionary:
        if i == 0:
            today = dayDictionary[day]
        elif i < len(dayDictionary)*2/3:
            neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"], dayDictionary[day]["daily_change"], False)
        else:
            neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"], dayDictionary[day]["daily_change"], True)
        i+=1
    neural_network.finalTest(today["impact"], today["number_of_articles"])
main()
