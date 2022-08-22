from random import randint
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager

class HomeScreen(MDScreen):
    Builder.load_file('home.kv')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_task(self):
        wid = OneLineListItem(
            text=self.ids.ent.text,
            id=str(self.ids.lst.children),
            bg_color= (randint(0,101)/100, randint(0,101)/100, randint(0,101)/100, 1),
            size_hint_y = None,
            height = 400
            )
        wid.on_release = lambda x = wid: self.ids.lst.remove_widget(x)
        self.ids.lst.add_widget(wid)
        self.ids.ent.text = ""

class MainApp(MDApp):
    def build(self):
        self.screenManager = ScreenManager()
        self.homeScreen = HomeScreen(name='home')
        self.screenManager.add_widget(self.homeScreen)
        return self.screenManager

if __name__ == '__main__':
    MainApp().run()