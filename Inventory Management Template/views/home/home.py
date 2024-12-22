from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty

Builder.load_file('views/home/home.kv')
class Home(Screen):
    user = StringProperty("Tanaka Peter Makuni")
    user_type = StringProperty("Admin")
    avatar = "assets/images/avatar.png"
    def on_enter(self, *args):
        return super().on_enter(*args)