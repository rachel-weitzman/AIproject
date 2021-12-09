"""
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'resizable', True)


class YourApp(App):
    def build(self):
        layout = FloatLayout()
        next_page = Button(text='next page',
                           size_hint=(.2, .2),
                           pos=(600,50),
                           background_color='red')


        layout.add_widget(next_page)

        return layout


YourApp().run()
