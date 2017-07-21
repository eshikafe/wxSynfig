import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class BeaverApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    BeaverApp().run()