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
from kivy.uix.dropdown import DropDown
import json
import acces_my_info, register_screen
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

class ProfileScreen (Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.1))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        self.lab1.bind(on_release = self.press_btn13)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'settings1.png', background_down = 'settings2.png')
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

        self.us_des = Button(text = acces_my_info.GetDescription(), size_hint_y = None, height = (Window.size[1] - Window.size[0] / 5) * 2 * 0.9 / 5)
        self.grid.add_widget(self.us_des)
        self.us_des.bind(on_press = self.UserDescription)

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
        self.quant_m_p = 10
        self.quant_f_p = 11
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
        self.text_des = self.us_des.text
        #self.us_des = TextInput(text = self.text_des, multiline = False, on_text_validate = self.change_description_2)

    #def change_description_2(self, instance, value):
        #self.text_des = self.us_des.text
        #self.us_des = Button(text = self.text_des, on_press = self.UserDescription)

    def UserFollowers(self, instance):
        pass

    def UserFollowing(self, instance):
        pass

    def UserPosts(self, instance):
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
        for a in range (self.quant_m_p): 
            self.btn_p = Button (size_hint_y = None, height = Window.size[0] / 1.61, text = "M" + (get_post_text(a)))
            self.my_posts.add_widget(self.btn_p)

        self.us_posts = Label(text = "My Posts")
        self.fav = Button(text = "Favourite Posts")
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 1

    def Image_press(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "image"

    def UserFavourites(self, instance):
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
        for a in range (self.quant_f_p):
            self.btn_f = Button (size_hint_y = None, height = Window.size[0] / 1.61, text = "F" + (get_post_text(a)))
            self.favourite_posts.add_widget(self.btn_f)
        
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 2

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