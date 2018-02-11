from tkinter import *
import datainterpretation
import data
import hackathonann

class gui(Frame):
    def __init__(self):
        super().__init__(root)
        self.winfo_toplevel().title("StockPredict")
        self.main_frame = Frame(root)

        self.stock_ticker = StringVar()
        self.headline = StringVar()

        self.open_main_menu()


    def open_main_menu(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        title_label = Label(self.main_frame, text="Welcome to StockPredict!",
                            padx=20, pady=20, font=(None, 20))
        title_label.grid(row=0, columnspan=3)

        stock_screen_button = Button(self.main_frame, text="Predict Stock Change")
        stock_screen_button.bind("<Button-1>", self.open_stock_screen)
        stock_screen_button.grid(row=1, column=0)

        headline_screen_button = Button(self.main_frame, text="Predict Headline Effect")
        headline_screen_button.bind("<Button-1>", self.open_headline_screen)
        headline_screen_button.grid(row=1, column=1)

        word_screen_button = Button(self.main_frame, text="View Effective Words")
        word_screen_button.bind("<Button-1>", self.open_word_screen)
        word_screen_button.grid(row=1, column=2)

    def open_stock_screen(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        enter_stock_label = Label(self.main_frame, text="Enter Stock Ticker: ")
        enter_stock_label.grid(row=0, column=0)

        enter_stock_entry = Entry(self.main_frame, textvariable=self.stock_ticker)
        enter_stock_entry.grid(row=0, column=1)

        back_button = Button(self.main_frame, text="Back")
        back_button.bind("<Button-1>", self.open_main_menu)
        back_button.grid(row=1, column=0)

        enter_button = Button(self.main_frame, text="Enter")
        enter_button.bind("<Button-1>", self.open_prediction_screen)
        enter_button.grid(row=1, column=1)

        # Labels, etc.

    def open_prediction_screen(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

#        loading_label = Label(self.main_frame, text="Calculating...\n(This may take a few seconds.)")
 #       loading_label.grid(row=0, column=0)
        prediction_number = 0

        try:
            prediction_number = self.get_prediction()[0]
            print(prediction_number)
            prediction_string = self.stock_ticker.get() + " is predicted to "
            if prediction_number > 0.1:
                prediction_string += "drastically increase."
            elif prediction_number > 0.02:
                prediction_string += "moderately increase."
            elif prediction_number > -0.02:
                prediction_string += "hold steady."
            elif prediction_number > -0.1:
                prediction_string += "moderately decrease."
            else:
                prediction_string += "drastically decrease."

            prediction_label = Label(self.main_frame, text=prediction_string, font=(None, 20))
            prediction_label.grid(row=0, column=0, columnspan=2)

            back_to_menu_button = Button(self.main_frame, text="Back to Menu")
            back_to_menu_button.bind("<Button-1>", self.open_main_menu)
            back_to_menu_button.grid(row=1, column=0)

            new_prediction_button = Button(self.main_frame, text="Make Another Prediction")
            new_prediction_button.bind("<Button-1>", self.open_stock_screen)
            new_prediction_button.grid(row=1, column=1)

            self.stock_ticker.set("")

        except TypeError:
            self.stock_ticker = StringVar()
            self.open_stock_screen()

    def get_prediction(self):
        self.stock_ticker.set(self.stock_ticker.get().upper())
        stockInput = self.stock_ticker.get()
        stockInfoDict = data.getInfoDict(stockInput)
        dataCollection = datainterpretation.KeywordCollection(stockInfoDict)
        dayDictionary = dataCollection.getDayDictionary()

        neural_network = hackathonann.NN(2, 3, 1)

        i = 0
        today = None
        for day in dayDictionary:
            if i == 0:
                today = dayDictionary[day]
            elif i < len(dayDictionary) * 2 / 3:
                neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"],
                                    dayDictionary[day]["daily_change"], False)
            else:
                neural_network.demo(dayDictionary[day]["impact"], dayDictionary[day]["number_of_articles"],
                                    dayDictionary[day]["daily_change"], True)
            i += 1
        return neural_network.finalTest(today["impact"], today["number_of_articles"])

    def open_headline_screen(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        enter_headline = Label(self.main_frame, text="Enter Your Headline: ")
        enter_headline.grid(row=0, column=0)

        enter_stock_entry = Entry(self.main_frame, textvariable=self.headline)
        enter_stock_entry.grid(row=0, column=1)

        enter_stock_label = Label(self.main_frame, text="Enter Stock Ticker: ")
        enter_stock_label.grid(row=1, column=0)

        enter_stock_entry = Entry(self.main_frame, textvariable=self.stock_ticker)
        enter_stock_entry.grid(row=1, column=1)

        back_button = Button(self.main_frame, text="Back")
        back_button.bind("<Button-1>", self.open_main_menu)
        back_button.grid(row=2, column=0)

        calculate_headline_button = Button(self.main_frame, text="Enter")
        calculate_headline_button.bind("<Button-1>", self.open_headline_prediction)
        calculate_headline_button.grid(row=2, column=1)

    def open_headline_prediction(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        try:
            self.stock_ticker.set(self.stock_ticker.get().upper())
            stockInput = self.stock_ticker.get()
            stockInfoDict = data.getInfoDict(stockInput)
            dataCollection = datainterpretation.KeywordCollection(stockInfoDict)

            words_of_headline = self.headline.get().split()
            headline_impact = 0
            for word in words_of_headline:
                for keyword in dataCollection.getKeywords():
                    if word.lower() == keyword.getWord():
                        headline_impact += keyword.getImpact()

            prediction_string = "Your headline will "
            if headline_impact > 0.1:
                prediction_string += "drastically increase the value of " + self.stock_ticker.get() + "."
            elif headline_impact > 0.02:
                prediction_string += "moderately increase the value of " + self.stock_ticker.get() + "."
            elif headline_impact > -0.02:
                prediction_string += "not greatly affect the value of " + self.stock_ticker.get() + "."
            elif headline_impact > -0.1:
                prediction_string += "moderately decrease the value of " + self.stock_ticker.get() + "."
            else:
                prediction_string += "drastically decrease the value of " + self.stock_ticker.get() + "."

            prediction_label = Label(self.main_frame, text=prediction_string)
            prediction_label.grid(row=0, column=0, columnspan=2)

            back_to_menu_button = Button(self.main_frame, text="Back to Menu")
            back_to_menu_button.bind("<Button-1>", self.open_main_menu)
            back_to_menu_button.grid(row=1, column=0)

            new_headline_button = Button(self.main_frame, text="Try Another Headline")
            new_headline_button.bind("<Button-1>", self.open_headline_screen)
            new_headline_button.grid(row=1, column=1)
        except:
            self.stock_ticker = StringVar()
            self.open_headline_screen()

    def open_word_screen(self, event=None):
        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        enter_stock_label = Label(self.main_frame, text="Enter Stock Ticker: ")
        enter_stock_label.grid(row=0, column=0)

        enter_stock_entry = Entry(self.main_frame, textvariable=self.stock_ticker)
        enter_stock_entry.grid(row=0, column=1)

        back_button = Button(self.main_frame, text="Back")
        back_button.bind("<Button-1>", self.open_main_menu)
        back_button.grid(row=1, column=0)

        calculate_headline_button = Button(self.main_frame, text="Enter")
        calculate_headline_button.bind("<Button-1>", self.open_words_list)
        calculate_headline_button.grid(row=1, column=1)

    def open_words_list(self, event=None):
        try:
            self.stock_ticker.set(self.stock_ticker.get().upper())
            stockInput = self.stock_ticker.get()
            stockInfoDict = data.getInfoDict(stockInput)
            dataCollection = datainterpretation.KeywordCollection(stockInfoDict)

            top_five_positive

            for keyword in dataCollection.getKeywords():
                if word.lower() == keyword.getWord():
                    headline_impact += keyword.getImpact()



            prediction_label = Label(self.main_frame, text=prediction_string)
            prediction_label.grid(row=0, column=0, columnspan=2)

            back_to_menu_button = Button(self.main_frame, text="Back to Menu")
            back_to_menu_button.bind("<Button-1>", self.open_main_menu)
            back_to_menu_button.grid(row=1, column=0)

            new_headline_button = Button(self.main_frame, text="Try Another Headline")
            new_headline_button.bind("<Button-1>", self.open_headline_screen)
            new_headline_button.grid(row=1, column=1)
        except:
            self.stock_ticker = StringVar()
            self.open_headline_screen()

root = Tk()
main = gui()
root.resizable(0, 0)
root.mainloop()
