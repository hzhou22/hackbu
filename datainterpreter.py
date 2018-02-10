class KeywordCollection:
    def __init__(self, dict):
        self.dictionary = dict
        self.keywords = []
        self.eatDictionary(dict)

    def eatDictionary(self, dict):
        for date in dict:
            value_to_assign = dict[date]["daily_change"]
            for i in range(len(dict[date]["articles"])):
                title_words = dict[date]["articles"][i]["title"].split()
                description_words = []
                if dict[date]["articles"][i]["description"] is not None:
                    description_words = dict[date]["articles"][i]["title"].split()
                all_words = title_words + description_words
#                filtered_words =                                                                                        # Add a filter function.
                for word in all_words:
                    if self.isDuplicate(word):
                        self.keywords[self.findIndex(word)].addAppearance(value)
                    self.keywords.append(Keyword(word, value_to_assign))

    def isDuplicate(self, word):
        flag = False
        for keyword in self.words:
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
        total = sum(self.appearances)
