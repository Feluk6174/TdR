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
import random
from datetime import datetime
from kivy.graphics import BorderImage
from kivy.lang import Builder

import api, register_screen, user_image_register_screen, profile_screen, home_screen, chat_screen, search_screen, create_post_screen, user_image_screen

#optional. errase when doing apk
Window.size = (500, 750)

connection = api.Connection()


class MyApp (App):
    def build(self):

        #set basis. screen manager and connection
        global connection
        sm = ScreenManager()

        #look if user created and if it is registered. if it does not, make it
        check_info = register_screen.check_my_info_exists()
        if check_info == False:
            sm.add_widget(register_screen.RegisterScreen(connection, name = "register"))
            sm.add_widget(user_image_register_screen.ImageScreen(connection, name = "image_register"))
        elif check_info == True:
            check_register = register_screen.check_my_info_exists(connection)
            if check_register == False:
                register_screen.register(connection)
            #make screens of app
            my_profile_screen = profile_screen.ProfileScreen(connection, name = "profile")
            sm.add_widget(home_screen.MainScreen(connection, name = "main"))
            sm.add_widget(chat_screen.ChatScreen(connection, name = "chat"))
            sm.add_widget(search_screen.SearchScreen(connection, name = "search"))
            sm.add_widget(create_post_screen.PostUserScreen(connection, name = "last"))
            sm.add_widget(my_profile_screen)
            sm.add_widget(user_image_screen.ImageScreen(my_profile_screen, name = "image"))
        return sm



if __name__ == "__main__":
    MyApp().run()


#make image of register repeat password and 2 (when wrong)
#improve buttons to other screens
#alarm symbol in chat button on ground box of other screens
#refresh def in all screens

#order posts
#functions clicking posts



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