import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class StockPredictorApp(App):

    def build(self):
        return GridLayout()

stock_predictor = StockPredictorApp()

stock_predictor.run()
