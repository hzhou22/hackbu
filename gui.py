import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class predictButton(Button):
    def __init__(self):
        super(predictButton, self).__init__()

        self.bind(on_press=self.clicked)

    def clicked(self, obj):
        print("Hello potato")


class StockPredictorApp(App):

    def build(self):
        return BoxLayout()


stock_predictor = StockPredictorApp()

stock_predictor.run()
