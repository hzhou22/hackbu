import hackbu.data as data


class KeywordCollection:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keywords = []
        self.eatDictionary()

    def eatDictionary(self):
        for date in self.dictionary:
            value_to_assign = self.dictionary[date]["daily_change"]                                                          # do per article value
                                                                                                                        #
            for i in range(len(self.dictionary[date]["articles"])):
                title_words = self.dictionary[date]["articles"][i]["title"].split()
                description_words = []
                if self.dictionary[date]["articles"][i]["description"] is not None:
                    description_words = self.dictionary[date]["articles"][i]["description"].split()
                all_words = title_words + description_words
                filtered_words = self.filterGarbageWords(all_words)
                for word in filtered_words:
                    if self.isDuplicate(word):
                        self.keywords[self.findIndex(word)].addAppearance(value_to_assign)
                    else:
                        self.keywords.append(Keyword(word, value_to_assign))
        for keyword in self.keywords:
            keyword.calculateWeight()

    def filterGarbageWords(self, words):
        garbage_words = ["for", "and", "nor", "but", "or", "yet", "so",                                                 # Add more garbage!
                         "he", "she", "it", "them", "they"]
        i_offset = 0
        for i in range(len(words)):
            for garbage_word in garbage_words:
                if garbage_word == words[i - i_offset]:
                    words.pop(i - i_offset)
                    i_offset += 1
                    break

        return words

    def isDuplicate(self, word):
        flag = False
        for keyword in self.keywords:
            if word == keyword.getWord():
                flag = True
        return flag

    def findIndex(self, word):
        for i in range(len(self.keywords)):
            if self.keywords[i].getWord() == word:
                return i

    def getKeywords(self):
        return self.keywords


class Keyword:
    def __init__(self, word, appearance):
        self.word = word
        self.weight = 0
        self.appearances = [appearance]

    def getWord(self):
        return self.word

    def getWeight(self):
        return self.weight

    def addAppearance(self, value):
        self.appearances.append(value)

    def calculateWeight(self):
        self.weight = sum(self.appearances)/len(self.appearances)


def main():
    exampleDictionary = data.getInfoDict()
    myCollection = KeywordCollection(exampleDictionary)
    for keyword in myCollection.getKeywords():
        print(keyword.getWord(), keyword.getWeight())


main()