from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import json
import api
import random
import rsa_gui
import acces_my_info
from kivy.uix.screenmanager import FallOutTransition


def Reg_f():
        user_name = acces_my_info.GetName()
        public_key = acces_my_info.GetPubKey()
        private_key = acces_my_info.GetPubKey()     
        profile_picture = acces_my_info.GetImage()
        info = acces_my_info.GetDescription()
        api.register_user(user_name, public_key, profile_picture, info)

def check_register():
    my_user_info = json.loads(open("my_info.json", "r").read())
    if my_user_info == "":
        return False
    else:
        return True

    

def create_my_info_file(username, password, pub_key, priv_key, image, description, following):
    dictionary = {}
    dictionary["basic_info"]["user_name"] = username
    dictionary["basic_info"]["password"] = password
    dictionary["basic_info"]["user_pub_key"] = pub_key
    dictionary["basic_info"]["user_priv_key"] = priv_key
    dictionary["semi_basic_info"]["profile_image"] = image
    dictionary["semi_basic_info"]["description"] = description
    dictionary["semi_basic_info"]["user_following"] = following
    my_info_file = open("my_info.json", "w")
    my_info_file.write(dictionary)
    my_info_file.close
    

def check_password(word):
    #min_letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    #max_letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    #num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #special_caracters = ["!", "#", "$", "%", "&", "*", "?", "+", "-", "_", "º", "ª", "|", "@", "·", "~", "¬", "(", ")", "¿", "¡", "[", "]", "{", "}", "^", "<", ">"]
    min_letters = "qwertyuiopasdfghjklzxcvbnm"
    max_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    num = "01234567889"
    special_caracters = "!|@·#$~%&/()?^[]+*-_<>"
    word_cheme = []
    for _ in range (len(word)):
        word_cheme.append(0)
    for l in range (len(min_letters)):
        for p in range (len(word)):
            if min_letters[l] == word[p]:
                word_cheme[p] = 1
    for l in range (len(max_letters)):
        for p in range (len(word)):
            if max_letters[l] == word[p]:
                word_cheme[p] = 2
    for l in range (len(num)):
        for p in range (len(word)):
            if num[l] == word[p]:
                word_cheme[p] = 3
    for l in range (len(special_caracters)):
        for p in range (len(word)):
            if special_caracters[l] == word[p]:
                word_cheme[p] = 4
    if not 0 in word_cheme:
        if 1 in word_cheme and 2 in word_cheme and 3 in word_cheme and 4 in word_cheme:
            final_truth = True
    else:
        final_truth = False
    return final_truth
    
def check_image(image):
    all_hex = "0123456789ABCDEF"
    check_list = 0
    if len(image) == 64:
        for a in range (len(all_hex)):
            for b in range (len(image)):
                if all_hex[a] == image[b]:
                    check_list = check_list + 1
    elif check_list == 64:
        final = True
    elif check_list != 64:
        final = False
    return final


class RegisterScreen (Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.main_box = BoxLayout()
        self.main_box.orientation = "vertical"
        self.add_widget(self.main_box)

        self.title_box = BoxLayout(size_hint=(1, 1))
        self.title_box.orientation = "horizontal"
        self.main_box.add_widget(self.title_box)

        self.logo = Button (border = (0, 0, 0, 0), size_hint = (None, None), size = ((Window.size[1] - Window.size[0] / 5) * 0.2, (Window.size[1] - Window.size[0] / 5) * 0.2), background_normal = 'logo.png', background_down = 'logo.png')
        self.title_box.add_widget(self.logo)
        
        self.title = Label (text = ("Small brother"))
        self.title_box.add_widget(self.title)

        self.username_password_box = BoxLayout(size_hint = (1, 1), orientation = "vertical")
        self.main_box.add_widget(self.username_password_box)

        self.username_text_box = TextInput(size_hint = (1, 1), text = "username")
        self.username_password_box.add_widget(self.username_text_box)

        self.password_text_box = TextInput(size_hint = (1, 1), text = "password")
        self.username_password_box.add_widget(self.password_text_box)

        self.profile_image_box = BoxLayout(size_hint = (1, 1))
        self.main_box.add_widget(self.profile_image_box)
        
        self.profile_image_text_box = TextInput(size_hint = (1, 1), text = "profile image")
        self.profile_image_box.add_widget(self.profile_image_text_box)

        self.description_box = BoxLayout(size_hint = (1, 2))
        self.main_box.add_widget(self.description_box)
        
        self.description_text_box = TextInput(size_hint = (1, 1), text = "description")
        self.description_box.add_widget(self.description_text_box)

        self.following_box = BoxLayout(size_hint = (1, 1))
        self.main_box.add_widget(self.following_box)
        
        self.following_text_box = TextInput(size_hint = (1, 1), text = "following")
        self.following_box.add_widget(self.following_text_box)

        self.register_box = BoxLayout(size_hint = (1, 1))
        self.main_box.add_widget(self.register_box)
        
        self.register_button = Button(size_hint = (1, 1), text = "Register")
        self.register_box.add_widget(self.register_button)
        self.register_button.bind(on_release = self.register)

    
    def register(self):
        self.other_users = api.get_user(self.username_text_box.text)
        if self.other_users != {}:
            self.username_text_box.text = "USERNAME"
            self.register_button.text = "Register. Try again"
        elif self.other_users == {}:
            self.password_check = check_password(self.password_text_box.text)
            self.color_check = check_image(self.profile_image_text_box)
            if self.password_check == False:
                self.password_text_box.text = "PASSWORD"
                self.register_button.text = "Register. Try again"
            elif self.color_check == False:
                self.profile_image_text_box.text = "PROFILE IMAGE"
                self.register_button.text = "Register. Try again"
            elif self.password_check == True and self.color_check == True:
                rsa_gui.gen_key(self.username_text_box.text, self.password_text_box.text)
                following = self.following_text_box.text.split(", ")
                create_my_info_file(self.username_text_box.text, self.password_text_box.text, "pub_my_key_storage.pem", "priv_my_key_storage.pem", self.profile_image_text_box.text, self.description_text_box.text, following)
                Reg_f()
                self.manager.transition = FallOutTransition()
                self.manager.current = "main"