class KeywordCollection:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keywords = []
        self.eatDictionary(dictionary)

    def eatDictionary(self, dictionary):
        for date in dictionary:
            value_to_assign = dictionary[date]["daily_change"]
            for i in range(len(dictionary[date]["articles"])):
                title_words = dictionary[date]["articles"][i]["title"].split()
                description_words = []
                if dictionary[date]["articles"][i]["description"] is not None:
                    description_words = dictionary[date]["articles"][i]["title"].split()
                all_words = title_words + description_words
                filtered_words =                                                                                        # Add a filter function.
                for word in all_words:
                    if self.isDuplicate(word):
                        self.keywords[self.findIndex(word)].addAppearance(value_to_assign)
                    else:
                        self.keywords.append(Keyword(word, value_to_assign))
        for keyword in self.keywords:
            keyword.calculateWeight()

    def filterGarbageWords(self, words):
        garbage_words = ["for", "and", "nor", "but", "or", "yet", "so",
                         "he", "she", "it", "them", "they"]
        for word in words:
            for garbage_word in garbage_words:
                if word == garbage_word:
                    words.remove()

    def isDuplicate(self, word):
        flag = False
        for keyword in self.keywords:
            if word == keyword.getWord():
                flag = True
        return flag

    def findIndex(self, word):
        for i in self.keywords:
            if self.keywords[i] == word:
                return i


class Keyword:
    def __init__(self, word, appearance):
        self.word = word
        self.weight = 0
        self.appearances = [appearance]

    def getWord(self):
        return self.word

    def addAppearance(self, value):
        self.appearances.append(value)

    def calculateWeight(self):
        self.weight = sum(self.appearances)/len(self.appearances)
