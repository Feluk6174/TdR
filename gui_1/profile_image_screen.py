#import kivy 
from kivy.app import App
from functools import partial
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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
import kivy.utils
from datetime import datetime
import acces_my_info
import api

class ImageScreen (Screen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)

        self.box0 = BoxLayout(orientation = "vertical")
        self.add_widget(self.box0)

        self.box01 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box01)

        self.box2 = BoxLayout()
        self.box01.add_widget(self.box2)

        self.box1 = GridLayout(cols = 8, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box01.add_widget(self.box1)

        self.color_list = []
        for x in range (64):
            self.color_list.append("0")

        for _ in range (64):
            self.btn = Button(background_normal = '', background_color = (0, 0, 0, 0), on_press = self.button_1)
            self.box1.add_widget(self.btn)

        self.box3 = BoxLayout()
        self.box01.add_widget(self.box3)

    
        self.box02 = BoxLayout()
        self.box0.add_widget(self.box02)


        self.box03 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box03)

        self.box4 = BoxLayout()
        self.box03.add_widget(self.box4)

        self.box5 = GridLayout(cols = 4, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box03.add_widget(self.box5)

        self.all_colors = [("0", '#000000'), ("1", '#7e7e7e'), ("2", '#bebebe'), ("3", '#ffffff'), ("4", '#7e0000'), ("5", '#fe0000'), ("6", '#047e00'), ("7", '#06ff04'), ("8", '#7e7e00'), ("9", '#ffff04'), ("A", '#00007e'), ("B", '#0000ff'), ("C", '#7e007e'), ("D", '#fe00ff'), ("E", '#047e7e'), ("F", '#06ffff')]

        for x in range (len(self.all_colors)):
            self.btn1 = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(self.all_colors[x][1]), on_press = self.button_2)
            self.box5.add_widget(self.btn1)

        self.box6 = BoxLayout()
        self.box03.add_widget(self.box6)

        self.actual_btn1 = self.btn
        self.actual_btn2 = self.btn1

    def button_1(self, instance):
        instance.background_color = (0, 0, 0, 1)
        self.actual_btn1 = instance

    def button_2(self, instance):
        self.actual_btn2 = instance
