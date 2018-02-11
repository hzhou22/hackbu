import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget


class ButtonPanel(Widget):
    pass


class StockPredictorApp(App):

    def build(self):
        return ButtonPanel()


stock_predictor = StockPredictorApp()

stock_predictor.run()
