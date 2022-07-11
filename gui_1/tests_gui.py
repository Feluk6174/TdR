#import kivy
from kivy.app import App
from functools import partial
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
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
from kivy.graphics import BorderImage
from kivy.lang import Builder


Window.size = (300, 600)

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

class test(BoxLayout):
    def __init__(self, **kwargs):
        super(test, self).__init__(**kwargs)

        self.box0 = BoxLayout(orientation = "vertical")
        self.add_widget(self.box0)

        self.box01 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box01)

        self.box2 = BoxLayout()
        self.box01.add_widget(self.box2)

        self.box1 = GridLayout(spacing = 5, cols = 8, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box01.add_widget(self.box1)

        self.color_list = []
        for x in range (64):
            self.color_list.append("0")

        for y in range (64):
            self.btn = Button(background_normal = '', font_size = 1, text = str(y), background_color = (1, 1, 1, 1), on_press = self.button_1)
            self.box1.add_widget(self.btn)

        self.box3 = BoxLayout()
        self.box01.add_widget(self.box3)

    
        self.box02 = BoxLayout()
        self.box0.add_widget(self.box02)


        self.box03 = BoxLayout(size_hint_y = None, height = Window.size[0] * 0.7, orientation = "horizontal")
        self.box0.add_widget(self.box03)

        self.box4 = BoxLayout()
        self.box03.add_widget(self.box4)

        self.box5 = GridLayout(cols = 4, size_hint = (None, None), size = (Window.size[0] * 0.7, Window.size[0] * 0.7))
        self.box03.add_widget(self.box5)

        self.all_colors = [("0", '#1B1A1A'), ("1", '#7e7e7e'), ("2", '#bebebe'), ("3", '#ffffff'), ("4", '#7e0000'), ("5", '#fe0000'), ("6", '#047e00'), ("7", '#06ff04'), ("8", '#7e7e00'), ("9", '#ffff04'), ("A", '#00007e'), ("B", '#0000ff'), ("C", '#7e007e'), ("D", '#fe00ff'), ("E", '#047e7e'), ("F", '#06ffff')]

        for x in range (len(self.all_colors)):
            self.btn1 = Button(border = (0, 0, 0, 0), background_normal = '', font_size = 1, text = str(x), background_color = kivy.utils.get_color_from_hex(self.all_colors[x][1]), on_press = self.button_2)
            self.box5.add_widget(self.btn1)

        self.box6 = BoxLayout()
        self.box03.add_widget(self.box6)

        self.actual_btn1 = self.btn
        self.actual_btn2 = self.btn1

    def button_1(self, instance):
        instance.background_color = self.actual_btn2.background_color
        self.color_list.append(self.all_colors[int(self.actual_btn2.text)][0])
        self.actual_btn1 = instance

    def button_2(self, instance):
        self.actual_btn2.background_normal = ""
        instance.background_normal = "check_verd.png"
        self.actual_btn2 = instance
        """
        self.orientation = "vertical"

        self.all_posts_info = []
        for post in self.all_posts_info:
            self.make_post_btn(post["username"], post["userimage"], post["posttext"], post["postlikes"], post["postdate"])
        
        self.anch_lay = AnchorLayout(size_hint = (0.7, 0.7), anchor_x = "center", anchor_y = "center")
        self.add_widget(self.anch_lay)

        #self.grid = GridLayout(cols = 8, size_hint = (None, None), size = (30, 30))
        #self.anch_lay.add_widget(self.grid)

        self.grid = GridLayout(cols = 8)
        self.anch_lay.add_widget(self.grid)
        
        self.box1 = BoxLayout()
        self.grid.add_widget(self.box1)
        
        self.box2 = BoxLayout()
        self.grid.add_widget(self.box2)
        
        self.box3 = BoxLayout()
        self.grid.add_widget(self.box3)
        
        self.box4 = BoxLayout()
        self.grid.add_widget(self.box4)

        self.box5 = BoxLayout()
        self.grid.add_widget(self.box5)
        
        self.box6 = BoxLayout()
        self.grid.add_widget(self.box6)
        
        self.box7 = BoxLayout()
        self.grid.add_widget(self.box7)
        
        self.box8 = BoxLayout()
        self.grid.add_widget(self.box8)
        

        #self.color_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "5", "6", "7", "8", "1", "2", "3", "4", "9", "0", "A", "B", "D", "E", "F", "5", "5", "6", "7", "8", "1", "2", "3", "4", "6", "7", "8", "9", "0", "A", "B", "C", "6", "7", "8", "1", "2", "3", "4", "6", "8", "1", "2", "3", "4", "9", "0", "A"]
        
        #self.BuildImage()

    def BuildImage(self):
        #self.color_list = self.color_list
        self.color_button_list = []
        for x in range (64):
            self.color_bit = Button(border = (10, 10, 10, 10), background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(self.color_list[x])))
            self.color_button_list.append(self.color_bit)
            self.grid.add_widget(self.color_bit)
            
            
            if x < 8:
                self.box1.add_widget(self.color_bit)
            elif x  > 7 and x < 16:
                self.box2.add_widget(self.color_bit)
            elif x  > 15 and x < 24:
                self.box3.add_widget(self.color_bit)
            elif x  > 23 and x < 32:
                self.box4.add_widget(self.color_bit)
            elif x  > 31 and x < 40:
                self.box5.add_widget(self.color_bit)
            elif x  > 39 and x < 48:
                self.box6.add_widget(self.color_bit)
            elif x  > 47 and x < 56:
                self.box7.add_widget(self.color_bit)
            elif x  > 55 and x < 64:
                self.box8.add_widget(self.color_bit)
            """


        #self.make_post_btn("aniol", 0, "Hello World", 10, "14/3/1984")


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

    