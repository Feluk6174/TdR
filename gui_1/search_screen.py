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


def get_post_text(num):
    return (str(num))

def ChangeTime(date):
    date_post = int(date)
    dt_obj = datetime.fromtimestamp(date_post).strftime('%d-%m-%y')
    return dt_obj

def hex_color(hex_num):
    if hex_num == "0":
        col = '#000000'
    if hex_num == "1":
        col = '#7e7e7e'
    if hex_num == "2":
        col = '#bebebe'
    if hex_num == "3":
        col = '#ffffff'
    if hex_num == "4":
        col = '#7e0000'
    if hex_num == "5":
        col = '#fe0000'
    if hex_num == "6":
        col = '#047e00'
    if hex_num == "7":
        col = '#06ff04'
    if hex_num == "8":
        col = '#7e7e00'
    if hex_num == "9":
        col = '#ffff04'
    if hex_num == "A":
        col = '#00007e'
    if hex_num == "B":
        col = '#0000ff'
    if hex_num == "C":
        col = '#7e007e'
    if hex_num == "D":
        col = '#fe00ff'
    if hex_num == "E":
        col = '#047e7e'
    if hex_num == "F":
        col = '#06ffff'
    return col

class SearchScreen (Screen):
    def __init__(self, connection, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.connection = connection
        
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.1))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/logo.png', background_down = 'images/logo.png')
        self.box1.add_widget(self.lab1)
        self.lab1.bind(on_release = self.press_btn13)
        
        self.text1 = Label(text = "Small brother", size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'images/settings1.png', background_down = 'images/settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 0.9))
        self.Box0.add_widget(self.box2)
        
        self.scroll = ScrollView ()
        self.box2.add_widget (self.scroll) 

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget (self.grid)

        #self.lab1 = TextInput(multiline = False, text = "Search post", size_hint_y = None, height = Window.size[1] / 15)
        #self.grid.add_widget(self.lab1)
        #self.lab1.bind(on_text_validate = self.search11)

        self.lab2 = TextInput(multiline = False, background_normal = 'images/search_user.png', size_hint_y = None, height = Window.size[1] / 15)
        self.grid.add_widget(self.lab2)
        self.lab2.bind(on_text_validate = self.search12)

        self.lab3 = TextInput(multiline = False, background_normal = 'images/search_hastag.png', size_hint_y = None, height = Window.size[1] / 15)
        self.grid.add_widget(self.lab3)
        self.lab2.bind(on_text_validate = self.search13)
   
        self.u_posts_all = BoxLayout(size_hint_y = None, height = Window.size[1] / 8)
        self.grid.add_widget(self.u_posts_all)

        self.popu_posts = Button(text = "Popular Posts")
        self.u_posts_all.add_widget(self.popu_posts)
        self.popu_posts.bind(on_press = self.PopularPosts)
        
        #self.fav = Button (text = "Favourites")
        #self.u_posts_all.add_widget(self.fav)
        #self.fav.bind(on_press = self.UserFavourites)

        #firstposts
        #current: 1 = popular, 2 = fav
        self.current_posts = 0
        self.quant_p_p = 8
        self.quant_f_p = 11
        self.popu_posts.trigger_action(duration = 0)

        """
        self.ran0 = Button (text = "Favourites", size_hint = (1, 1))
        self.grid.add_widget(self.ran0)
        self.ran0.bind(on_press = self.random0)

        self.ran1 = Button (text = "Global", size_hint = (1, 2.5))
        self.grid.add_widget(self.ran1)
        self.ran1.bind(on_press = self.random1)
        """


        self.box3 = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.Box0.add_widget(self.box3)

        self.btn11 = Button (text = ("C"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Label (text = ("Search"))
        self.box3.add_widget(self.btn12)
        
        self.btn13 = Button (text = ("H"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

        self.btn14 = Button (text = ("P"))
        self.box3.add_widget(self.btn14)
        self.btn14.bind(on_press = self.press_btn14)

        self.btn15 = Button (text = ("U"))
        self.box3.add_widget(self.btn15)
        self.btn15.bind(on_press = self.press_btn15)
        

    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass

    def search11(instance, value):
        pass

    def search12(instance, value):
        pass

    def search13(instance, value):
        pass

    def random0(self, instance):
        pass

    def random1(self, instance):
        pass

    def PopularPosts(self, instance):
        #connection = self.connection
        #self.all_popular_posts_info = connection.get_popular_posts()
        self.all_popular_posts_info = []

        if self.current_posts == 2:
            self.favourite_posts.clear_widgets()
            self.grid.remove_widget(self.favourite_posts)

        if self.current_posts == 3:
            self.newest_posts.clear_widgets()
            self.grid.remove_widget(self.newest_posts)
        
        self.u_posts_all.clear_widgets()

        self.popu_posts = Label(text = "Popular")
        self.u_posts_all.add_widget(self.popu_posts)

        self.new_posts = Button(text = "New")
        self.u_posts_all.add_widget(self.new_posts)
        self.new_posts.bind(on_press = self.NewPosts)
        
        self.fav = Button (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)
        self.fav.bind(on_press = self.UserFavourites)

        self.pop_posts = BoxLayout(size_hint_y = None, height = self.quant_p_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.pop_posts)

        #my posts
        self.create_popular()
            
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 1

    def UserFavourites(self, instance):
        self.username = acces_my_info.GetName()
        #conn = self.connection
        self.my_liked_list = acces_my_info.GetLiked()
        #self.my_liked_list = conn.get_posts_with_id()
        self.all_liked_posts = []

        self.quant_f_p = len(self.my_liked_list)

        if self.current_posts == 1:
            self.pop_posts.clear_widgets()
            self.grid.remove_widget(self.my_posts)
        
        if self.current_posts == 2:
            self.newest_posts.clear_widgets()
            self.grid.remove_widget(self.newest_posts)

        self.u_posts_all.clear_widgets()

        self.us_posts = Button(text = "Popular")
        self.u_posts_all.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.PopularPosts)

        self.new_posts = Button(text = "New")
        self.u_posts_all.add_widget(self.new_posts)
        self.new_posts.bind(on_press = self.NewPosts)

        self.fav = Label (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)

        self.favourite_posts = BoxLayout(size_hint_y = None, height = self.quant_f_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.favourite_posts)

        #favourite posts
        self.create_liked()
        
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 3
    
    def NewPosts(self, instance):
        self.quant_n_p = 10
        #connection = self.connection
        #self.all_new_posts_info = connection.get_new_posts(self.quant_n_p)
        self.all_new_posts_info = []

        if self.current_posts == 1:
            self.pop_posts.clear_widgets()
            self.grid.remove_widget(self.pop_posts)
        
        if self.current_posts == 3:
            self.favourite_posts.clear_widgets()
            self.grid.remove_widget(self.favourite_posts)

        self.u_posts_all.clear_widgets()

        self.us_posts = Button(text = "Popular")
        self.u_posts_all.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.PopularPosts)

        self.new_posts = Label(text = "New")
        self.u_posts_all.add_widget(self.new_posts)

        self.fav = Button (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)
        self.fav.bind(on_press = self.UserFavourites)

        self.newest_posts = BoxLayout(size_hint_y = None, height = self.quant_n_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.favourite_posts)

        #new posts
        self.create_new()
        
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 2

    def create_liked(self):
        actual_maybe_like = 5
        connection = self.connection
        for liked in self.my_liked_list:
            user_liked_info = connection.get_user(liked["user_name"])        
            self.all_liked_posts.append((liked["user_name"], user_liked_info["profile_image"], liked["flags"], liked["content"], 0, liked["time_posted"], liked["id"], actual_maybe_like))
            self.make_post_btn(liked["user_name"], user_liked_info["profile_image"], liked["flags"], liked["content"], 0, liked["time_posted"], liked["id"], actual_maybe_like)

    def create_popular(self):
        my_liked_posts = acces_my_info.GetLiked()
        self.connection = connection
        for post in self.all_popular_posts_info:
            user_info = connection.get_user(post["user_name"])
            #0 none, 1 yes, 
            actual_maybe_like = 0
            for liked in my_liked_posts:
                if liked["id"] == post["id"]:
                    actual_maybe_like = 1
            self.make_post_btn(post["user_name"], user_info["profile_image"], post["flags"], post["content"], 0, post["time_posted"], post["id"], actual_maybe_like)

    def create_new(self):
        my_liked_posts = acces_my_info.GetLiked()
        self.connection = connection
        for post in self.all_new_posts_info:
            user_info = connection.get_user(post["user_name"])
            actual_maybe_like = 2
            for liked in my_liked_posts:
                if liked["id"] == post["id"]:
                    actual_maybe_like = 3
            self.make_post_btn(post["user_name"], user_info["profile_image"], post["flags"], post["content"], 0, post["time_posted"], post["id"], actual_maybe_like)
    

    def Name_press(self, instance):
        pass

    def Image_press(self, instance):
        pass

    def Like_press(self, instance):
        num = int(instance.text)
        num = (num + 1) % 2
        if num == 1:
            instance.background_normal = 'images/heart2.png'
            home_screen.add_liked_post(instance.text)
        if num == 0:
            instance.background_normal = 'images/heart.png'
        instance.text = str(num)

    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, post_flags, textp, nlikes, date, moment_id, like_self):
        self.post = BoxLayout(size_hint_y = None, height = Window.size[0] / 1.61, orientation = "vertical")
        if like_self < 2 and like_self > (-1):
            self.pop_posts.add_widget(self.post)
        elif like_self < 4 and like_self > 1:
            self.newest_posts.add_widget(self.post)
        elif like_self < 6 and like_self > 3:
            self.pop_posts.add_widget(self.post)

        self.post_like = 0
        if int(like_self) == 1 or int(like_self) == 3 or int(like_self) ==5:
            self.post_like = 1
        
        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
            
        self.im = GridLayout(cols = 8, size_hint_x = None, width = Window.size[0] / 1.61 / 6)
        self.first_box.add_widget(self.im)
        self.BuildImagePost(user_image)
        
        self.pname = Button(text = user_name)
        self.first_box.add_widget(self.pname)
        self.pname.bind(on_press = self.Name_press)

        self.date = Label(size_hint_x = None, width = Window.size[0] / 1.61 / 3, text = str(ChangeTime(date)))
        self.first_box.add_widget(self.date)

        self.second_box = BoxLayout(size_hint = (1, 2))
        self.post.add_widget(self.second_box)

        self.txt = Button (text = textp)
        self.second_box.add_widget(self.txt)

        self.third_box = BoxLayout(size_hint = (1, 0.5))
        self.post.add_widget(self.third_box)

        self.flags = BoxLayout(size_hint = (1, 1))
        self.third_box.add_widget(self.flags)

        self.all_flags = [['images/check_verd.png'], ['images/age18.png'], ['images/blood.png'], ['images/fist.png'], ['images/soga.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png']]
        for x in range (len(self.all_flags) - 1):
            if post_flags[x] == "1":
                self.f_btn = Button(border = (0, 0, 0, 0), size_hint_x = None, width = (Window.size[1] - Window.size[0] / 5) * 0.9 / 12, background_normal = self.all_flags[x + 1][0])
                #self.all_flags[x + 1].append(self.f_btn)
                #self.all_flags[x + 1].append(0)
                self.flags.add_widget(self.f_btn)

        self.likes = BoxLayout(size_hint = (None, 1), width = Window.size[0] / 1.61 / 3)
        self.third_box.add_widget(self.likes)

        self.like_heart = Button(border = (0, 0, 0, 0),font_size = 0.01, text = moment_id)
        if self.post_like == 0:
            self.like_heart.background_normal = 'images/heart.png'
        if self.post_like == 1:
            self.like_heart.background_normal = 'images/heart2.png'
        self.likes.add_widget(self.like_heart)
        self.like_heart.bind(on_press = self.Like_press)

        self.num_likes = Label (text = (str(nlikes)), size_hint = (1, 1))
        self.likes.add_widget(self.num_likes)

        #self.all_my_posts.append(self.post)
        self.grid.bind(minimum_height=self.grid.setter('height'))
    
    def BuildImagePost(self, user_image):
        self.color_list = user_image
        self.color_button_list = []
        for x in range (64):
            self.color_bit = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(self.color_list[x])), on_release = self.Image_press)
            self.color_button_list.append(self.color_bit)
            self.im.add_widget(self.color_bit)

    def press_btn11(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        pass

    def press_btn13(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "main"
        self.manager.transition.direction = "left"

    def press_btn14(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "profile"
        self.manager.transition.direction = "left"