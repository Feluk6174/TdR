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
from datetime import datetime
from kivy.graphics import BorderImage
from kivy.lang import Builder

import access_my_info


def change_time(date):
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


def build_image(screen, user_image, order_number, width):
    image_grid = GridLayout(cols = 8, size_hint_x = None)
    image_grid.width = width
    for x in range (64):
        color_bit = Button(background_normal = '', background_color = kivy.utils.get_color_from_hex(hex_color(user_image[x])), on_release = partial(screen.image_press, order_number))
        image_grid.add_widget(color_bit)
    return image_grid


#def crear botó
def make_post_btn(screen, user_name, user_image, post_flags, text_content, nlikes, date, post_id, like_self, order_number):
    post = BoxLayout(size_hint_y = None, height = Window.size[0] / 1.61, orientation = "vertical")
        
    post_like = int(like_self)
        
    first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
    post.add_widget(first_box)
            
    image_grid = build_image(screen, user_image, order_number, (Window.size[1]  - Window.size[0] / 5) * 0.9 / 5)
    first_box.add_widget(image_grid)
        
    post_user_name = Button(text = user_name)
    first_box.add_widget(post_user_name)
    post_user_name.bind(on_release = partial(screen.name_press, order_number))

    date = Label(size_hint_x = None, width = Window.size[0] / 1.61 / 3, text = str(change_time(date)))
    first_box.add_widget(date)

    second_box = BoxLayout(size_hint = (1, 2))
    post.add_widget(second_box)

    txt = Button (text = text_content, on_release = partial(screen.content_post_press, order_number))
    second_box.add_widget(txt)

    third_box = BoxLayout(size_hint = (1, 0.5))
    post.add_widget(third_box)

    flags_box = BoxLayout(size_hint = (1, 1))
    third_box.add_widget(flags_box)

    all_flags = [['images/check_verd.png'], ['images/age18.png'], ['images/blood.png'], ['images/fist.png'], ['images/soga.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png'], ['images/white.png']]
    for x in range (len(all_flags) - 1):
        if post_flags[x] == "1":
            flag_btn = Button(border = (0, 0, 0, 0), size_hint_x = None, width = (Window.size[1] - Window.size[0] / 5) * 0.9 / 12, background_normal = all_flags[x + 1][0])
            #all_flags[x + 1].append(f_btn)
            #all_flags[x + 1].append(0)
            flags_box.add_widget(flag_btn)

    likes_box = BoxLayout(size_hint = (None, 1), width = Window.size[0] / 1.61 / 3)
    third_box.add_widget(likes_box)

    like_heart = Button(border = (0, 0, 0, 0))
    if post_like == 0:
        like_heart.background_normal = 'images/heart.png'
    if post_like == 1:
        like_heart.background_normal = 'images/heart2.png'
    likes_box.add_widget(like_heart)
    like_heart.bind(on_release = partial(screen.like_press, order_number))

    num_likes = Label (text = (str(nlikes)), size_hint = (1, 1))
    likes_box.add_widget(num_likes)

    return post


def add_liked_or_unliked_post(post_id, like_or_not):
    #change in server (api) and in my info (acces_my_info)
    access_my_info.add_or_remove_liked_post(post_id, like_or_not)
    pass

def order_posts_by_timestamp(posts_to_order):
    length = len(posts_to_order)
    how_big_list = []
    final_list = []
    for a in range (length):
        how_big_list.append([0, 0])
        for b in range (length):
            if posts_to_order[a]["time_stamp"] > posts_to_order[b]["time_stamp"]:
                how_big_list[a][1] = how_big_list[a][1] + 1
            elif posts_to_order[a]["time_stamp"] < posts_to_order[b]["time_stamp"]:
                how_big_list[a][0] = how_big_list[a][0] + 1
    for c in range (length):
        for d in range (length):
            if how_big_list[c][0] == d:
                final_list.append(posts_to_order[c])
    return final_list


def check_new_chat_alarm():
    pass

def change_my_description(description):
    access_my_info.change_my_description(description)
    #enviar a conn

def change_my_profile_image(color_string):
    access_my_info.change_my_image(color_string)
    #enviar a conn


def adapt_text_to_window(text, text_size, window_size):
    text_to_cut_lenght = len(text)
    letters_per_line = window_size / text_size
    jump_done = 0
    while text_to_cut_lenght > letters_per_line:
        for x in range (letters_per_line):
            if text[len(text) - text_to_cut_lenght + letters_per_line - x -1] == " ":
                if jump_done == 0:
                    jump_done = 1
                    text[letters_per_line - x -1] = "\n"
                    text_to_cut_lenght = text_to_cut_lenght - letters_per_line - x -1
