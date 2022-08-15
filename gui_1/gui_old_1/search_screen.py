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
import acces_my_info, home_screen
from datetime import datetime

import home_screen, functions


class SearchScreen (Screen):
    def __init__(self, conn, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)

        self.connection = conn

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
        

        self.content_box = BoxLayout (size_hint = (1, 0.9))
        self.main_all_box.add_widget(self.content_box)
        
        self.content_box_scroll = ScrollView ()
        self.content_box.add_widget (self.content_box_scroll) 

        self.content_grid = GridLayout(cols = 1, size_hint_y = None)
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
        self.content_box_scroll.add_widget (self.content_grid)

        #self.lab1 = TextInput(multiline = False, text = "Search post", size_hint_y = None, height = Window.size[1] / 15)
        #self.grid.add_widget(self.lab1)
        #self.lab1.bind(on_text_validate = self.search11)

        self.search_user_input = TextInput(multiline = False, background_normal = 'images/search_user.png', size_hint_y = None, height = Window.size[1] / 15)
        self.content_grid.add_widget(self.search_user_input)
        self.search_user_input.bind(on_text_validate = self.search_user_def)

        self.search_post_hastags = TextInput(multiline = False, background_normal = 'images/search_hastag.png', size_hint_y = None, height = Window.size[1] / 15)
        self.content_grid.add_widget(self.search_post_hastags)
        self.search_post_hastags.bind(on_text_validate = self.search_hastags_def)
   
        self.flag_filter_scroll = ScrollView ()
        self.content_box.add_widget(self.flag_filter_scroll) 

        self.flag_grid = GridLayout(rowss = 1, size_hint_x = None)
        self.flag_grid.bind(minimum_width = self.flag_grid.setter('width'))
        self.flag_filter_scroll.add_widget (self.flag_grid)

        self.all_flags = [['images/check_verd.png'], ['images/red_cross.png'], ['images/age18.png'], ['images/blood.png'], ['images/fist.png'], ['images/soga.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png']]
        for d in range(len(self.all_flags) - 2):
            self.all_flags[d + 2].append(str(d + 2))
        
        for x in range (len(self.all_flags) - 2):
            self.flag_btn = Button(border = (0, 0, 0, 0), font_size = 1, size_hint_x = None, width = (Window.size[1] - Window.size[0] / 5) * 0.9 / 12, text = str(self.all_flags[x + 2][1]), on_release = self.flag_press, background_normal = self.all_flags[x + 2][0])
            self.all_flags[x + 2].append(self.flag_btn)
            self.all_flags[x + 2].append(0)
            self.flag_grid.add_widget(self.flag_btn)
        
        self.posts_display_header_box = BoxLayout(size_hint_y = None, height = Window.size[1] / 8)
        self.content_grid.add_widget(self.posts_display_header_box)

        #self.popular_posts_header = Button(text = "Popular Posts")
        #self.posts_display_header_box.add_widget(self.popular_posts_header)
        #self.popular_posts_header.bind(on_press = self.popular_posts_header_press)

        #firstposts
        #current: 1 = popular, 2 = fav
        self.current_posts = 0
        #self.quantity_popular_posts = 8
        #self.quantity_favourite_posts = 11
        #self.popular_posts_header_press(0)


        self.ground_box = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.main_all_box.add_widget(self.ground_box)

        self.chat_btn = Button (text = ("C"))
        self.ground_box.add_widget(self.chat_btn)
        self.chat_btn.bind(on_release = self.press_chat_btn)

        self.search_label = Label (text = ("Search"))
        self.ground_box.add_widget(self.search_label)

        self.home_btn = Button (text = ("H"))
        self.ground_box.add_widget(self.home_btn)
        self.home_btn.bind(on_release = self.press_home_btn)

        self.make_posts_btn = Button (text = ("P"))
        self.ground_box.add_widget(self.make_posts_btn)
        self.make_posts_btn.bind(on_release = self.press_make_posts_btn)

        self.user_profile_btn = Button (text = ("U"))
        self.ground_box.add_widget(self.user_profile_btn)
        self.user_profile_btn.bind(on_release = self.press_user_profile_btn)
        

    def header_btn_press(self, instance):
        pass
        

    def search_user_def(instance, value):
        pass


    def search_hastags_def(instance, value):
        pass

    def flag_press(self, instance):
        flag_number = int(instance.text)
        if flag_number < 4:
            self.all_flags[flag_number][3] = (self.all_flags[flag_number][3] + 1) % 2 
            if self.all_flags[flag_number][3] == 1:
                instance.background_normal = self.all_flags[flag_number][0]
            if self.all_flags[flag_number][3] == 0:
                instance.background_normal = self.all_flags[1][0]
        else:
            self.all_flags[flag_number][3] = (self.all_flags[flag_number][3] + 1) % 2
            if self.all_flags[flag_number][3] == 1:
                instance.background_normal = self.all_flags[0][0]
            if self.all_flags[flag_number][3] == 0:
                instance.background_normal = self.all_flags[flag_number][0]

    def popular_posts_header_press(self, instance):
        #connection = self.connection
        #self.all_popular_posts_info = connection.get_popular_posts(self.get_filter_flags)
        self.all_popular_posts_info = []

        if self.current_posts == 2:
            self.newest_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.newest_posts_box)
        
        if self.current_posts == 3:
            self.favourite_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.favourite_posts_box)

        self.posts_display_header_box.clear_widgets()

        self.popular_posts_header_display_label = Label(text = "Popular")
        self.posts_display_header_box.add_widget(self.popular_posts_header_display_label)

        self.new_posts_header_display_btn = Button(text = "New")
        self.posts_display_header_box.add_widget(self.new_posts_header_display_btn)
        self.new_posts_header_display_btn.bind(on_press = self.new_posts_header_press)
        
        self.favourite_posts_header_display_btn = Button (text = "Favourites")
        self.posts_display_header_box.add_widget(self.favourite_posts_header_display_btn)
        self.favourite_posts_header_display_btn.bind(on_press = self.favourite_posts_header_press)

        self.popular_posts_box = BoxLayout(size_hint_y = None, height = len(self.all_popular_posts_info) * Window.size[0] / 1.61, orientation = "vertical")
        self.content_grid.add_widget(self.popular_posts_box)

        #my posts
        self.create_popular_posts()
            
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
        self.current_posts = 1

    def new_posts_header_press(self, instance):
        #connection = self.connection
        #self.all_new_posts_info = connection.get_newest_posts(self.get_filter_flags)
        self.all_newest_posts_info = []

        if self.current_posts == 1:
            self.popular_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.popular_posts_box)
        
        if self.current_posts == 3:
            self.favourite_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.favourite_posts_box)

        self.posts_display_header_box.clear_widgets()

        self.popular_posts_header_display_btn = Button(text = "Popular")
        self.posts_display_header_box.add_widget(self.popular_posts_header_display_btn)
        self.popular_posts_header_display_btn.bind(on_press = self.popular_posts_header_press)

        self.new_posts_header_display_label = Label(text = "New")
        self.posts_display_header_box.add_widget(self.new_posts_header_display_label)
        
        self.favourite_posts_header_display_btn = Button (text = "Favourites")
        self.posts_display_header_box.add_widget(self.favourite_posts_header_display_btn)
        self.favourite_posts_header_display_btn.bind(on_press = self.favourite_posts_header_press)


        self.newest_posts_box = BoxLayout(size_hint_y = None, height = len(self.all_newest_posts_info) * Window.size[0] / 1.61, orientation = "vertical")
        self.content_grid.add_widget(self.newest_posts_box)

        #new posts
        self.create_newest_posts()
        
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
        self.current_posts = 2

    def favourite_posts_header_press(self, instance):
        #self.username = acces_my_info.GetName()
        self.all_favourite_posts_info = acces_my_info.get_liked_posts(self.connection)

        if self.current_posts == 1:
            self.popular_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.popular_posts_box)
        
        if self.current_posts == 2:
            self.newest_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.newest_posts_box)

        self.posts_display_header_box.clear_widgets()

        self.popular_posts_header_display_btn = Button(text = "Popular")
        self.posts_display_header_box.add_widget(self.popular_posts_header_display_btn)
        self.popular_posts_header_display_btn.bind(on_press = self.popular_posts_header_press)

        self.new_posts_header_display_btn = Button(text = "New")
        self.popular_posts_header_display_btn.add_widget(self.new_posts_header_display_btn)
        self.new_posts_header_display_btn.bind(on_press = self.new_posts_header_press)

        self.favourite_posts_header_display_label = Label (text = "Favourites")
        self.posts_display_header_box.add_widget(self.favourite_posts_header_display_label)

        self.favourite_posts_box = BoxLayout(size_hint_y = None, height = len(self.all_favourite_posts_info) * Window.size[0] / 1.61, orientation = "vertical")
        self.content_grid.add_widget(self.favourite_posts_box)

        #favourite posts
        self.create_favourite_posts()
        
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
        self.current_posts = 3

    def create_favourite_posts(self):
        self.all_displayed_posts_list = []
        connection = self.connection
        for a in len(self.all_favourite_posts_info):
            actual_maybe_like = 1
            user_liked_info = connection.get_user_info(self.all_favourite_posts_info[a]["user_name"])
            self.post_btn = functions.make_post_btn(self, self.all_favourite_posts_info[a]["user_name"], user_liked_info["profile_image"], self.all_favourite_posts_info[a]["flags"], self.all_favourite_posts_info[a]["content"], 0, self.all_favourite_posts_info[a]["time_posted"], self.all_favourite_posts_info[a]["id"], actual_maybe_like, a)
            self.favourite_posts_box.add_widget(self.post_btn)
            self.all_displayed_posts_list.append((self.all_favourite_posts_info[a]["id"], self.post_btn, actual_maybe_like))

    def create_popular_posts(self):
        self.all_displayed_posts_list = []
        conn = self.connection
        my_liked_posts_id = acces_my_info.get_liked_posts_id(conn)
        for p in len(self.all_popular_posts_info):
            user_post_info = conn.get_user_info(self.all_popular_posts_info[p]["user_name"])
            #0 none, 1 yes, 
            actual_maybe_like = 0
            try:
                for liked in my_liked_posts_id:
                    if liked == self.all_popular_posts_info[p]["id"]:
                        actual_maybe_like = 1
            except KeyError:
                pass
            self.post_btn = functions.make_post_btn(self, self.all_popular_posts_info[p]["user_name"], user_post_info["profile_image"], self.all_popular_posts_info[p]["flags"], self.all_popular_posts_info[p]["content"], 0, self.all_popular_posts_info[p]["time_posted"], self.all_popular_posts_info[p]["id"], actual_maybe_like, p)
            self.popular_posts_box.add_widget(self.post_btn)
            self.all_displayed_posts_list.append((self.all_popular_posts_info[p]["id"], self.post_btn, actual_maybe_like))


    def create_newest_posts(self):
        self.all_displayed_posts_list = []
        conn = self.connection
        my_liked_posts_id = acces_my_info.get_liked_id(conn)
        for t in len(self.all_newest_posts_info):
            user_post_info = conn.get_user(self.all_newest_posts_info[t]["user_name"])
            actual_maybe_like = 0
            try:
                for liked in my_liked_posts_id:
                    if liked == self.all_newest_posts_info[t]["id"]:
                        actual_maybe_like = 1
            except KeyError:
                pass
            self.post_btn = functions.make_post_btn(self, self.all_newest_posts_info[t]["user_name"], user_post_info["profile_image"], self.all_newest_posts_info[t]["flags"], self.all_newest_posts_info[t]["content"], 0, self.all_newest_posts_info[t]["time_posted"], self.all_newest_posts_info[t]["id"], actual_maybe_like, t)
            self.newest_posts_box.add_widget(self.post_btn)
            self.all_displayed_posts_list.append((self.all_newest_posts_info[t]["id"], self.post_btn, actual_maybe_like))

    def get_filter_flags(self):
        self.flag_list = ""
        for y in range (len(self.all_flags) - 1):
            self.flag_list = self.flag_list + str(self.all_flags[y + 1][3])
        return self.flag_list

    def name_press(self, order_number,instance):
        #go to user screen (owner of post)
        pass

    def image_press(self, order_number, instance):
        #go to user screen (owner of post)
        pass

    def content_post_press(self, order_number, instance):
        #go to post screen (pressed)
        pass

    def like_press(self, order_number, instance):
        num = self.all_displayed_posts_list[order_number][2]
        num = (num + 1) % 2
        if num == 1:
            instance.background_normal = 'images/heart2.png'
            functions.add_liked_or_unliked_post(self.all_displayed_posts_list[order_number][0], 1)
        if num == 0:
            instance.background_normal = 'images/heart.png'
            functions.add_liked_or_unliked_post(self.all_displayed_posts_list[order_number][0], 0)
        self.all_displayed_posts_list[order_number][2] = num

    def press_chat_btn(self, instance):
        #chat_screen.create_my_chats
        self.manager.transition = SlideTransition()
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    #def press_search_btn(self, instance):
    #    pass

    def press_home_btn(self, instance):
        home_screen.get_my_posts(0)
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_make_posts_btn(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_user_profile_btn(self, instance):
        #profile_screen.set_profile_screen_inputs
        self.manager.transition = SlideTransition()
        self.manager.current = "profile"
        self.manager.transition.direction = "left"