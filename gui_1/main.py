#import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
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

Window.size = (400, 600)



def get_post_text(a):
    return str(a)
    #random.randint(0, a+1)


class LoadScreen (Screen):
    def __init__(self, **kwargs):
        super(LoadScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.lab1 = Button(size_hint = (None, None), size = (300, 300), background_normal = 'logo.png', background_down = 'logo.png')
        self.Box0.add_widget(self.lab1)

        self.lab2 = Label(text = "Small Brother", size_hint = (1, 0.12))
        self.Box0.add_widget(self.lab1)

        time.sleep(3)
        self.manager.current = "chat"






class ChatScreen (Screen):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        for a in range (20):
            self.btn = Button (size_hint_y = None, height = 80, text = "A" + (get_post_text(a)))
            self.grid.add_widget(self.btn)

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box3)

        self.btn11 = Label (text = ("Chat"))
        self.box3.add_widget(self.btn11)

        self.btn12 = Button (text = ("S"))
        self.box3.add_widget(self.btn12)
        self.btn12.bind(on_press = self.press_btn12)

        self.btn13 = Button (text = ("H"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

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
        pass

    def press_btn12(self, instance):
        self.manager.current = "search"
        self.manager.transition.direction = "left"

    def press_btn13(self, instance):
        self.manager.current = "main"
        self.manager.transition.direction = "left"

    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"





class SearchScreen (Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.box2.add_widget(self.grid)

        self.lab1 = TextInput(multiline = False, text = "Search post")
        self.grid.add_widget(self.lab1)
        self.lab1.bind(on_text_validate = self.search11)

        self.lab2 = TextInput(multiline = False, text = "Search user")
        self.grid.add_widget(self.lab2)
        self.lab2.bind(on_text_validate = self.search12)

        self.lab3 = TextInput(multiline = False, text = "Favourites")
        self.grid.add_widget(self.lab3)
        self.lab2.bind(on_text_validate = self.search13)

        self.ran1 = Button (text = "Global", size_hint = (1, 2.5))
        self.grid.add_widget(self.ran1)
        self.ran1.bind(on_press = self.random1)

        self.ran2 = Button (text = "Random", size_hint = (1, 1))
        self.grid.add_widget(self.ran2)
        self.ran2.bind(on_press = self.random2)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box3)

        self.btn11 = Button (text = ("C"))
        self.box3.add_widget(self.btn11)
        self.btn11.bind(on_press = self.press_btn11)

        self.btn12 = Label (text = ("Search"))
        self.box3.add_widget(self.btn12)
        
        self.btn13 = Button (text = ("H"))
        self.box3.add_widget(self.btn13)
        self.btn13.bind(on_press = self.press_btn13)

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

    def search11(instance, value):
        pass

    def search12(instance, value):
        pass

    def search13(instance, value):
        pass

    def random1(self, instance):
        pass

    def random2(self, instance):
        pass

    def press_btn11(self, instance):
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        pass

    def press_btn13(self, instance):
        self.manager.current = "main"
        self.manager.transition.direction = "left"


    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"
    

class MainScreen (Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        for a in range (20):
            self.btn = Button (size_hint_y = None, height = 100, text = "P" + (get_post_text(a)))
            self.grid.add_widget(self.btn)

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)


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
        self.manager.current = "chat"
        self.manager.transition.direction = "right"

    def press_btn12(self, instance):
        self.manager.current = "search"
        self.manager.transition.direction = "right"

    def press_btn13(self, instance):
        pass

    def press_btn14(self, instance):
        self.manager.current = "last"
        self.manager.transition.direction = "left"

    def press_btn15(self, instance):
        self.manager.current = "profile"
        self.manager.transition.direction = "left"



class PostUserScreen (Screen):
    def __init__(self, **kwargs):
        super(PostUserScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 0.9))
        self.Box0.add_widget(self.box2)
        
        self.grid = BoxLayout(orientation = "vertical")
        self.box2.add_widget(self.grid)

        self.actp = TextInput(multiline = True, size_hint = (1, 4))
        self.grid.add_widget(self.actp)
        self.actp.bind(on_text_validate = self.NotYet)

        self.send = Button (text = "Publish", size_hint = (1, 1))
        self.grid.add_widget(self.send)
        self.send.bind(on_press = self.SendPost)

        self.last = Button (text = "All your posts", size_hint = (1, 0.67))
        self.grid.add_widget(self.last)
        self.last.bind(on_press = self.LastPosts)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
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

    def NotYet(instance, value):
        pass

    def SendPost(self, instance):
        pass

    def LastPosts(self, instance):
        pass

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



class ProfileScreen (Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.Box0 = BoxLayout()
        self.Box0.orientation = "vertical"
        self.add_widget(self.Box0)

        self.box1 = BoxLayout (size_hint = (1, 0.15))
        self.Box0.add_widget(self.box1)

        self.lab1 = Button (size_hint = (None, None), size = (80, 80), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)
        
        self.us_name = Button(text = "Name", size_hint_y = None, height = 120)
        self.grid.add_widget(self.us_name)
        self.us_name.bind(on_press = self.UserName)

        self.us_image = Button(text = "Profile", size_hint_y = None, height = 200)
        self.grid.add_widget(self.us_image)
        self.us_image.bind(on_press = self.UserImage)

        self.us_des = Button(text = "Description", size_hint_y = None, height = 90)
        self.grid.add_widget(self.us_des)
        self.us_des.bind(on_press = self.UserDescription)

        self.us_followers = Button(text = "Followers", size_hint_y = None, height = 80)
        self.grid.add_widget(self.us_followers)
        self.us_followers.bind(on_press = self.UserFollowers)

        self.us_following = Button(text = "Following", size_hint_y = None, height = 80)
        self.grid.add_widget(self.us_following)
        self.us_following.bind(on_press = self.UserFollowing)

        self.us_posts = Button(text = "Posts", size_hint_y = None, height = 80)
        self.grid.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.UserPosts)

        self.settings_final = Button(text = "Settings", size_hint_y = None, height = 80)
        self.grid.add_widget(self.settings_final)
        self.settings_final.bind(on_press = self.FinalSettings)


        self.box3 = BoxLayout (size_hint = (1, 0.15))
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

        self.btn14 = Button (text = ("P"))
        self.box3.add_widget(self.btn14)
        self.btn14.bind(on_press = self.press_btn14)

        self.btn15 = Label (text = ("User"))
        self.box3.add_widget(self.btn15)
        

    def Search1(instance, value):
        pass

    def Settings(self, instance):
        pass

    def UserName(self, instance):
        pass

    def UserImage(self, instance):
        pass

    def UserDescription(self, instance):
        pass

    def UserFollowers(self, instance):
        pass

    def UserFollowing(self, instance):
        pass

    def UserPosts(self, instance):
        pass

    def FinalSettings(self, instance):
        pass

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
        self.manager.current = "last"
        self.manager.transition.direction = "right"

    def press_btn15(self, instance):
        pass






class MyApp (App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoadScreen(name = "load"))
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(ChatScreen(name = "chat"))
        sm.add_widget(SearchScreen(name = "search"))
        sm.add_widget(PostUserScreen(name = "last"))
        sm.add_widget(ProfileScreen(name = "profile"))
        return sm

if __name__ == "__main__":
    MyApp().run()
