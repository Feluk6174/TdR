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

def get_post_text(num):
    return(str(num))

class ProfileScreen (Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        self.lab1.bind(on_release = self.press_btn13)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1), orientation = "vertical")
        self.Box0.add_widget(self.box2)

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)

        self.user_n_f = BoxLayout(size_hint_y = None, height = 100)
        self.grid.add_widget(self.user_n_f)

        self.us_image = Button(text = "Foto", size_hint = (0.5, 1))
        self.user_n_f.add_widget(self.us_image)
        self.us_image.bind(on_press = self.UserImage)

        self.us_name = Button(text = "Name")
        self.user_n_f.add_widget(self.us_name)
        self.us_name.bind(on_press = self.UserName)

        self.us_des = Button(text = "Description", size_hint_y = None, height = 162)
        self.grid.add_widget(self.us_des)
        self.us_des.bind(on_press = self.UserDescription)

        self.user_foll = BoxLayout(size_hint_y = None, height = 100)
        self.grid.add_widget(self.user_foll)

        self.us_followers = Button(text = "Followers")
        self.user_foll.add_widget(self.us_followers)
        self.us_followers.bind(on_press = self.UserFollowers)

        self.us_following = Button(text = "Following")
        self.user_foll.add_widget(self.us_following)
        self.us_following.bind(on_press = self.UserFollowing)

        self.u_posts_all = BoxLayout(size_hint_y = None, height = 100)
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


        self.box3 = BoxLayout (size_hint = (1, 0.15))
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

    def UserName(self, instance):
        pass

    def UserImage(self, instance):
        pass

    def UserDescription(self, instance):
        pass

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

        self.my_posts = BoxLayout(size_hint_y = None, height = self.quant_m_p * 100, orientation = "vertical")
        self.grid.add_widget(self.my_posts)

        #my posts
        for a in range (self.quant_m_p): 
            self.btn_p = Button (size_hint_y = None, height = 100, text = "M" + (get_post_text(a)))
            self.my_posts.add_widget(self.btn_p)

        self.us_posts = Label(text = "My Posts")
        self.fav = Button(text = "Favourite Posts")
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 1

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

        self.favourite_posts = BoxLayout(size_hint_y = None, height = self.quant_f_p * 100, orientation = "vertical")
        self.grid.add_widget(self.favourite_posts)

        #favourite posts
        for a in range (self.quant_f_p):
            self.btn_f = Button (size_hint_y = None, height = 100, text = "F" + (get_post_text(a)))
            self.favourite_posts.add_widget(self.btn_f)
            
        
        
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 2

    def press_btn11(self, instance):
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        self.manager.current = "search"
        self.manager.transition.direction = "right"

    def press_btn13(self, instance):
        self.manager.current = "main"
        self.manager.transition.direction = "right"

    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "right"