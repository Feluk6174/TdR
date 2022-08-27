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
from datetime import datetime

import access_my_info, functions, search_screen, home_screen, chat_screen



class ProfileScreen (Screen):
    def __init__(self, connection, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

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
        

        self.content_box = BoxLayout (size_hint = (1, 0.9), orientation = "vertical")
        self.main_all_box.add_widget(self.content_box)

        self.content_grid = GridLayout(cols = 1, size_hint_y = None)
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))

        self.content_grid_scroll = ScrollView ()
        self.content_grid_scroll.add_widget (self.content_grid)
        self.main_all_box.add_widget (self.content_grid_scroll)

        self.user_image_name_box = BoxLayout(size_hint_y = None, height = (Window.size[1]  - Window.size[0] / 5) * 0.9 / 5)
        self.content_grid.add_widget(self.user_image_name_box)

        self.user_image_box = BoxLayout()
        self.user_image_name_box.add_widget(self.user_image_box)
        
        self.user_image_grid = functions.build_image(self, access_my_info.get_profile_image(), 0, Window.size[0] / 1.61 / 6)
        self.user_image_box.add_widget(self.user_image_grid)

        self.user_name_btn = Button(text = access_my_info.get_user_name())
        self.user_image_name_box.add_widget(self.user_name_btn)
        #self.user_name_btn.bind(on_release = self.user_name_press)

        self.description_box = BoxLayout(size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 2 * 0.9 / 5)
        self.content_grid.add_widget(self.description_box)

        self.user_description_btn = Button(text = access_my_info.get_description(), size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 2 * 0.9 / 5)
        self.content_grid.add_widget(self.user_description_btn)
        self.user_description_btn.bind(on_release = self.user_description_press)

        self.user_following_btn = Button(text = "Following", size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 0.9 / 5)
        self.content_grid.add_widget(self.user_following_btn)
        self.user_following_btn.bind(on_release = self.user_following_press)

        self.user_posts_header_box = BoxLayout(size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 0.9 / 5)
        self.content_grid.add_widget(self.user_posts_header_box)

        #self.user_posts = Button(text = "My Posts")
        #self.user_posts_header_box.add_widget(self.user_posts)
        #self.us_posts.bind(on_press = self.UserPosts)
        
        #self.fav = Button (text = "Favourites")
        #self.u_posts_all.add_widget(self.fav)
        #self.fav.bind(on_press = self.UserFavourites)

        #firstposts
        #current: 1 = my, 2 = fav
        self.current_posts = 0
        
        
        #self.user_posts_press(0)


        self.ground_box = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.main_all_box.add_widget(self.ground_box)

        self.chat_btn = Button (text = ("C"))
        self.ground_box.add_widget(self.chat_btn)
        self.chat_btn.bind(on_release = self.press_chat_btn)

        self.search_btn = Button (text = ("S"))
        self.ground_box.add_widget(self.search_btn)
        self.search_btn.bind(on_release = self.press_search_btn)

        self.home_btn = Button (text = ("H"))
        self.ground_box.add_widget(self.home_btn)
        self.home_btn.bind(on_release = self.press_home_btn)

        self.make_posts_btn = Button (text = ("P"))
        self.ground_box.add_widget(self.make_posts_btn)
        self.make_posts_btn.bind(on_release = self.press_make_posts_btn)

        self.user_profile_label = Label (text = ("User"))
        self.ground_box.add_widget(self.user_profile_label)


    def user_description_press(self, instance):
        self.text_description = self.user_description_btn.text
        self.description_box.clear_widgets()

        self.user_description_input = TextInput(text = self.text_description, multiline = False, on_text_validate = self.change_description)
        self.description_box.add_widget(self.user_description_input)

    def change_description(self, instance):
        self.text_description = self.user_description_input.text
        self.description_box.clear_widgets()

        functions.change_my_description(self.text_description)

        self.user_description_btn = Button(text = self.text_description, on_release = self.user_description_press)
        self.description_box.add_widget(self.user_description_btn)

    def user_followers_press(self, instance):
        #go to screen
        pass

    def user_following_press(self, instance):
        #go to screen
        pass

    def refresh_profile_screen(self):
        #self.user_image_box.clear_widgets()

        #self.user_image_grid = functions.build_image(self, access_my_info.get_image(), 0, Window.size[0] / 1.61 / 6)
        #self.user_image_box.add_widget(self.user_image_grid)
        
        if self.current_posts != 1:
            self.user_posts_press(0)
        elif self.current_posts == 1:
            self.user_favourites_press(0)
            self.user_posts_press(0)

    def user_posts_press(self, instance):
        conn = self.connection
        self.my_posts_list = conn.get_posts(username = self.user_name_btn.text)
        #self.my_posts_list = access_my_info.get_my_posts()
        #self.my_posts_list = []
        self.my_posts_list = functions.order_posts_by_timestamp(self.my_posts_list)

        if self.current_posts == 2:
            self.favourite_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.favourite_posts_box)

        self.user_posts_header_box.clear_widgets()

        self.user_posts_label = Label(text = "My Posts")
        self.user_posts_header_box.add_widget(self.user_posts_label)
        
        self.favourite_posts_btn = Button (text = "Favourites")
        self.user_posts_header_box.add_widget(self.favourite_posts_btn)
        self.favourite_posts_btn.bind(on_release = self.user_favourites_press)


        #my posts
        self.create_my_posts()

        self.current_posts = 1

    def user_favourites_press(self, instance):
        conn = self.connection
        #with connection or in phone memory
        self.my_liked_list_id = access_my_info.get_liked_id()
        self.my_liked_list = []
        for id in self.my_liked_list_id:
            self.my_liked_list.append(conn.get_post(id = id))
        #self.my_liked_posts_list = []
        self.my_liked_posts_list = functions.order_posts_by_timestamp(self.my_liked_posts_list)

        if self.current_posts == 1:
            self.my_posts_box.clear_widgets()
            self.content_grid.remove_widget(self.my_posts_box)

        self.user_posts_header_box.clear_widgets()

        self.user_posts_btn = Button(text = "My Posts")
        self.user_posts_header_box.add_widget(self.user_posts_btn)
        self.user_posts_btn.bind(on_release = self.user_posts_press)

        self.favourite_posts_label = Label (text = "Favourites")
        self.user_posts_header_box.add_widget(self.favourite_posts_label)


        #favourite posts
        self.create_liked_posts()

        self.current_posts = 2

    def create_my_posts(self):
        #conn = self.connection

        self.my_posts_box = BoxLayout(size_hint_y = None, height = len(self.my_posts_list) * Window.size[0] / 1.61, orientation = "vertical")
        self.content_grid.add_widget(self.my_posts_box)

        my_liked_posts_id = access_my_info.get_liked_id()
        self.all_displayed_posts_list = []
        my_image = access_my_info.get_profile_image()
        for a in range (len(self.my_posts_list)):
            actual_maybe_like = 0
            try:
                for liked_id in my_liked_posts_id:
                    if liked_id == self.my_posts_list[a]["id"]:
                        actual_maybe_like = 1
            except KeyError:
                pass
            self.post_btn = functions.make_post_btn(self.my_posts_list[a]["user_id"], my_image, self.my_posts_list[a]["flags"], self.my_posts_list[a]["content"], 0, self.my_posts_list[a]["time_posted"], self.my_posts_list[a]["id"], actual_maybe_like, a)
            self.my_posts_box.add_widget(self.post)
            self.all_displayed_posts_list.append(self.my_posts_list[a]["id"], self.post_btn, actual_maybe_like)

        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
    
    def create_liked_posts(self):
        conn = self.connection

        self.favourite_posts_box = BoxLayout(size_hint_y = None, height = len(self.my_liked_posts_list) * Window.size[0] / 1.61, orientation = "vertical")
        self.content_grid.add_widget(self.favourite_posts_box)

        actual_maybe_like = 1
        for b in range (len(self.my_liked_posts_list)):
            user_liked_info = conn.get_user(self.my_liked_posts_list[b]["user_id"])        
            self.post_btn = functions.make_post_btn(self.my_liked_posts_list[b]["user_id"], user_liked_info["profile_picture"], self.my_liked_posts_list[b]["flags"], self.my_liked_posts_list[b]["content"], self.my_liked_posts_list[b]["likes"], self.my_liked_posts_list[b]["time_posted"], self.my_liked_posts_list[b]["id"], actual_maybe_like, b)
            self.my_posts_box.add_widget(self.post)
            self.all_displayed_posts_list.append(self.my_liked_posts_list[b]["id"], self.post_btn, actual_maybe_like)
        
        self.content_grid.bind(minimum_height=self.content_grid.setter('height'))
    
    def user_image_press(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "image"

    def like_press(self, order_number, instance):
        #num = int(instance.text)
        num = order_number
        like = (self.all_displayed_posts_list[num][2] + 1) % 2
        if like == 1:
            instance.background_normal = 'images/heart2.png'
            functions.add_liked_or_unliked_post(self.all_displayed_posts_list[num][0], like)
        if like == 0:
            instance.background_normal = 'images/heart.png'
            functions.add_liked_or_unliked_post(self.all_displayed_posts_list[num][0], like)
        
        self.all_displayed_posts_list[num][2] = like

    def name_press(self, order_number,instance):
        #go to user screen (owner of post)
        pass

    def image_press(self, order_number, instance):
        #go to user screen (owner of post)
        pass

    def content_post_press(self, order_number, instance):
        #go to post screen (pressed)
        pass

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

    def press_home_btn(self, instance):
        home_scrn = self.home_screen
        home_screen.get_my_posts(home_scrn)
        self.manager.current = "home"
        self.manager.transition.direction = "right"

    def press_make_posts_btn(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "create"
        self.manager.transition.direction = "right"

    #def press_user_profile_btn(self, instance):
        #pass
    
    def add_screens(self, home_screen, chat_screen, search_screen):
        self.home_screen = home_screen
        self.chat_screen = chat_screen
        self.search_sscreen = search_screen