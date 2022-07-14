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
import auth, api

def change_my_color(col_str):
    my_user_info = json.loads(open("my_info.json", "r").read())
    my_user_info["semi_basic_info"]["profile_image"] = col_str
    file_my = open("my_info.json", "w")
    file_my.write(json.dumps(my_user_info))
    file_my.close()
    #cal enviar-ho

def change_my_description(description):
    my_user_info = json.loads(open("my_info.json", "r").read())
    my_user_info["semi_basic_info"]["description"] = description
    file_my = open("my_info.json", "w")
    file_my.write(json.dumps(my_user_info))
    file_my.close()
    #cal enviar-ho

def add_liked_post(post_id):
    my_user_info = json.loads(open("my_info.json", "r").read())
    my_user_info["semi_basic_info"]["liked_posts"].append(post_id)
    file_my = open("my_info.json", "w")
    file_my.write(json.dumps(my_user_info))
    file_my.close()
    #cal enviar-ho

def Get(num):
    try:
        my_user_info = json.loads(open("my_info.json", "r").read())
    except FileNotFoundError:
        my_user_info = ""

    username = my_user_info["basic_info"]["user_name"]
    password = my_user_info["basic_info"]["password"]
    profileimage = my_user_info["semi_basic_info"]["profile_image"]
    public_key, private_key = auth.get_keys(username + password)
    user_description = my_user_info["semi_basic_info"]["description"]
    user_following = my_user_info["semi_basic_info"]["user_following"]
    user_following = my_user_info["semi_basic_info"]["user_following"]
    user_liked_id = my_user_info["semi_basic_info"]["liked_posts"]
    user_liked = []
    for post in user_liked_id:
        actual_liked = api.get_post(post)
        user_liked.append(actual_liked)


    if num == 0:
        return username
    if num == 1:
        return profileimage
    if num == 2:
        return public_key
    if num == 3:
        return private_key
    if num == 4:
        return user_description
    if num == 5:
        return user_following
    if num == 6:
        return password
    if num == 7:
        return user_liked

def GetName():
    return Get(0)
def GetImage():
    return Get(1)
def GetPubKey():
    return Get(2)
def GetPrivKey():
    return Get(3)
def GetDescription():
    return Get(4)
def GetFollowing():
    return Get(5)
def GetPassword():
    return Get(6)
def GetLiked():
    return Get(7) 
