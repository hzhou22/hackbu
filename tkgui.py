from tkinter import *


class gui(Frame):
    def __init__(self):
        super().__init__(root)
        self.winfo_toplevel().title("StockPredict")
        self.main_frame = Frame(root)
        self.open_main_menu()

        # open_stock_screen variables
        self.stock_ticker = ""

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


    def open_headline_screen(self, event=None):
        pass

    def open_word_screen(self, event=None):
        pass


root = Tk()
main = gui()
root.mainloop()
root.resizable(0, 0)
