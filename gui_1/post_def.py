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

Window.size = (300, 500)

class test(BoxLayout):
    def __init__(self, **kwargs):
        super(test, self).__init__(**kwargs)
        
        self.orientation = "vertical"

        self.all_posts_info = []
        for post in self.all_posts_info:
            self.make_post_btn(post["username"], post["userimage"], post["posttext"], post["postlikes"], post["postdate"])
        
        self.btn_1 = Button(text = "A", on_press = self.Hey)
        self.add_widget(self.btn_1)


        #self.make_post_btn("aniol", 0, "Hello World", 10, "14/3/1984")

    def Hey(self, instance):
        print(instance)

    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, textp, nlikes, date):
    
        self.post = BoxLayout(size_hint_y = None, height = Window.size[0] / 1.61, orientation = "vertical")
        self.add_widget(self.post)
        self.post_like = 0
        
        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
            
        self.im = Button(size_hint_x = None, width = Window.size[0] / 1.61 / 6)
        self.first_box.add_widget(self.im)
        self.im.bind(on_press = partial(self.Image_press))
        
        self.pname = Button(text = user_name)
        self.first_box.add_widget(self.pname)
        self.pname.bind(on_press = partial(self.Name_press))

        self.date = Label(size_hint_x = None, width = Window.size[0] / 1.61 / 3, text = date)
        self.first_box.add_widget(self.date)

        self.second_box = BoxLayout(size_hint = (1, 2))
        self.post.add_widget(self.second_box)

        self.txt = Button (text = textp)
        self.second_box.add_widget(self.txt)

        self.third_box = BoxLayout(size_hint = (1, 0.5))
        self.post.add_widget(self.third_box)

        self.flags = BoxLayout(size_hint = (2, 1))
        self.third_box.add_widget(self.flags)

        self.flag_text = Button (text = "more")
        self.flags.add_widget(self.flag_text)

        self.likes = BoxLayout(size_hint = (None, 1), width = Window.size[0] / 1.61 / 3)
        self.third_box.add_widget(self.likes)

        self.like_heart = Button(background_normal = 'heart.png')
        self.likes.add_widget(self.like_heart)
        self.like_heart.bind(on_press = self.Like_press)

        self.num_likes = Label (text = (str(nlikes)), size_hint = (1, 1))
        self.likes.add_widget(self.num_likes)

        

    
    
    def Name_press(self, instance):
        pass

    def Image_press(self, instance):
        pass

    def Like_press(self, instance):
        self.post_like = (self.post_like + 1) % 2
        if self.post_like == 1:
            self.like_heart.background_normal = 'heart2.PNG'
        if self.post_like == 0:
            self.like_heart.background_normal = 'heart.PNG' 
        



class MyApp (App):
    def build(self):
        return test()

if __name__ == "__main__":
    MyApp().run()

    