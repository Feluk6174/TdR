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

import chat_screen, home_screen, loading_screen, post_screen, profile_screen, search_screen

Window.size = (400, 600)

class MyApp (App):
    def build(self):
        sm = ScreenManager(transition = FallOutTransition())
        sm.add_widget(loading_screen.LoadScreen(name = "load"))
        sm.transition = SlideTransition()
        sm.add_widget(home_screen.MainScreen(name = "main"))
        sm.add_widget(chat_screen.ChatScreen(name = "chat"))
        sm.add_widget(search_screen.SearchScreen(name = "search"))
        sm.add_widget(post_screen.PostUserScreen(name = "last"))
        sm.add_widget(profile_screen.ProfileScreen(name = "profile"))
        return sm

if __name__ == "__main__":
    MyApp().run()




#random anchor down right float