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


my_user_info = json.loads(open("my_info.json", "r").read())
username = my_user_info["basic_info"]["user_name"]
password = my_user_info["basic_info"]["password"]
profileimage = my_user_info["semi_basic_info"]["profile_image"]
user_pub_key = my_user_info["basic_info"]["user_pub_key"]
public_key = json.loads(open(user_pub_key, "r").read())
user_priv_key = my_user_info["basic_info"]["user_priv_key"]
private_key = json.loads(open(user_priv_key, "r").read())
user_description = my_user_info["semi_basic_info"]["description"]
user_following = my_user_info["semi_basic_info"]["user_following"]

def GetName():
    return username
def GetImage():
    return profileimage
def GetPubKey():
    return public_key
def GetPrivKey():
    return private_key
def GetDescription():
    return user_description
def GetFollowing():
    return user_following
def GetPassword():
    return password  