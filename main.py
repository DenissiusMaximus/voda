from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode','systemanddock')


class MainWidget(BoxLayout):
    def calc(self):
        calc = int(self.input.text) * 1.2
        calc = round(calc)
        self.res.text = str(calc) + " грн"

    def repl12(self):
        self.input.text = '12'
        calc = int(self.input.text) * 1.2
        calc = round(calc)
        self.res.text = str(calc) + " грн"

    def repl14(self):
        self.input.text = '14'
        calc = int(self.input.text) * 1.2
        calc = round(calc)
        self.res.text = str(calc) + " грн"

    def repl13(self):
        self.input.text = '13'
        calc = int(self.input.text) * 1.2
        calc = round(calc)
        self.res.text = str(calc) + " грн"

    def repl19(self):
        self.input.text = '19'
        calc = int(self.input.text) * 1.2
        calc = round(calc)
        self.res.text = str(calc) + " грн"




class MainApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MainApp().run()