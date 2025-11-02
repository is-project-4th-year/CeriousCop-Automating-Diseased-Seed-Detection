from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from SignUp import SignUpForm
from Login import LoginScreen
from ImageScan import ImageScanScreen

class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = SignUpForm()
        self.add_widget(layout)

class HomePageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = HomePage()
        self.add_widget(layout)

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
        btn_account = Button(
            text="Create an account",
            size_hint=(1, 0.15),
            on_press=self.create_account

        )
        btn_account = Button(
            text="Login",
            size_hint=(1, 0.15),
            on_press=self.login

        )
        btn_detect = Button(
            text="Detect Diseased Seeds",
            size_hint=(1, 0.15),
            on_press=self.start_detection
        )
        btn_history = Button(
            text="View Detection History",
            size_hint=(1, 0.15)
        )
        btn_about = Button(
            text="About",
            size_hint=(1, 0.15)
        )
        self.add_widget(btn_account)
        self.add_widget(btn_detect)
        self.add_widget(btn_history)
        self.add_widget(btn_about)

    def create_account(self, instance):
        sm = self.parent.parent
        sm.current = 'signup'
        # Logic to navigate to account creation screen
        pass

    def login(self,instance):
        sm=self.parent.parent
        sm.current = 'login'

    def start_detection(self, instance):
        sm = self.parent.parent
        sm.current = 'image_scan'
        # Logic to navigate to diseased seed detection screen
        pass

class HomePageApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomePageScreen(name='home'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ImageScanScreen(name='image_scan'))
        sm.current = 'home'
        return sm

if __name__ == '__main__':
    HomePageApp().run()