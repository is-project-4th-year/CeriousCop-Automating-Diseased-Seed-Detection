from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from Homepage import HomePage

class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_to_main, 3)  # Show splash for 3 seconds

    def switch_to_main(self, dt):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = HomePage()
        
        self.add_widget(layout)
class SplashApp(App):
    def build(self):
        sm = ScreenManager()
        splash_layout = BoxLayout(orientation='vertical', padding=50)
        splash_layout.add_widget(Image(source='../../C.png'))  # Replace with your logo path
        splash_layout.add_widget(Label(text="CeriousCop", font_size=40))
        splash_layout.add_widget(Label(text="Automating Diseased Seed Detection", font_size=20))
        splash = SplashScreen(name='splash')
        splash.add_widget(splash_layout)
        sm.add_widget(splash)
        sm.add_widget(MainScreen(name='main'))
        sm.current = 'splash'
        return sm

if __name__ == '__main__':
    SplashApp().run()