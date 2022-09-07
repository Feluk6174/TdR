#import kivy
from multiprocessing import connection
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
import home_screen, access_my_info
from datetime import datetime

import search_screen, functions, profile_screen


class ChatScreen (Screen):
    def __init__(self, connection, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)

        self.connection = connection

        self.main_all_box = BoxLayout(orientation = "vertical")
        self.add_widget(self.main_all_box)

        self.header_box = BoxLayout (size_hint = (1, 0.1))
        self.main_all_box.add_widget(self.header_box)

        self.logo = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/logo.png', background_down = 'images/logo.png', on_release = self.press_home_btn)
        self.header_box.add_widget(self.logo)
        
        self.header_text = Label(text = "Small brother", size_hint = (2, 1))
        self.header_box.add_widget(self.header_text)
        
        self.header_btn = Button(border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/settings1.png', background_down = 'images/settings2.png')
        self.header_box.add_widget(self.header_btn)
        self.header_btn.bind(on_release = self.header_btn_press)
        

        self.float_content_layout = FloatLayout()
        self.main_all_box.add_widget(self.float_content_layout)

        self.content_box = BoxLayout (pos_hint = {"x" : 0, "y" : 0})
        self.float_content_layout.add_widget(self.content_box)
        
        self.content_grid = GridLayout(cols = 1, size_hint_y = None)
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))

        self.content_grid_scroll = ScrollView ()
        self.content_grid_scroll.add_widget (self.content_grid)
        self.content_box.add_widget (self.content_grid_scroll)

        #create_chats()
        #self.refresh_messages()

        #desplegable para configurar la búsqueda
        self.random_chat_btn = Button (border = (0, 0, 0, 0), background_normal = 'images/dice1.png', size_hint = (None, None), height = Window.size[0] * 0.2, width = Window.size[0] * 0.2, pos_hint = {"x" : 0.75, "y" : 0.035})
        self.float_content_layout.add_widget(self.random_chat_btn)
        self.random_chat_btn.bind(on_release = self.random_chat_press)


        self.ground_box = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.main_all_box.add_widget(self.ground_box)

        self.chat_label = Label (text = ("Chat"))
        self.ground_box.add_widget(self.chat_label)

        self.search_btn = Button (text = ("S"))
        self.ground_box.add_widget(self.search_btn)
        self.search_btn.bind(on_release = self.press_search_btn)

        self.home_btn = Button (text = ("H"))
        self.ground_box.add_widget(self.home_btn)
        self.home_btn.bind(on_release = self.press_home_btn)

        self.make_posts_btn = Button (text = ("P"))
        self.ground_box.add_widget(self.make_posts_btn)
        self.make_posts_btn.bind(on_release = self.press_make_posts_btn)

        self.user_profile_btn = Button (text = ("U"))
        self.ground_box.add_widget(self.user_profile_btn)
        self.user_profile_btn.bind(on_release = self.press_user_profile_btn)


    def generate_chats(self):
        #last_time_stamp = access_my_info.get_last_time_stamp()
        conn = self.connection
        self.displayed_chat_list = []
        chat_list = access_my_info.get_new_chats(conn, (0, 20))
        #gotta get last timestamp, ask api for new messages and change stored timestamp
        for a in range (len(chat_list)):
            #functions.create_chat(chat_list{a}, a)
            self.chat_btn = self.create_chat(chat_list[a], a)
            self.content_grid.add_widget(self.chat_btn)
            self.displayed_chat_list.append([chat_list[a]["chat_name"], self.chat_btn])
            #info in chat (diccionari): "type" = chat (0) or group (1), "users" = list by alfabetic order (start with you??) (another list. 0 name 1 role in the group), "id" (get from hash of members, timestamp an rnd number?), "chat_name"(only if group) = nom del xat per l'usuari, "image" = ...(if a group), "alert" = 0 (no) or 1 (yes)
            #les claus dels chats estan en un altre document i les aconseguim per la id del chat

    def create_chat(self, chat_info, order_number):
        conn = self.connection

        self.chat_btn = BoxLayout(orientation = 'horizontal', size_hint_y = None, height = Window.size[0] / 1.61 / 2)


        if chat_info["type"] == 0:
            user_info = conn.get_user(chat_info["users"][0])
            self.image_grid = functions.build_image(self, user_info["profile_picture"], order_number, Window.size[0] / 1.61 / 2)
        
        elif chat_info["type"] == 1:
            self.image_grid = functions.build_image(self, chat_info["image"], order_number, Window.size[0] / 1.61 / 2)
        
        self.chat_btn.add_widget(self.image_grid)


        self.middle_box = BoxLayout(orientation = 'vertical')
        self.chat_btn.add_widget(self.middle_box)

        if chat_info["type"] == 0:
            self.chat_name_btn = Button(text = chat_info["users"][0], on_release = partial(self.chat_press, order_number))
        
        elif chat_info["type"] == 1:
            self.chat_name_btn = Button(text = chat_info["chat_name"], on_release = partial(self.chat_press, order_number))
        
        self.middle_box.add_widget(self.chat_name_btn)

        if chat_info["type"] == 0:
            last_message = access_my_info.message_from_chat(chat_info["users"][0], 0)
            self.last_message_btn = Button(text = last_message, on_release = partial(self.chat_press, order_number))

        elif chat_info["type"] == 1:
            last_message = access_my_info.message_from_chat(chat_info["chat_name"], 0)
            self.last_message_btn = Button(text = last_message, on_release = partial(self.chat_press, order_number))

        self.middle_box.add_widget(self.last_message_btn)

        if chat_info["alert"] == 1:
            self.alert_btn = Button(on_release = partial(self.chat_press, order_number), size_hint_x = None, width = Window.size[0] / 1.61 / 3, border = (0, 0, 0, 0), background_normal = 'images/logo.png')
            self.chat_btn.add_widget(self.alert_btn)

    def chat_press(self, order_number):
        pass

    def image_press(self, order_number):
        self.chat_press(order_number)

    def refresh_messages(self):
        pass
    
    def header_btn_press(self, instance):
        pass

    def random_chat_press(self, instance):
        pass

    #def press_chat_btn(self, instance):
        #pass

    def press_search_btn(self, instance):
        search_scrn = self.search_screen
        search_screen.refresh_search_screen(search_scrn)
        self.manager.transition = SlideTransition()
        self.manager.current = "search"
        self.manager.transition.direction = "left"

    def press_home_btn(self, instance):
        home_scrn = self.home_screen
        home_screen.get_my_posts(home_scrn)
        self.manager.transition = SlideTransition()
        self.manager.current = "home"
        self.manager.transition.direction = "left"

    def press_make_posts_btn(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "create"
        self.manager.transition.direction = "left"

    def press_user_profile_btn(self, instance):
        profile_scrn = self.profile_screen
        profile_screen.refresh_profile_screen(profile_scrn)
        self.manager.transition = SlideTransition()
        self.manager.transition = SlideTransition()
        self.manager.current = "profile"
        self.manager.transition.direction = "left"

    def add_screens(self, home_screen, profile_screen, search_screen, other_profile_screen):
        self.home_screen = home_screen
        self.profile_screen = profile_screen
        self.search_screen = search_screen
        self.other_profile_screen = other_profile_screen
