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
import kivy.utils
import json
import register_screen

import chat_screen, home_screen, loading_screen, post_screen, profile_screen, search_screen, acces_my_info, register_screen, profile_image_screen, api

Window.size = (540*0.7, 880*0.7)
connection = api.Connection()

class BlackScreen (Screen):
    def __init__(self, **kwargs):
        super(BlackScreen, self).__init__(**kwargs)
        pass

class MyApp (App):
    def build(self):
        global connection
        sm = ScreenManager()
        check = register_screen.check_register()
        if check == True:
            #pass
            register_screen.Reg_f(connection)
            #sm.add_widget(loading_screen.LoadScreen(name = "load"))
            sm.add_widget(home_screen.MainScreen(connection, name = "main"))
            sm.add_widget(chat_screen.ChatScreen(name = "chat"))
            sm.add_widget(search_screen.SearchScreen(name = "search"))
            sm.add_widget(post_screen.PostUserScreen(connection, name = "last"))
            sm.add_widget(profile_screen.ProfileScreen(name = "profile"))
            sm.add_widget(profile_image_screen.ImageScreen(name = "image"))
        elif check == False:
            sm.add_widget(register_screen.RegisterScreen(connection, name = "register"))
            sm.add_widget(profile_image_screen.ImageScreen(name = "image"))
            sm.add_widget(BlackScreen(name = "close_register"))
        return sm

if __name__ == "__main__":
    try:
        MyApp().run()
    except ZeroDivisionError:
        MyApp().run()