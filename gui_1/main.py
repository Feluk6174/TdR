import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
import random
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.properties import StringProperty
from kivy.lang import Builder



def get_text(a):
    return str(random.randint(0, a+1))


class MainWidget (BoxLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.orientation = "vertical"
        


        self.box1 = BoxLayout (size_hint = (1, 0.12))
        self.add_widget(self.box1)

        self.lab1 = Label (text = ("Small Brother"), size_hint = (3, 1))
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1))
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        


        self.box2 = BoxLayout (size_hint = (1, 1))
        self.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        for a in range (20):
            self.btn = Button (size_hint_y = None, height = 100, text = (get_text(a)))
            self.grid.add_widget(self.btn)

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)
        
        



        self.box3 = BoxLayout (size_hint = (1, 0.12))
        self.add_widget(self.box3)

        self.btn11 = Button (text = ("A"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Button (text = ("B"))
        self.box3.add_widget(self.btn12)
        self.btn12.bind(on_press = self.press_btn12)

        self.btn13 = Button (text = ("C"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

        self.btn14 = Button (text = ("D"))
        self.box3.add_widget(self.btn14)
        self.btn14.bind(on_press = self.press_btn14)

        self.btn15 = Button (text = ("E"))
        self.box3.add_widget(self.btn15)
        self.btn15.bind(on_press = self.press_btn15)

        

    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass
    

    def press_btn11(self, instance):
        pass

    def press_btn12(self, instance):
        pass

    def press_btn13(self, instance):
        pass

    def press_btn14(self, instance):
        pass

    def press_btn15(self, instance):
        pass













class MyApp (App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()
