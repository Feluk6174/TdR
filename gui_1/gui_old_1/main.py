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
import random
from datetime import datetime

import chat_screen, home_screen, loading_screen, post_screen, profile_screen, search_screen, acces_my_info, register_screen, profile_image_screen, api, profile_image_register_screen

Window.size = (540*0.7, 880*0.7)
connection = api.Connection()


class MyApp (App):
    def build(self):
        global connection
        sm = ScreenManager()
        check = register_screen.check_register()
        if check == True:
            #pass
            #register_screen.Reg_f(connection)
            my_profile_screen = profile_screen.ProfileScreen(connection, name = "profile")
            
            sm.add_widget(home_screen.MainScreen(connection, name = "main"))
            sm.add_widget(chat_screen.ChatScreen(name = "chat"))
            sm.add_widget(search_screen.SearchScreen(connection, name = "search"))
            sm.add_widget(post_screen.PostUserScreen(connection, name = "last"))
            sm.add_widget(my_profile_screen)
            sm.add_widget(profile_image_screen.ImageScreen(my_profile_screen, name = "image"))
        elif check == False:
            sm.add_widget(register_screen.RegisterScreen(connection, sm, name = "register"))
            sm.add_widget(profile_image_register_screen.ImageScreen(name = "image"))
            sm.add_widget(loading_screen.LoadScreen(name = "load"))
        return sm

if __name__ == "__main__":
    MyApp().run()
    



#post_screen + structure
#likes
#flags
#chat subjects: art, programation, videogames, philosophy, politic, sport, books, 

#actualitzar pàgina al clicar el botó de desplaçament cap a allà

#search screen improve
#textbox with background text
#writing box
#string into different lines 

#password x2 + *****
#small brother label

#my_posts
#following, followers
#best + new
#reload up 
