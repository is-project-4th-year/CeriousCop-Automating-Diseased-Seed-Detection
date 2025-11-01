from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User  # Assuming there's a User class in backend.User module
class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = SignUpForm()
        self.add_widget(layout)


class SignUpForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="Register Account", font_size=24, size_hint=(1, 0.2)))

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.add_widget(self.username_input)

        self.email_input = TextInput(hint_text="Email", multiline=False)
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False)
        self.add_widget(self.password_input)

        self.confirm_input = TextInput(hint_text="Confirm Password", password=True, multiline=False)
        self.add_widget(self.confirm_input)

        self.register_btn = Button(text="Register", size_hint=(1, 0.3))
        self.register_btn.bind(on_press=self.register)
        self.add_widget(self.register_btn)

        

    def register(self, instance):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text
        confirm = self.confirm_input.text

        if not username or not email or not password or not confirm:
            self.show_popup("All fields are required.")
        elif password != confirm:
            self.show_popup("Passwords do not match.")
        else:
            user = User(username, email, password)
            user.signup(username, password)
            # Here you would add logic to save the user data
            #self.show_popup("Registration successful!")
            #self.manager.current = 'Home page'  # Navigate to Home page

    def show_popup(self, message):
        popup = Popup(title='Sign Up', content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

class SignUpApp(App):
    def build(self):
        return SignUpForm()

if __name__ == '__main__':
    SignUpApp().run()

    