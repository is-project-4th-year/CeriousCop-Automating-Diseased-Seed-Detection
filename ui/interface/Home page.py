from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=20, **kwargs)
        self.add_widget(Label(
            text="CeriousCop: Automating Diseased Seed Detection",
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.2)
        ))
        self.add_widget(Label(
            text="Welcome! Please choose an option below to get started.",
            font_size='16sp',
            size_hint=(1, 0.1)
        ))
        btn_detect = Button(
            text="Detect Diseased Seeds",
            size_hint=(1, 0.15)
        )
        btn_history = Button(
            text="View Detection History",
            size_hint=(1, 0.15)
        )
        btn_about = Button(
            text="About",
            size_hint=(1, 0.15)
        )
        self.add_widget(btn_detect)
        self.add_widget(btn_history)
        self.add_widget(btn_about)

class HomePageApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return HomePage()

if __name__ == '__main__':
    HomePageApp().run()