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



Window.size = (400, 600)



def get_post_text(a):
    return str(a)
    #random.randint(0, a+1)




class LoadScreen (Screen):
    def __init__(self, **kwargs):
        super(LoadScreen, self).__init__(**kwargs)
        self.box0 = BoxLayout(orientation = "vertical")
        self.add_widget(self.box0)

        self.Lab1 = Button(size_hint = (None, None), size = (400, 400), background_normal = 'logo.png', background_down = 'logo.png')
        self.box0.add_widget(self.Lab1)
        self.Lab1.bind(on_press = self.change)

        self.lab2 = Label(text = "Small Brother", size_hint = (1, 0.12))
        self.box0.add_widget(self.lab2)

        Clock.schedule_once(self.change, 2)

        
    def change(self, instance):
        self.manager.transition = FallOutTransition()
        self.manager.current = "main"
        


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
        self.lab1.bind(on_release = self.press_btn13)
        
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
        self.lab1.bind(on_release = self.press_btn13)
        
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

        self.lab3 = TextInput(multiline = False, text = "Search hastag")
        self.grid.add_widget(self.lab3)
        self.lab2.bind(on_text_validate = self.search13)

        self.ran0 = Button (text = "Favourites", size_hint = (1, 1))
        self.grid.add_widget(self.ran0)
        self.ran0.bind(on_press = self.random0)

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

    def random0(self, instance):
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

        self.lab1 = Button (size_hint = (None, None), size = (70, 70), background_normal = 'logo.png', background_down = 'logo.png')
        self.box1.add_widget(self.lab1)
        
        self.text1 = TextInput(multiline = False)
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(size_hint = (None, None), size = (70, 70), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1))
        self.Box0.add_widget(self.box2)
        
        self.grid = GridLayout(cols = 1, size_hint_y = None, spacing = 3)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)


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

        for a in range (7):
            self.btn_p = Button (size_hint_y = None, height = 100, text = "P" + (get_post_text(a)))
            self.grid.add_widget(self.btn_p)

        """
        #botó per crear posts
        self.btn1 = Button (text = "1", size_hint_y = None, height = 50)
        self.grid.add_widget(self.btn1)
        self.btn1.bind(on_press = partial(self.make_post_btn, "aniol", "foto", "What doesn't kill you makes you stronger." + '\n' + " ~Friedrich Niesche~", 9))
        """



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
    
    """
    #def crear botó. Estructura "correcta"
    def make_post_btn(self, user_name, user_image, textp, nlikes, instance):
        
        self.post = BoxLayout(size_hint_y = None, height = 200, orientation = "vertical")
        self.grid.add_widget(self.post)
        self.post_like = 0

        self.first_box = BoxLayout(orientation = "horizontal", size_hint = (1, 0.5))
        self.post.add_widget(self.first_box)
        
        self.im = Button(size_hint = (None, 1), width = 50, text = "I")
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
        """

    
    def Name_press(self, instance):
        pass

    def Image_press(self, instance):
        pass

    def Like_press(self, nlikes, instance):
        self.post_like = (self.post_like + 1) % 2
        self.num_likes.text = (str(nlikes + self.post_like))
        return
        



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
        self.lab1.bind(on_release = self.press_btn13)
        
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
        #self.actp.bind(on_text_validate = self.NotYet)

        self.actp2 = TextInput(multiline = False, size_hint = (1, 0.5))
        self.grid.add_widget(self.actp2)

        self.actp3 = TextInput(multiline = False, size_hint = (1, 0.5))
        self.grid.add_widget(self.actp3)

        self.send = Button (text = "Publish", size_hint = (1, 0.8))
        self.grid.add_widget(self.send)
        self.send.bind(on_press = self.SendPost)

        #self.last = Button (text = "All your posts", size_hint = (1, 0.67))
        #self.grid.add_widget(self.last)
        #self.last.bind(on_press = self.LastPosts)


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
        self.lab1.bind(on_release = self.press_btn13)
        
        self.text1 = TextInput(multiline = False, size_hint = (2, 1))
        self.box1.add_widget(self.text1)
        self.text1.bind(on_text_validate = self.Search1)
        
        self.btn1 = Button(text = "S", size_hint = (1, 1), background_normal = 'settings1.png', background_down = 'settings2.png')
        self.box1.add_widget(self.btn1)
        self.btn1.bind(on_press = self.Settings)
        

        self.box2 = BoxLayout (size_hint = (1, 1), orientation = "vertical")
        self.Box0.add_widget(self.box2)

        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.scroll = ScrollView ()
        self.scroll.add_widget (self.grid)
        self.box2.add_widget (self.scroll)

        self.user_n_f = BoxLayout(size_hint_y = None, height = 100)
        self.grid.add_widget(self.user_n_f)

        self.us_image = Button(text = "Foto", size_hint = (0.5, 1))
        self.user_n_f.add_widget(self.us_image)
        self.us_image.bind(on_press = self.UserImage)

        self.us_name = Button(text = "Name")
        self.user_n_f.add_widget(self.us_name)
        self.us_name.bind(on_press = self.UserName)

        self.us_des = Button(text = "Description", size_hint_y = None, height = 162)
        self.grid.add_widget(self.us_des)
        self.us_des.bind(on_press = self.UserDescription)

        self.user_foll = BoxLayout(size_hint_y = None, height = 100)
        self.grid.add_widget(self.user_foll)

        self.us_followers = Button(text = "Followers")
        self.user_foll.add_widget(self.us_followers)
        self.us_followers.bind(on_press = self.UserFollowers)

        self.us_following = Button(text = "Following")
        self.user_foll.add_widget(self.us_following)
        self.us_following.bind(on_press = self.UserFollowing)

        self.u_posts_all = BoxLayout(size_hint_y = None, height = 100)
        self.grid.add_widget(self.u_posts_all)

        self.us_posts = Button(text = "My Posts")
        self.u_posts_all.add_widget(self.us_posts)
        self.us_posts.bind(on_press = self.UserPosts)
        
        self.fav = Button (text = "Favourites")
        self.u_posts_all.add_widget(self.fav)
        self.fav.bind(on_press = self.UserFavourites)

        #firstposts
        #current: 1 = my, 2 = fav
        self.current_posts = 0
        self.quant_m_p = 10
        self.quant_f_p = 11
        self.us_posts.trigger_action(duration = 0)


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
        if self.current_posts != 1:
            if self.current_posts == 2:
                self.favourite_posts.clear_widgets()
                self.grid.remove_widget(self.favourite_posts)

            self.my_posts = BoxLayout(size_hint_y = None, height = self.quant_m_p * 100, orientation = "vertical")
            self.grid.add_widget(self.my_posts)

            #my posts
            for a in range (self.quant_m_p): 
                self.btn_p = Button (size_hint_y = None, height = 100, text = "M" + (get_post_text(a)))
                self.my_posts.add_widget(self.btn_p)
            
            self.grid.bind(minimum_height=self.grid.setter('height'))
            self.current_posts = 1

    def UserFavourites(self, instance):
        if self.current_posts != 2:
            if self.current_posts == 1:
                self.my_posts.clear_widgets()
                self.grid.remove_widget(self.my_posts)

            self.favourite_posts = BoxLayout(size_hint_y = None, height = self.quant_f_p * 100, orientation = "vertical")
            self.grid.add_widget(self.favourite_posts)

            #favourite posts
            for a in range (self.quant_f_p):
                self.btn_f = Button (size_hint_y = None, height = 100, text = "F" + (get_post_text(a)))
                self.favourite_posts.add_widget(self.btn_f)
            
            self.grid.bind(minimum_height=self.grid.setter('height'))
            self.current_posts = 2

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
        sm = ScreenManager(transition = FallOutTransition())
        sm.add_widget(LoadScreen(name = "load"))
        sm.transition = SlideTransition()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(ChatScreen(name = "chat"))
        sm.add_widget(SearchScreen(name = "search"))
        sm.add_widget(PostUserScreen(name = "last"))
        sm.add_widget(ProfileScreen(name = "profile"))
        return sm

if __name__ == "__main__":
    MyApp().run()




#random anchor down right float