from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User 

 # Assuming there's a User class in backend.User module
class AdminLoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = AdminLoginScreen()
        self.add_widget(layout)
class AdminLoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="Admin Login", font_size=24, size_hint=(1, 0.3)))

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False)
        self.add_widget(self.password_input)

        login_btn = Button(text="Login", size_hint=(1, 0.3))
        login_btn.bind(on_press=self.authenticate)
        self.add_widget(login_btn)
        
        forgot_btn = Button(text="Forgot Password?", size_hint=(1, 0.2))
        forgot_btn.bind(on_press=self.forgot_password)
        self.add_widget(forgot_btn)
    def authenticate(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        user = User(username, password, 'admin')
        if user.adminLogin(username, password):
           self.show_popup("Success", "Admin login successful!")
           #self.manager.current = 'Admin-dashboard'
            # Navigate to admin dashboard or next screen
    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 150))
        popup.open()

    def forgot_password(self, instance):
        self.manager.current = 'ResetPassword'

class AdminLoginApp(App):
    def build(self):
        return AdminLoginScreen()

if __name__ == "__main__":
    AdminLoginApp().run()