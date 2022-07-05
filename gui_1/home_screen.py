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
    return str(num)

class MainScreen (Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (70, 70), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False)
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(size_hint = (None, None), size = (70, 70), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None, spacing = 3)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)


        #posts prova
        self.post = BoxLayout(size_hint_y = None, height = 200, orientation = "vertical")
        self.grid.add_widget(self.post)
        self.post_like = 0

        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
        
        self.im = Button(size_hint = (None, 1), width = 50, text = "O")
        self.first_box.add_widget(self.im)
        self.im.bind(on_press = partial(self.Image_press))
        
        self.pname = Button(text = "aniol")
        self.first_box.add_widget(self.pname)
        self.pname.bind(on_press = partial(self.Name_press))

        self.likes = BoxLayout(size_hint = (None, 1), width = 100)
        self.first_box.add_widget(self.likes)

        self.like_heart = Button(background_normal = 'heart.png')
        self.likes.add_widget(self.like_heart)
        self.like_heart.bind(on_press = partial(self.Like_press, 0))

        self.num_likes = Label (text = (str(0 + self.post_like)), size_hint = (1, 1))
        self.likes.add_widget(self.num_likes)

        self.second_box = BoxLayout(size_hint = (1, 2))
        self.post.add_widget(self.second_box)

        self.txt = Button (text = "hello world")
        self.second_box.add_widget(self.txt)

        for a in range (7):
            self.btn_p = Button (size_hint_y = None, height = 100, text = "P" + (get_post_text(a)))
            self.grid.add_widget(self.btn_p)

        """
        #botó per crear posts
        self.btn1 = Button (text = "1", size_hint_y = None, height = 50)
        self.grid.add_widget(self.btn1)
        self.btn1.bind(on_press = partial(self.make_post_btn, "aniol", "foto", "What doesn't kill you makes you stronger." + '\n' + " ~Friedrich Niesche~", 9))
        """



        self.box3 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box3)

        self.btn11 = Button (text = ("C"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Button (text = ("S"))
        self.box3.add_widget(self.btn12)
        self.btn12.bind(on_press = self.press_btn12)

        self.btn13 = Label (text = ("Home"))
        self.box3.add_widget(self.btn13)

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

    def press_btn11(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "search"
        self.manager.transition.direction = "right"

    def press_btn13(self, instance):
        pass

    def press_btn14(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "profile"
        self.manager.transition.direction = "left"
    
    """
    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, textp, nlikes, instance):
        
        self.post = BoxLayout(size_hint_y = None, height = 200, orientation = "vertical")
        self.grid.add_widget(self.post)
        self.post_like = 0

        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
        
        self.im = Button(size_hint = (None, 1), width = 50, text = "I")
        self.first_box.add_widget(self.im)
        self.im.bind(on_press = partial(self.Image_press))
        
        self.pname = Button(text = "aniol")
        self.first_box.add_widget(self.pname)
        self.pname.bind(on_press = partial(self.Name_press))

        self.likes = BoxLayout(size_hint = (None, 1), width = 100)
        self.first_box.add_widget(self.likes)

        self.like_heart = Button(background_normal = 'heart.png')
        self.likes.add_widget(self.like_heart)
        self.like_heart.bind(on_press = partial(self.Like_press, 0))

        self.num_likes = Label (text = (str(0 + self.post_like)), size_hint = (1, 1))
        self.likes.add_widget(self.num_likes)

        self.second_box = BoxLayout(size_hint = (1, 2))
        self.post.add_widget(self.second_box)

        self.txt = Button (text = "hello world")
        self.second_box.add_widget(self.txt)
        """

    
    def Name_press(self, instance):
        pass

    def Image_press(self, instance):
        pass

    def Like_press(self, nlikes, instance):
        self.post_like = (self.post_like + 1) % 2
        self.num_likes.text = (str(nlikes + self.post_like))
        return
        