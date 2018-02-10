def KeywordCollection:
    def __init__(self, dict):
        self.dictionary = dict
        self.keywords = []

    def eatDictionary(dict):
        for date in dict:
            value_to_assign = dict[date][""]

class Keyword:

    def __init__(self, word):
        self.word = word
        self.weight = 0
        self.appearances = []

    def getWord(self):
        return self.word

    def addAppearance(self, value):
        self.appearances.append(value)

    def calculateWeight(self):
        total = sum(self.appearances)
