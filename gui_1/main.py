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

import chat_screen, home_screen, loading_screen, post_screen, profile_screen, search_screen

#Window.size = (540*0.7, 880*0.7)

my_user_info = json.loads(open("my_info.json", "r").read())
username = my_user_info["user_name"]
profileimage = my_user_info["profile_image"]
user_pub_key = my_user_info["user_pub_key"]
user_priv_key = my_user_info["user_priv_key"]

def GetName():
    return username
def GetImage():
    return profileimage
def GetPubKey():
    return user_pub_key
def GetPrivKey():
    return user_priv_key


class MyApp (App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(loading_screen.LoadScreen(name = "load"))
        sm.add_widget(home_screen.MainScreen(name = "main"))
        sm.add_widget(chat_screen.ChatScreen(name = "chat"))
        sm.add_widget(search_screen.SearchScreen(name = "search"))
        sm.add_widget(post_screen.PostUserScreen(name = "last"))
        sm.add_widget(profile_screen.ProfileScreen(name = "profile"))
        return sm

if __name__ == "__main__":
    MyApp().run()



