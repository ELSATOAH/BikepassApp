from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainPage import MainPage
from DetailsPage import DetailsPage  


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name="main"))
        sm.add_widget(DetailsPage(name="details"))
        return sm


if __name__ == "__main__":
    MyApp().run()