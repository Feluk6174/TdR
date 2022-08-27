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

import chat_screen, search_screen, profile_screen, functions, access_my_info


class MainScreen (Screen):
    def __init__(self, conn, my_profile_screen, my_search_screen, my_chat_screen, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.chat_screen = my_chat_screen
        self.profile_screen = my_profile_screen
        self.search_screen = my_search_screen

        self.chat_screen.add_screens(self, self.profile_screen, self.search_screen)
        self.profile_screen.add_screens(self, self.chat_screen, self.search_screen)
        self.search_screen.add_screens(self, self.profile_screen, self.chat_screen)

        self.connection = conn

        self.main_all_box = BoxLayout(orientation = "vertical")
        self.add_widget(self.main_all_box)

        self.header_box = BoxLayout (size_hint = (1, 0.1))
        self.main_all_box.add_widget(self.header_box)

        self.logo = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/logo.png', background_down = 'images/logo.png', on_release = self.get_my_posts)
        self.header_box.add_widget(self.logo)
        
        self.header_text = Label(text = "Small brother", size_hint = (2, 1))
        self.header_box.add_widget(self.header_text)
        
        self.header_btn = Button(border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/settings1.png', background_down = 'images/settings2.png')
        self.header_box.add_widget(self.header_btn)
        self.header_btn.bind(on_release = self.header_btn_press)
        
        
        self.content_box = BoxLayout (size_hint = (1, 0.9))
        self.main_all_box.add_widget(self.content_box)
        
        self.posts_grid = GridLayout(cols = 1, size_hint_y = None, spacing = 3)
        self.posts_grid.bind(minimum_height=self.posts_grid.setter('height'))
        
        self.posts_grid_scroll = ScrollView()
        self.posts_grid_scroll.add_widget (self.posts_grid)
        self.content_box.add_widget (self.posts_grid_scroll)

        #self.post_btn_test = Button(size_hint_y = None, height = 100, text = "Refresh Posts", on_release = self.get_my_posts)
        #self.posts_grid.add_widget(self.post_btn_test)

        self.posts_box = BoxLayout(orientation = "vertical", size_hint_y = None, height = 100)
        self.posts_grid.add_widget(self.posts_box)

        self.all_posts_i_get = []
        self.get_my_posts(0)


        self.ground_box = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.main_all_box.add_widget(self.ground_box)

        self.chat_btn = Button (text = ("C"))
        self.ground_box.add_widget(self.chat_btn)
        self.chat_btn.bind(on_release = self.press_chat_btn)

        self.search_btn = Button (text = ("S"))
        self.ground_box.add_widget(self.search_btn)
        self.search_btn.bind(on_release = self.press_search_btn)

        self.home_label = Label (text = ("Home"))
        self.ground_box.add_widget(self.home_label)

        self.make_posts_btn = Button (text = ("P"))
        self.ground_box.add_widget(self.make_posts_btn)
        self.make_posts_btn.bind(on_release = self.press_make_posts_btn)

        self.user_profile_btn = Button (text = ("U"))
        self.ground_box.add_widget(self.user_profile_btn)
        self.user_profile_btn.bind(on_release = self.press_user_profile_btn)
        

    def header_btn_press(self, instance):
        pass

    def press_chat_btn(self, instance):
        chat_scrn = self.chat_screen
        chat_screen.generate_chats(chat_scrn)
        self.manager.transition = SlideTransition()
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_search_btn(self, instance):
        search_scrn = self.search_screen
        search_screen.refresh_search_screen(search_scrn)
        self.manager.transition = SlideTransition()
        self.manager.current = "search"
        self.manager.transition.direction = "right"

    #def press_home_btn(self, instance):
    #    mainscreen.get_my_posts(0)

    def press_make_posts_btn(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_user_profile_btn(self, instance):
        profile_scrn = self.profile_screen
        profile_screen.refresh_profile_screen(profile_scrn)
        self.manager.transition = SlideTransition()
        self.manager.current = "profile"
        self.manager.transition.direction = "left"

    def get_my_posts(self, instance):
        self.all_posts_i_get = []
        self.posts_box.clear_widgets()
        self.posts_grid.remove_widget(self.posts_box)
        self.all_posts_info = self.get_new_follower_posts(self.connection)
        self.all_posts_info = functions.order_posts_by_timestamp(self.all_posts_info)
        self.posts_box = BoxLayout(orientation = "vertical", size_hint_y = None, height = Window.size[0] / 1.61 * (len(self.all_posts_info)))
        self.posts_grid.add_widget(self.posts_box)
        for p in range(len(self.all_posts_info)):
            self.post_btn = functions.make_post_btn(self.all_posts_info[p][0], self.all_posts_info[p][1], self.all_posts_info[p][2], self.all_posts_info[p][3], self.all_posts_info[p][4], self.all_posts_info[p][5], self.all_posts_info[p][6], self.all_posts_info[p][7], p)
            self.posts_box.add_widget(self.post_btn)
            self.all_posts_i_get.append((self.all_posts_info[p][6], self.post_btn, self.all_posts_info[p][7]))
        self.posts_grid.bind(minimum_height=self.posts_grid.setter('height'))

    def get_new_follower_posts(self, connection):
        all_my_following = access_my_info.get_following_users()
        my_liked_posts = access_my_info.get_liked_posts_id()
        all_posts = []
        for following in all_my_following:
            follower_posts = connection.get_user_posts(following)
            follower_info = connection.get_user(following)
            #0 none, 1 yes, 
            for post in follower_posts:
                for liked in my_liked_posts:
                        if liked == post["id"]:
                            actual_maybe_like = 1
            all_posts.append((following, follower_info["profile_picture"], post["flags"], post["content"], post["likes"], post["time_posted"],post["id"], actual_maybe_like))
        return all_posts
        
    def name_press(self, order_number,instance):
        #go to user screen (owner of post)
        pass

    def image_press(self, order_number, instance):
        #go to user screen (owner of post)
        pass

    def content_post_press(self, order_number, instance):
        #copy post (mantain pressed)
        pass

    def like_press(self, order_number, instance):
        num = self.all_posts_i_get[order_number][2]
        num = (num + 1) % 2
        if num == 1:
            instance.background_normal = 'images/heart2.png'
            access_my_info.add_liked_or_unliked_post(self.all_posts_i_get[order_number][0], 1)
        if num == 0:
            instance.background_normal = 'images/heart.png'
            access_my_info.add_liked_or_unliked_post(self.all_posts_i_get[order_number][0], 0)
        self.all_posts_i_get[order_number][2] = num