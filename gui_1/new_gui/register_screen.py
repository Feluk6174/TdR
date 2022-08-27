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
import register_screen
import random
from datetime import datetime
from kivy.graphics import BorderImage
from kivy.lang import Builder

import user_image_register_screen, auth, home_screen, search_screen, chat_screen, create_post_screen, profile_screen, user_image_screen, acces_my_info


def check_my_info_exists():
    try:
        my_user_info = json.loads(open("my_info.json", "r").read())
        return True
    except FileNotFoundError:
        return False

def check_my_user_exists(connection):
    my_user_info = json.loads(open("my_info.json", "r").read())
    username = my_user_info["basic_info"]["username"]
    check = check_user_exists(connection, username)
    return check

def check_user_exists(connection, user):
    check_user = connection.get_user(user)
    if check_user != {}:
        return True
    elif check_user == {}:
        return False

#gotta change this!!!!!!!!!!!!!
def register(connection):
    user_name = acces_my_info.GetName()
    public_key = acces_my_info.GetPubKey()
    profile_picture = acces_my_info.GetImage()
    info = acces_my_info.GetDescription()
    connection.register_user(user_name, public_key, "rsa_key.bin", profile_picture, info)

class RegisterScreen (Screen):
    def __init__(self, conn, sm, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

        #import info
        self.connection = conn
        self.sm = sm
        

        #llista imatges de fons ((inicials)
        self.my_list_of_background_images = ['images/username_register.png', 'images/password_register.png', 'images/repeat_password_register.png', 'images/description_register.png', 'images/following_register.png']

        self.main_box = BoxLayout()
        self.main_box.orientation = "vertical"
        self.add_widget(self.main_box)

        #titel
        self.title_box = BoxLayout(size_hint=(1, 1))
        self.title_box.orientation = "horizontal"
        self.main_box.add_widget(self.title_box)

        self.logo = Button (border = (0, 0, 0, 0), size_hint_x = None, width = Window.size[1] / 8, background_normal = 'images/logo.png', background_down = 'images/logo.png')
        self.title_box.add_widget(self.logo)
        
        self.title = Label (text = ("Small brother"))
        self.title_box.add_widget(self.title)

        #cos de la pantalla. text inputs i boto
        self.username_text_input = TextInput(size_hint = (1, 1), multiline = False, background_normal = self.my_list_of_background_images[0], keyboard_on_key_down = self.username_text_input_background_image_f)
        self.main_box.add_widget(self.username_text_input)

        self.password_text_input = TextInput(size_hint = (1, 1), multiline = False, background_normal = self.my_list_of_background_images[1], password = True, keyboard_on_key_down = self.password_text_input_background_image_f)
        self.main_box.add_widget(self.password_text_input)

        self.repeat_password_text_input = TextInput(size_hint = (1, 1), multiline = False, background_normal = self.my_list_of_background_images[2], password = True, keyboard_on_key_down = self.repeat_password_text_input_background_image_f)
        self.main_box.add_widget(self.repeat_password_text_input)
        
        self.image_button = Button(text = "Make your profile image", on_press = self.to_image_making)
        self.main_box.add_widget(self.image_button)
        
        self.description_text_input = TextInput(size_hint = (1, 2), multiline = False, background_normal = self.my_list_of_background_images[3], keyboard_on_key_down = self.description_text_input_background_image_f)
        self.main_box.add_widget(self.description_text_input)
        
        self.following_text_input = TextInput(size_hint = (1, 1), multiline = False, background_normal = self.my_list_of_background_images[4], keyboard_on_key_down = self.following_text_input_background_image_f)
        self.main_box.add_widget(self.following_text_input)
        
        self.register_button = Button(size_hint = (1, 1), text = "Register")
        self.main_box.add_widget(self.register_button)
        self.register_button.bind(on_release = self.register)
        
    #creem o modifiquem la imatge de perfil 
    def to_image_making(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "image_register"
    
    #funcions per que al deixar de seleccionar una casella hi hagi el fons corresponent
    def following_text_input_background_image_f(self, instance):
        if self.following_text_input.text != "":
            self.following_text_input.background_normal = 'atlas://data/images/defaulttheme/textinput'
        elif self.following_text_input.text == "":
            self.following_text_input.background_normal = self.my_list_of_background_images[4]
         
    def description_text_input_background_image_f(self, instance):
        if self.description_text_input.text != "":
            self.description_text_input.background_normal = 'atlas://data/images/defaulttheme/textinput'
        if self.description_text_input.text == "":
            self.description_text_input.background_normal = self.my_list_of_background_images[3]

    def repeat_password_text_input_background_image_f(self, instance):
        if self.password_text_input.text != "":
            self.password_text_input.background_normal = 'atlas://data/images/defaulttheme/textinput'
        elif self.password_text_input.text == "":
            self.password_text_input.background_normal = self.my_list_of_background_images[2]

    def password_text_input_background_image_f(self, instance):
        if self.password_text_input.text != "":
            self.password_text_input.background_normal = 'atlas://data/images/defaulttheme/textinput'
        elif self.password_text_input.text == "":
            self.password_text_input.background_normal = self.my_list_of_background_images[1]

    def username_text_input_background_image_f(self, instance):
        if self.username_text_input.text != "":
            self.username_text_input.background_normal = 'atlas://data/images/defaulttheme/textinput'
        elif self.username_text_input.text == "":
            self.username_text_input.background_normal = self.my_list_of_background_images[0]
    
    #register user f
    def register(self, instance):

        #comprovar username, password i image que son correctes
        self.other_users = check_user_exists(self.connection, self.username_text_input.text)
        if self.other_users == True:
            self.my_list_of_background_images[0] = 'images/username_2_register.png'
            self.username_text_input.text = ""
            self.register_button.text = "Register. Sorry, try again"
        elif self.other_users == False:
            self.password_check = self.check_password()
            self.image_str = user_image_register_screen.get_my_image()
            self.color_check = self.check_image()
            if self.password_check == False or self.password_text_input.text != self.repeat_password_text_input.text:
                self.my_list_of_background_images[1] = 'images/password_2_register.png'
                self.password_text_input.text = ""
                self.my_list_of_background_images[2] = 'images/repeat_password_2_register.png'
                self.repeat_password_text_input.text = ""
                self.register_button.text = "Register. Sorry, try again"
            elif self.color_check == False:
                self.image_button.text = "MAKE YOUR PROFILE IMAGE!"
                self.register_button.text = "Register. Sorry, try again"
            if self.password_check == True and self.color_check == True and self.password_text_input.text == self.repeat_password_text_input.text:

                #guardar la informacio
                self.username_text = self.username_text_input.text
                self.password_text = self.password_text_input.text
                self.description_text = self.description_text_input.text
                self.following_text = self.following_text_input.text
                self.following_list = self.following_text.split(", ")

                #crear pantalla d'espera
                self.clear_widgets()
                self.main_box_load = BoxLayout(orientation = "vertical")
                self.add_widget(self.main_box_load)

                self.black_box_1_load = BoxLayout(size_hint_y = None, height = (Window.size[0] * 0.2))
                self.main_box_load.add_widget(self.black_box_1_load)

                self.logo_load = Button(border = (0, 0, 0, 0), size_hint = (None, None), background_normal = 'images/logo.png', background_down = 'images/logo.png', size = (Window.size[0] * 0.7, Window.size[0] * 0.7), pos_hint = {"center_x":0.5})   
                self.main_box_load.add_widget(self.logo_load)

                self.text_load = Label(text = "Creating user...", size_hint = (1, 0.12))
                self.main_box_load.add_widget(self.text_load)

                self.create_user()

    #creating user keys and starting session
    def create_user(self):
        #create public and private key
        auth.gen_key(self.username_text + self.password_text)
        
        #create jso file with my new info
        self.create_my_info_file()
        #registrate_user
        con = self.connection
        register(con)
        #create (add) the rest of the main screens
        my_profile_screen = profile_screen.ProfileScreen(con, name = "profile")
        self.sm.add_widget(home_screen.MainScreen(con, name = "main"))
        self.sm.add_widget(chat_screen.ChatScreen(name = "chat"))
        self.sm.add_widget(search_screen.SearchScreen(name = "search"))
        self.sm.add_widget(create_post_screen.PostUserScreen(con, name = "last"))
        self.sm.add_widget(my_profile_screen)
        self.sm.add_widget(user_image_screen.ImageScreen(my_profile_screen, name = "image"))
        self.manager.transition = FallOutTransition()
        self.manager.current = "main"
    
    def create_my_info_file(self):
        dictionary = {}
        dictionary["basic_info"] = {}
        dictionary["semi_basic_info"] = {}
        dictionary["basic_info"]["user_name"] = self.username_text
        dictionary["basic_info"]["password"] = self.password_text
        #dictionary["basic_info"]["user_pub_key"] = pub_key
        #dictionary["basic_info"]["user_priv_key"] = priv_key
        #dictionary["basic_info"]["user_key_storage"] = "rsa_key.bin"
        dictionary["semi_basic_info"]["profile_image"] = self.image_str
        dictionary["semi_basic_info"]["description"] = self.description_text
        dictionary["semi_basic_info"]["user_following"] = self.following_list
        dictionary["semi_basic_info"]["liked_posts"] = []
        my_info_file = open("my_info.json", "w")
        my_info_file.write(json.dumps(dictionary))
        my_info_file.close
    
    def check_password(self):
        word = self.password_text_input.text

        #characters to include
        minuscule_letters = "qwertyuiopasdfghjklzxcvbnm"
        majuscule_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numbers = "01234567889"
        special_caracters = "!|@·#$~%&/()?^[]+*_<>€"
        
        #list of character types in password
        word_cheme = []

        #check if each character type is in the password
        for _ in range (len(word)):
            word_cheme.append(0)
        for l in range (len(minuscule_letters)):
            for p in range (len(word)):
                if minuscule_letters[l] == word[p]:
                    word_cheme[p] = 1
        for l in range (len(majuscule_letters)):
            for p in range (len(word)):
                if majuscule_letters[l] == word[p]:
                    word_cheme[p] = 2
        for l in range (len(numbers)):
            for p in range (len(word)):
                if numbers[l] == word[p]:
                    word_cheme[p] = 3
        for l in range (len(special_caracters)):
            for p in range (len(word)):
                if special_caracters[l] == word[p]:
                    word_cheme[p] = 4
        if not 0 in word_cheme:

            #check if uses all character types
            if 1 in word_cheme and 2 in word_cheme and 3 in word_cheme and 4 in word_cheme:
                return True
            else:
                return False
        else:
            return False

    def check_image(self):
        image = self.image_str

        #hexadecimal characters
        all_hexadecimal_characters = "0123456789ABCDEF"

        #number that counts correct characters
        check_characters = 0
        if len(image) == 64:
            for a in range (len(all_hexadecimal_characters)):
                for b in range (len(image)):
                    if all_hexadecimal_characters[a] == image[b]:
                        check_characters = check_characters + 1
        
        #check all characters are correct
        if check_characters == 64:
            return True
        if check_characters != 64:
            return False

