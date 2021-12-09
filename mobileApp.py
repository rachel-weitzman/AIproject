

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.popup import Popup


Config.set('graphics', 'resizable', True)


class YourApp(App):
    def build(self,color='red'):
        layout = FloatLayout()
        next_page = Button(text='next page',
                           size_hint=(.2, .2),
                           pos=(600,50),
                           background_color=color)
        #mic=open("microphone.png")
        record = Button(background_normal = 'microphone.png',
                        background_down='white',
                        size_hint=(.2, .2),
                        pos=(300,50),
                        press_on=show())
        layout.add_widget(next_page)
        layout.add_widget(record)

        #next_page.bind(on_press=self.nextPage())

        return layout



class P(FloatLayout):
    pass

class A(FloatLayout):
    pass

def show():
    show=P()
    popupWindow=Popup(content=show)
    popupWindow.open()


class kvfileApp(App):
    def build(self):
        return P()

kv = kvfileApp()
kv.run()

#YourApp().run()



