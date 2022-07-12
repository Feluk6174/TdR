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
import json
import random
import acces_my_info

api = None

def SendPostFinal(postflags, textp, nlikes):
    global api
    content = textp
    user_name = acces_my_info.GetName()
    post_flags = str(postflags)
    #post_likes = nlikes
    #date = int(time.time())
    post_id = hash(str(content) + str(user_name) + str(post_flags))
    api.post(content, post_id, user_name, post_flags)

class PostUserScreen (Screen):
    def __init__(self, connection, **kwargs):
        super(PostUserScreen, self).__init__(**kwargs)
        global api
        api = connection
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
        
        self.grid = BoxLayout(orientation = "vertical")
        self.box2.add_widget(self.grid)

        self.actp = TextInput(multiline = True, size_hint = (1, 3.5))
        self.grid.add_widget(self.actp)

        self.actp2 = TextInput(multiline = False, size_hint = (1, 0.5), text = "")
        self.grid.add_widget(self.actp2)

        self.actp3 = TextInput(multiline = False, size_hint = (1, 0.5), text = "")
        self.grid.add_widget(self.actp3)

        self.flag_box = BoxLayout(size_hint = (1, 0.5))
        self.grid.add_widget(self.flag_box)

        #flags
        #self.fl_bt = Button(text = "flags to add")
        #self.flag_box.add_widget(self.fl_bt)

        self.grid2 = GridLayout(rows = 1, size_hint_x = None, spacing = 1)
        self.grid2.bind(minimum_width=self.grid2.setter('width'))
        
        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid2)
        self.flag_box.add_widget (self.scroll)

        self.all_flags = [['check_verd.png'], ['age18.png'], ['blood.png'], ['fist.png'], ['soga.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png'], ['white.png']]
        for d in range(len(self.all_flags) - 1):
            self.all_flags[d + 1].append(str(d + 1))
        for x in range (len(self.all_flags) - 1):
            self.f_btn = Button(border = (0, 0, 0, 0), font_size = 1, size_hint_x = None, width = (Window.size[1] - Window.size[0] / 5) * 0.9 / 12, text = str(self.all_flags[x + 1][1]), on_release = self.Flag_press, background_normal = self.all_flags[x + 1][0])
            self.all_flags[x + 1].append(self.f_btn)
            self.all_flags[x + 1].append(0)
            self.grid2.add_widget(self.f_btn)
            
        self.send = Button (text = "Publish", size_hint = (1, 1))
        self.grid.add_widget(self.send)
        self.send.bind(on_press = self.SendPost)

        #self.last = Button (text = "All your posts", size_hint = (1, 0.67))
        #self.grid.add_widget(self.last)
        #self.last.bind(on_press = self.LastPosts)


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

        self.btn14 = Label (text = ("Post"))
        self.box3.add_widget(self.btn14)

        self.btn15 = Button (text = ("U"))
        self.box3.add_widget(self.btn15)
        self.btn15.bind(on_press = self.press_btn15)

    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass
    
    def Flag_press(self, instance):
        flag = int(instance.text)
        self.all_flags[flag][3] = (self.all_flags[flag][3] + 1) % 2
        if self.all_flags[flag][3] == 1:
            instance.background_normal = self.all_flags[0][0]
        if self.all_flags[flag][3] == 0:
            instance.background_normal = self.all_flags[flag][0]

    def SendPost(self, instance):
        global api
        self.flag_list = ""
        for y in range (len(self.all_flags) - 1):
            self.flag_list = self.flag_list + str(self.all_flags[y + 1][3])
        SendPostFinal(self.flag_list, str(self.actp.text) + ". " + str(self.actp2.text) + ". " + str(self.actp3.text), 0)
        self.actp.text = ""
        self.actp2.text = ""
        self.actp3.text = ""
        for y in range (len(self.all_flags) - 1):
            if self.all_flags[y + 1][3] == 1:
                self.all_flags[y + 1][2].trigger_action(duration = 0)
        
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
        pass

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"
