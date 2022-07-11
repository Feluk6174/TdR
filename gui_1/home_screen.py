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
from datetime import datetime
import acces_my_info
import api, register_screen
  

def GetNewPosts():
    all_my_following = acces_my_info.GetFollowing()
    all_posts = []
    for following in all_my_following:
        foll_posts = api.get_posts(following)
        foll_info = api.get_user(following)
        for post in foll_posts:
            all_posts.append((following, foll_info["profile_picture"], post["flags"], post["content"], 0, post["time_posted"]))
    return all_posts

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

def get_post_text(num):
    return str(num)

class MainScreen (Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        self.bind(on_enter = self.checkcheck())

        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.1))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.1, (Window.size[1] - Window.size[0] / 5) * 0.1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        
        
        self.box2 = BoxLayout (size_hint = (1, 0.9))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None, spacing = 3)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)

        self.post_btn_test = Button(size_hint_y = None, height = 100, text = "Refresh Posts", on_release = self.get_my_posts)
        self.grid.add_widget(self.post_btn_test)
        
        #self.get_my_posts(0)

        """
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

        self.new_posts = 7
        for a in range (self.new_posts):
            self.btn_p = Button (size_hint_y = None, height = Window.size[0] / 1.61, text = "P" + (get_post_text(a)))
            self.grid.add_widget(self.btn_p)
        
        #botó per crear posts
        self.btn1 = Button (text = "1", size_hint_y = None, height = 50)
        self.grid.add_widget(self.btn1)
        self.btn1.bind(on_press = partial(self.make_post_btn, "aniol", "foto", "What doesn't kill you makes you stronger." + '\n' + " ~Friedrich Niesche~", 9))
        """

        self.box3 = BoxLayout (size_hint_y = None, height = Window.size[0] / 5)
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
    
    def get_my_posts(self, instance):
        self.all_posts_info = GetNewPosts()
        for post in self.all_posts_info:
            self.make_post_btn(post[0], post[1], post[2], post[3], post[4], post[5])

    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, post_flags, textp, nlikes, date):
    
        self.post = BoxLayout(size_hint_y = None, height = Window.size[0] / 1.61, orientation = "vertical")
        self.grid.add_widget(self.post)
        self.post_like = 0
        
        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
            
        self.im = GridLayout(cols = 8, size_hint_x = None, width = Window.size[0] / 1.61 / 6)
        self.first_box.add_widget(self.im)
        self.BuildImage(user_image)
        
        self.pname = Button(text = user_name)
        self.first_box.add_widget(self.pname)
        self.pname.bind(on_press = partial(self.Name_press))

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

        self.all_flags = [['check_verd.png'], ['age18.png'], ['blood.png'], ['fist.png'], ['soga.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png']]
        for x in range (len(self.all_flags) - 1):
            if post_flags[x] == 1:
                self.f_btn = Button(border = (0, 0, 0, 0), size_hint_x = None, width = (Window.size[1] - Window.size[0] / 5) * 0.9 / 12, background_normal = self.all_flags[x + 1][0])
                #self.all_flags[x + 1].append(self.f_btn)
                #self.all_flags[x + 1].append(0)
                self.flags.add_widget(self.f_btn)

        self.likes = BoxLayout(size_hint = (None, 1), width = Window.size[0] / 1.61 / 3)
        self.third_box.add_widget(self.likes)

        self.like_heart = Button(border = (0, 0, 0, 0),font_size = 1, text = "0", background_normal = 'heart.png')
        self.likes.add_widget(self.like_heart)
        self.like_heart.bind(on_press = self.Like_press)

        self.num_likes = Label (text = (str(nlikes)), size_hint = (1, 1))
        self.likes.add_widget(self.num_likes)
    
    def BuildImage(self, user_image):
        self.color_list = user_image
        self.color_button_list = []
        for x in range (64):
            self.color_bit = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(self.color_list[x])), on_release = self.Image_press)
            self.color_button_list.append(self.color_bit)
            self.im.add_widget(self.color_bit)

    def checkcheck(self):
        my_check = register_screen.check_register()
        if my_check == True: 
            self.get_my_posts(0)

    def Name_press(self, instance):
        pass

    def Image_press(self, instance):
        pass

    def Like_press(self, instance):
        num = int(instance.text)
        num = (num + 1) % 2
        if num == 1:
            instance.background_normal = 'heart2.PNG'
        if num == 0:
            instance.background_normal = 'heart.PNG'
        instance.text = str(num)
        