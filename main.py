from random import randint
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager

from backend import Database

class HomeScreen(MDScreen):
    Builder.load_file('home.kv')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = Database()
        for task in self.db.get_tasks():
            wid = OneLineListItem(
                text=task,
                bg_color= (randint(0,101)/100, randint(0,101)/100, randint(0,101)/100, 1),
                size_hint_y = None,
                height = 400
                )
            wid.on_release = lambda x = wid: self.delete_task(x)
            self.ids.lst.add_widget(wid)


    def add_task(self):
        wid = OneLineListItem(
            text=self.ids.ent.text,
            bg_color= (randint(0,101)/100, randint(0,101)/100, randint(0,101)/100, 1),
            size_hint_y = None,
            height = 400
            )
        wid.on_release = lambda x = wid: self.delete_task(x)
        self.db.add_task(self.ids.ent.text)
        self.ids.lst.add_widget(wid)
        self.ids.ent.text = ""

    def delete_task(self, wid):
        self.db.delete_task(wid.text)
        self.ids.lst.remove_widget(wid)

class MainApp(MDApp):
    def build(self):
        self.screenManager = ScreenManager()
        self.homeScreen = HomeScreen(name='home')
        self.screenManager.add_widget(self.homeScreen)
        return self.screenManager

if __name__ == '__main__':
    MainApp().run()