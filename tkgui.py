from tkinter import *
import datainterpretation
import data
import hackathonann

class gui(Frame):
    def __init__(self):
        super().__init__(root)
        self.winfo_toplevel().title("StockPredict")
        self.main_frame = Frame(root)
        self.open_main_menu()

        # open_stock_screen variables
        self.stock_ticker = StringVar()

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

        headline_screen_button = Button(self.main_frame, text="Predict Stock Change")
        headline_screen_button.bind("<Button-1>", self.open_headline_screen)
        headline_screen_button.grid(row=1, column=1)

        word_screen_button = Button(self.main_frame, text="Predict Stock Change")
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

        loading_label = Label(self.main_frame, text="Calculating...\n(This may take a few seconds.)")
        loading_label.grid(row=0, column=0)

        prediction_number = self.get_prediction()
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

        self.main_frame.destroy()
        self.main_frame = Frame(root)
        self.main_frame.grid()

        prediction_label = Label(self.main_frame, text=prediction_string, )


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
        pass

    def open_word_screen(self, event=None):
        pass


root = Tk()
main = gui()
root.resizable(0, 0)
root.mainloop()
