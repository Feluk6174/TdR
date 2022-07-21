#import kivy 
from multiprocessing import connection
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
from datetime import datetime
from kivy.uix.dropdown import DropDown
import json
from matplotlib.pyplot import connect
import acces_my_info, register_screen, api, home_screen
from kivy.clock import Clock


def get_post_text(num):
    return(str(num))

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

def ChangeTime(date):
    date_post = int(date)
    dt_obj = datetime.fromtimestamp(date_post).strftime('%d-%m-%y')
    return dt_obj

class ProfileScreen (Screen):
    def __init__(self, connection, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

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
        

        self.box2 = BoxLayout (size_hint = (1, 0.9), orientation = "vertical")
        self.Box0.add_widget(self.box2)

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)

        self.user_n_f = BoxLayout(size_hint_y = None, height = (Window.size[1]  - Window.size[0] / 5) * 0.9 / 5)
        self.grid.add_widget(self.user_n_f)

        self.us_image = GridLayout(cols = 8, size_hint_x = None, width =  (Window.size[1] - Window.size[0] / 5) * 0.9 / 5)
        self.user_n_f.add_widget(self.us_image)

        self.us_image_list = acces_my_info.GetImage()
        self.BuildImage(self.us_image_list)        

        self.us_name = Button(text = acces_my_info.GetName())
        self.user_n_f.add_widget(self.us_name)
        self.us_name.bind(on_press = self.UserName)

        self.description_box = BoxLayout(size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 2 * 0.9 / 5)
        self.grid.add_widget(self.description_box)

        self.us_des_btn = Button(text = acces_my_info.GetDescription())
        self.description_box.add_widget(self.us_des_btn)
        self.us_des_btn.bind(on_press = self.UserDescription)

        self.user_foll = BoxLayout(size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 0.9 / 5)
        self.grid.add_widget(self.user_foll)

        self.us_followers = Button(text = "Followers")
        self.user_foll.add_widget(self.us_followers)
        self.us_followers.bind(on_press = self.UserFollowers)

        self.us_following = Button(text = "Following")
        self.user_foll.add_widget(self.us_following)
        self.us_following.bind(on_press = self.UserFollowing)

        self.u_posts_all = BoxLayout(size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 0.9 / 5)
        self.grid.add_widget(self.u_posts_all)

        self.us_posts = Button(text = "My Posts")
        self.u_posts_all.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.UserPosts)
        
        #self.fav = Button (text = "Favourites")
        #self.u_posts_all.add_widget(self.fav)
        #self.fav.bind(on_press = self.UserFavourites)

        #firstposts
        #current: 1 = my, 2 = fav
        self.current_posts = 0
        self.us_posts.trigger_action(duration = 0)


        self.box3 = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
        self.Box0.add_widget(self.box3)

        self.btn11 = Button (text = ("C"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Button (text = ("S"))
        self.box3.add_widget(self.btn12)
        self.btn12.bind(on_press = self.press_btn12)

        self.btn13 = Button (text = ("H"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

        self.btn14 = Button (text = ("P"))
        self.box3.add_widget(self.btn14)
        self.btn14.bind(on_press = self.press_btn14)

        self.btn15 = Label (text = ("User"))
        self.box3.add_widget(self.btn15)


    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass

    def BuildImage(self, user_image):
        self.us_image.clear_widgets()
        self.color_list = user_image
        self.color_button_list = []
        for x in range (64):
            self.color_bit = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(self.color_list[x])), on_release = self.Image_press)
            self.color_button_list.append(self.color_bit)
            self.us_image.add_widget(self.color_bit)  

    def UserName(self, instance):
        pass

    def UserDescription(self, instance):
        self.text_des = self.us_des_btn.text
        self.description_box.clear_widgets()

        self.us_des_text = TextInput(text = self.text_des, multiline = False, on_text_validate = self.change_description_2)
        self.description_box.add_widget(self.us_des_text)

    def change_description_2(self, instance):
        self.text_des = self.us_des_text.text
        self.description_box.clear_widgets()

        acces_my_info.change_my_description(self.text_des)

        self.us_des_btn = Button(text = self.text_des, on_press = self.UserDescription)
        self.description_box.add_widget(self.us_des_btn)

    def UserFollowers(self, instance):
        pass

    def UserFollowing(self, instance):
        pass

    def UserPosts(self, instance):
        self.username = acces_my_info.GetName()
        conn = self.connection
        self.my_posts_list = conn.get_user_posts(self.username)
        self.all_my_posts = []

        self.quant_m_p = len(self.my_posts_list)

        if self.current_posts == 2:
            self.favourite_posts.clear_widgets()
            self.grid.remove_widget(self.favourite_posts)

        self.u_posts_all.clear_widgets()

        self.us_posts = Label(text = "My Posts")
        self.u_posts_all.add_widget(self.us_posts)
        
        self.fav = Button (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)
        self.fav.bind(on_press = self.UserFavourites)

        self.my_posts = BoxLayout(size_hint_y = None, height = self.quant_m_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.my_posts)

        #my posts
        self.create_my_posts()

        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 1

    def BuildImagePost(self, user_image):
        self.color_list = user_image
        self.color_button_list = []
        for x in range (64):
            self.color_bit = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(self.color_list[x])), on_release = self.Image_press)
            self.color_button_list.append(self.color_bit)
            self.im.add_widget(self.color_bit)

    def create_my_posts(self):
        conn = self.connection
        my_liked_posts = acces_my_info.GetLiked(conn)
        for post in self.my_posts_list:
            actual_maybe_like = 0
            try:
                for liked in my_liked_posts:
                    if liked["id"] == post["id"]:
                        actual_maybe_like = 1
            except KeyError:
                pass
            self.all_my_posts.append((self.username, acces_my_info.GetImage(), post["flags"], post["content"], 0, post["time_posted"], post["id"], actual_maybe_like))
            self.make_post_btn(self.username, acces_my_info.GetImage(), post["flags"], post["content"], 0, post["time_posted"], post["id"], actual_maybe_like)
        
    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, post_flags, textp, nlikes, date, moment_id, like_self):
        self.post = BoxLayout(size_hint_y = None, height = Window.size[0] / 1.61, orientation = "vertical")
        self.my_posts.add_widget(self.post)

        self.post_like = like_self
        
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

        self.all_my_posts.append(self.post)
        self.grid.bind(minimum_height=self.grid.setter('height'))

    def Image_press(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "image"

    def Like_press(self, instance):
        num = int(instance.text)
        num = (num + 1) % 2
        if num == 1:
            instance.background_normal = 'images/heart2.png'
            home_screen.add_liked_post(instance.text)
        if num == 0:
            instance.background_normal = 'images/heart.png'
        instance.text = str(num)

    def Name_press(self):
        pass

    def UserFavourites(self, instance):
        self.username = acces_my_info.GetName()
        conn = self.connection
        self.my_liked_list = acces_my_info.GetLiked(conn)
        #self.my_liked_list = conn.get_posts_with_id()
        self.all_liked_posts = []

        self.quant_f_p = len(self.my_liked_list)

        if self.current_posts == 1:
            self.my_posts.clear_widgets()
            self.grid.remove_widget(self.my_posts)

        self.u_posts_all.clear_widgets()

        self.us_posts = Button(text = "My Posts")
        self.u_posts_all.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.UserPosts)

        self.fav = Label (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)

        self.favourite_posts = BoxLayout(size_hint_y = None, height = self.quant_f_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.favourite_posts)

        #favourite posts
        self.create_liked()
        
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 2
    
    def create_liked(self):
        actual_maybe_like = 1
        for liked in self.my_liked_list:
            user_liked_info = self.connection.get_user(liked["user_name"])        
            self.all_liked_posts.append((liked["user_name"], user_liked_info["profile_image"], liked["flags"], liked["content"], 0, liked["time_posted"], liked["id"], actual_maybe_like))
            self.make_post_btn(liked["user_name"], user_liked_info["profile_image"], liked["flags"], liked["content"], 0, liked["time_posted"], liked["id"], actual_maybe_like)
        

    def press_btn11(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "search"
        self.manager.transition.direction = "right"

    def press_btn13(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "main"
        self.manager.transition.direction = "right"

    def press_btn14(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "right"
    
    def press_btn15(self, instance):
        pass
