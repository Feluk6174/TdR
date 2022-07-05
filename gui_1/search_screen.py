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

class SearchScreen (Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.box2.add_widget(self.grid)

        self.lab1 = TextInput(multiline = False, text = "Search post")
        self.grid.add_widget(self.lab1)
        self.lab1.bind(on_text_validate = self.search11)

        self.lab2 = TextInput(multiline = False, text = "Search user")
        self.grid.add_widget(self.lab2)
        self.lab2.bind(on_text_validate = self.search12)

        self.lab3 = TextInput(multiline = False, text = "Search hastag")
        self.grid.add_widget(self.lab3)
        self.lab2.bind(on_text_validate = self.search13)

        self.ran0 = Button (text = "Favourites", size_hint = (1, 1))
        self.grid.add_widget(self.ran0)
        self.ran0.bind(on_press = self.random0)

        self.ran1 = Button (text = "Global", size_hint = (1, 2.5))
        self.grid.add_widget(self.ran1)
        self.ran1.bind(on_press = self.random1)

        self.ran2 = Button (text = "Random", size_hint = (1, 1))
        self.grid.add_widget(self.ran2)
        self.ran2.bind(on_press = self.random2)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box3)

        self.btn11 = Button (text = ("C"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Label (text = ("Search"))
        self.box3.add_widget(self.btn12)
        
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

    def search11(instance, value):
        pass

    def search12(instance, value):
        pass

    def search13(instance, value):
        pass

    def random0(self, instance):
        pass

    def random1(self, instance):
        pass

    def random2(self, instance):
        pass

    def press_btn11(self, instance):
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        pass

    def press_btn13(self, instance):
        self.manager.current = "main"
        self.manager.transition.direction = "left"


    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"