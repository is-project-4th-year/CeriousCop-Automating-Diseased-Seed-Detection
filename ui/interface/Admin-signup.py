from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User  # Assuming there's a User class in backend.User module
class AdminSignup(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text='Admin Signup', font_size=24, size_hint=(1, 0.2)))

        self.username = TextInput(hint_text='Username', multiline=False)
        self.add_widget(self.username)

        self.email = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.email)

        self.password = TextInput(hint_text='Password', password=True, multiline=False)
        self.add_widget(self.password)

        self.confirm_password = TextInput(hint_text='Confirm Password', password=True, multiline=False)
        self.add_widget(self.confirm_password)

        signup_btn = Button(text='Sign Up', size_hint=(1, 0.3))
        signup_btn.bind(on_press=self.signup)
        self.add_widget(signup_btn)

    def signup(self, instance):
        username = self.username.text.strip()
        email = self.email.text.strip()
        password = self.password.text
        confirm_password = self.confirm_password.text
        user = User(username, email, password, 'admin')
        user.adminSignup(username, email,password)

        self.show_popup('Success', 'Admin account created successfully!')
        #self.manager.current = 'Admin_login'  # Navigate to admin login screen

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

class AdminSignupApp(App):
    def build(self):
        return AdminSignup()

if __name__ == '__main__':
    AdminSignupApp().run()