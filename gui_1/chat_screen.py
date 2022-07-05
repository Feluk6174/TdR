#import kivy
from kivy.app import App
from functools import partial
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivy.clock import Clock
from kivy.uix.screenmanager import FallOutTransition
from kivy.uix.screenmanager import SlideTransition

def get_post_text(num):
    return str(num)

class ChatScreen (Screen):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        self.lab1.bind(on_release = self.press_btn13)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        for a in range (20):
            self.btn = Button (size_hint_y = None, height = 80, text = "A" + (get_post_text(a)))
            self.grid.add_widget(self.btn)

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box3)

        self.btn11 = Label (text = ("Chat"))
        self.box3.add_widget(self.btn11)

        self.btn12 = Button (text = ("S"))
        self.box3.add_widget(self.btn12)
        self.btn12.bind(on_press = self.press_btn12)

        self.btn13 = Button (text = ("H"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

        self.btn14 = Button (text = ("P"))
        self.box3.add_widget(self.btn14)
        self.btn14.bind(on_press = self.press_btn14)

        self.btn15 = Button (text = ("U"))
        self.box3.add_widget(self.btn15)
        self.btn15.bind(on_press = self.press_btn15)

        
    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass

    def press_btn11(self, instance):
        pass

    def press_btn12(self, instance):
        self.manager.current = "search"
        self.manager.transition.direction = "left"

    def press_btn13(self, instance):
        self.manager.current = "main"
        self.manager.transition.direction = "left"

    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"
