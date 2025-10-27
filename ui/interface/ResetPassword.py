from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User 

class ResetPasswordScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.add_widget(Label(text="Reset Password", font_size=24, size_hint=(1, 0.2)))

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.add_widget(self.username_input)

        self.old_password_input = TextInput(hint_text="Old Password", password=True, multiline=False)
        self.add_widget(self.old_password_input)

        self.new_password_input = TextInput(hint_text="New Password", password=True, multiline=False)
        self.add_widget(self.new_password_input)

        self.confirm_password_input = TextInput(hint_text="Confirm New Password", password=True, multiline=False)
        self.add_widget(self.confirm_password_input)

        self.reset_btn = Button(text="Reset Password", size_hint=(1, 0.3))
        self.reset_btn.bind(on_press=self.reset_password)
        self.add_widget(self.reset_btn)

    def reset_password(self, instance):
        username = self.username_input.text
        old_password = self.old_password_input.text
        new_password = self.new_password_input.text
        confirm_password = self.confirm_password_input.text
        

        if not username or not old_password or not new_password or not confirm_password:
            self.show_popup("Error", "All fields are required.")
        elif new_password != confirm_password:
            self.show_popup("Error", "New passwords do not match.")
        else:
            user = User(username, old_password,'user')
            user.change_password(username, old_password, new_password)
            # Here you would add logic to verify old password and update credentials
            self.show_popup("Success", "Password has been reset.")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.7, 0.4))
        popup.open()

class ResetPasswordApp(App):
    def build(self):
        return ResetPasswordScreen()

if __name__ == "__main__":
    ResetPasswordApp().run()