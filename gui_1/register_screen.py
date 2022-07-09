from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

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

        self.username_box = BoxLayout(size_hint = (1, 1))
        self.main_box.add_widget(self.username_box)

        self.username_text_box = TextInput(size_hint = (1, 1), text = "username")
        self.username_box.add_widget(self.username_text_box)

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
        self.lab1.bind(on_release = self.register)

    def register(self):
        pass
