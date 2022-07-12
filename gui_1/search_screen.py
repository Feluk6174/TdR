#import kivy
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
import acces_my_info

def get_post_text(num):
    return (str(num))

class SearchScreen (Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
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
        

        self.box2 = BoxLayout (size_hint = (1, 0.9))
        self.Box0.add_widget(self.box2)
        
        self.scroll = ScrollView ()
        self.box2.add_widget (self.scroll) 

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget (self.grid)

        self.lab1 = TextInput(multiline = False, text = "Search post", size_hint_y = None, height = Window.size[1] / 15)
        self.grid.add_widget(self.lab1)
        self.lab1.bind(on_text_validate = self.search11)

        self.lab2 = TextInput(multiline = False, text = "Search user", size_hint_y = None, height = Window.size[1] / 15)
        self.grid.add_widget(self.lab2)
        self.lab2.bind(on_text_validate = self.search12)

        self.lab3 = TextInput(multiline = False, text = "Search hastag", size_hint_y = None, height = Window.size[1] / 15)
        self.grid.add_widget(self.lab3)
        self.lab2.bind(on_text_validate = self.search13)
   
        self.u_posts_all = BoxLayout(size_hint_y = None, height = Window.size[1] / 8)
        self.grid.add_widget(self.u_posts_all)

        self.popu_posts = Button(text = "Popular Posts")
        self.u_posts_all.add_widget(self.popu_posts)
        self.popu_posts.bind(on_press = self.UserPosts)
        
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

    def UserPosts(self, instance):
        if self.current_posts == 2:
            self.favourite_posts.clear_widgets()
            self.grid.remove_widget(self.favourite_posts)
        
        self.u_posts_all.clear_widgets()

        self.popu_posts = Label(text = "Popular Posts")
        self.u_posts_all.add_widget(self.popu_posts)
        
        self.fav = Button (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)
        self.fav.bind(on_press = self.UserFavourites)

        self.pop_posts = BoxLayout(size_hint_y = None, height = self.quant_p_p * Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.pop_posts)

        #my posts
        for a in range (self.quant_p_p): 
            self.btn_p = Button (size_hint_y = None, height = Window.size[0] / 1.61, text = "P" + (get_post_text(a)))
            self.pop_posts.add_widget(self.btn_p)
            
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.current_posts = 1

    def UserFavourites(self, instance):
        if self.current_posts == 1:
            self.pop_posts.clear_widgets()
            self.grid.remove_widget(self.pop_posts)
        
        self.u_posts_all.clear_widgets()
        
        self.popu_posts = Button(text = "Popular Posts")
        self.u_posts_all.add_widget(self.popu_posts)
        self.popu_posts.bind(on_press = self.UserPosts)

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