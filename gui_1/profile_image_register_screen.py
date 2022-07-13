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
import register_screen
import profile_screen

my_colors_from_screen = ""

def get_my_image():
    global my_colors_from_screen
    return my_colors_from_screen

class ImageScreen (Screen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)

        self.box0 = BoxLayout(orientation = "vertical")
        self.add_widget(self.box0)

        self.box01 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box01)

        self.box2 = BoxLayout()
        self.box01.add_widget(self.box2)

        self.box1 = GridLayout(spacing = 5, cols = 8, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box01.add_widget(self.box1)

        self.color_list = []
        for x in range (64):
            self.color_list.append("3")

        for y in range (64):
            self.btn = Button(background_normal = '', font_size = 1, text = str(y), background_color = (1, 1, 1, 1), on_press = self.button_1)
            self.box1.add_widget(self.btn)

        self.box3 = BoxLayout()
        self.box01.add_widget(self.box3)

    
        self.box02 = BoxLayout()
        self.box0.add_widget(self.box02)

        self.return_to_back = Button(text = "Done", on_release = self.go_back)
        self.box02.add_widget(self.return_to_back)


        self.box03 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box03)

        self.box4 = BoxLayout()
        self.box03.add_widget(self.box4)

        self.box5 = GridLayout(cols = 4, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box03.add_widget(self.box5)

        self.all_colors = [("0", '#1B1A1A'), ("1", '#7e7e7e'), ("2", '#bebebe'), ("3", '#ffffff'), ("4", '#7e0000'), ("5", '#fe0000'), ("6", '#047e00'), ("7", '#06ff04'), ("8", '#7e7e00'), ("9", '#ffff04'), ("A", '#00007e'), ("B", '#0000ff'), ("C", '#7e007e'), ("D", '#fe00ff'), ("E", '#047e7e'), ("F", '#06ffff')]

        for x in range (len(self.all_colors)):
            self.btn1 = Button(border = (0, 0, 0, 0), background_normal = '', font_size = 1, text = str(x), background_color = kivy.utils.get_color_from_hex(self.all_colors[x][1]), on_press = self.button_2)
            self.box5.add_widget(self.btn1)

        self.box6 = BoxLayout()
        self.box03.add_widget(self.box6)

        self.actual_btn1 = self.btn
        self.actual_btn2 = self.btn1
    
    def go_back(self, instance):
        col_str = ""
        for a in range (len(self.color_list)):
            col_str = col_str + self.color_list[a]
        check = register_screen.check_register()
        if check == True:
            acces_my_info.change_my_color(col_str)
            #profile_screen.BuildImage(profile_screen, col_str)
            self.manager.transition = FallOutTransition()
            self.manager.current = "profile"

        elif check == False:
            global my_colors_from_screen 
            my_colors_from_screen= col_str
            self.manager.transition = FallOutTransition()
            self.manager.current = "register"

    def button_1(self, instance):
        instance.background_color = self.actual_btn2.background_color
        self.color_list[int(instance.text)] = self.all_colors[int(self.actual_btn2.text)][0]
        self.actual_btn1 = instance

    def button_2(self, instance):
        self.actual_btn2.background_normal = ""
        instance.background_normal = "check_verd.png"
        self.actual_btn2 = instance