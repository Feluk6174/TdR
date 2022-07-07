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

class LoadScreen (Screen):
    def __init__(self, **kwargs):
        super(LoadScreen, self).__init__(**kwargs)
        self.box0 = BoxLayout(orientation = "vertical")
        self.add_widget(self.box0)

        self.black_box_1 = BoxLayout(size_hint_y = None, height = (Window.size[0] * 0.2))
        self.box0.add_widget(self.black_box_1)

        self.Lab1 = Button(size_hint = (None, None), background_normal = 'logo.png', background_down = 'logo.png', size = (Window.size[0] * 0.7, Window.size[0] * 0.7), pos_hint = {"center_x":0.5})   
        self.box0.add_widget(self.Lab1)
        self.Lab1.bind(on_press = self.change)

        self.lab2 = Label(text = "Small Brother", size_hint = (1, 0.12))
        self.box0.add_widget(self.lab2)

        Clock.schedule_once(self.change, 3)

        
    def change(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "main"
