from kivy.app import App
from  kivy.uix.label import Label

class App(App):
    def build(self):
        return Label(text='Hello, I am michael')

App().run()