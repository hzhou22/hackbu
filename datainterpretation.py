import data

class KeywordCollection:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keywords = []

        self.eatDictionary()

    def eatDictionary(self):
        for date in self.dictionary:
            value_to_assign = self.dictionary[date]["daily_change"]
            for i in range(len(self.dictionary[date]["articles"])):
                title_words = self.dictionary[date]["articles"][i]["title"].split()
                description_words = []
                if self.dictionary[date]["articles"][i]["description"] is not None:
                    description_words = self.dictionary[date]["articles"][i]["description"].split()
                all_words = title_words + description_words
                filtered_words = self.refine(all_words)
                for word in filtered_words:
                    if self.isDuplicate(word):
                        self.keywords[self.findIndex(word)].addAppearance(value_to_assign)
                    else:
                        self.keywords.append(Keyword(word, value_to_assign))
        for keyword in self.keywords:
            keyword.calculateWeight()

    def refine(self, words):
        garbage_words = ["for", "and", "nor", "but", "or", "yet", "so",
                         "he", "she", "it", "them", "they"
                         "i", "you", "we", "us", "a", "my", "to", "the",
                         "its", "of", "in", "that", "what", "do", "as", "me",
                         "was", "him", "this", "isnt", "that", "thats", "is",
                         "has", "be", "will", "an", "are", "like", "there", "either",
                         "or", "but", "also", "neither", "both", "whether", "rather",
                         "thing", "ive", "if," "their", "our", "your", "with"]

        punctuations = ['.', ',', ':', ';', '"', "'", "’", "“", "”" "'s", "(", ")", "?", "!", "…"]
        i_offset = 0
        for i in range(len(words)):
            current_word = words[i - i_offset].lower()

            for punctuation in punctuations:
                current_word = current_word.replace(punctuation, '')

            words[i - i_offset] = current_word

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

    def getDayDictionary(self):
        dict_return = {}
        for date in self.dictionary:
            dayStockChange = self.dictionary[date]["daily_change"]
            dayTotalImpact = 0
            numberOfArticles = len(self.dictionary[date]["articles"])
            if numberOfArticles != 0:
                for i in range(len(self.dictionary[date]["articles"])):

                    articleImpact = 0
                    wordsOfArticle = (self.dictionary[date]["articles"][i]["title"]
                                     + self.dictionary[date]["articles"][i]["description"]).split()
                    for word in wordsOfArticle:
                        for keyword in self.keywords:
                            if word == keyword.getWord():
                                articleImpact += keyword.getImpact()
                    dayTotalImpact += articleImpact
                dict_return[date] = {"impact": dayTotalImpact,
                                     "number_of_articles": numberOfArticles,
                                     "daily_change": dayStockChange}
        return dict_return


class Keyword:
    def __init__(self, word, appearance):
        self.word = word
        self.impact = 0
        self.appearances = [appearance]

    def getWord(self):
        return self.word

    def getImpact(self):
        return self.impact

    def addAppearance(self, value):
        self.appearances.append(value)

    def calculateWeight(self):
        self.impact = sum(self.appearances) / len(self.appearances)
