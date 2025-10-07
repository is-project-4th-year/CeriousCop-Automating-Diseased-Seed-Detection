from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from ..backend.User import User  # Assuming there's a User class in backend.User module

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(orientation='vertical', **kwargs)
        self.padding = 40
        self.spacing = 20

        self.add_widget(Label(text='Login', font_size=32, size_hint=(1, 0.2)))

        self.username = TextInput(hint_text='Username', multiline=False, size_hint=(1, 0.15))
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint=(1, 0.15))
        self.add_widget(self.password)

        self.login_btn = Button(text='Login', size_hint=(1, 0.15))
        self.login_btn.bind(on_press=self.on_login)
        self.add_widget(self.login_btn)

        self.message = Label(text='', color=(1,0,0,1), size_hint=(1, 0.15))
        self.add_widget(self.message)

    def on_login(self, instance):
        user = self.username.text
        pwd = self.password.text
        if user == "admin" and pwd == "password":
            self.message.text = "Login successful!"
            self.message.color = (0,1,0,1)
        else:
            self.message.text = "Invalid credentials."
            self.message.color = (1,0,0,1)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()