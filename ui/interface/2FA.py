from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User  # Assuming there's a User class in backend.User module
import Login
class TwoFA(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=40, **kwargs)
        self.add_widget(Label(text="2-Factor Authentication", font_size=24, size_hint=(1, 0.2)))

        self.fingerprint_btn = Button(text="Authenticate with Fingerprint", size_hint=(1, 0.2))
        self.fingerprint_btn.bind(on_release=self.fingerprint_auth)
        self.add_widget(self.fingerprint_btn)

        self.add_widget(Label(text="Or enter OTP:", size_hint=(1, 0.1)))
        self.otp_input = TextInput(hint_text="Enter OTP", multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.otp_input)

        self.otp_btn = Button(text="Verify OTP", size_hint=(1, 0.2))
        self.otp_btn.bind(on_release=self.verify_otp)
        self.add_widget(self.otp_btn)

    def fingerprint_auth(self, instance):
        user = Login.get_current_user()  # Get the currently logged-in user
        user.fingerprint_auth()
        # Simulate fingerprint authentication (replace with actual implementation)
        popup = Popup(title="Fingerprint", content=Label(text="Fingerprint authenticated!"),
                      size_hint=(0.6, 0.3))
        popup.open()

    def verify_otp(self, instance):
        otp = self.otp_input.text
        user = Login.get_current_user()  # Get the currently logged-in user
        user.two_factor_auth(otp)
            msg = "OTP verified!"
            self.manager.current = 'Home page'  # Navigate to the main screen
        else:
            msg = "Invalid OTP!"
        popup = Popup(title="OTP Verification", content=Label(text=msg), size_hint=(0.6, 0.3))
        popup.open()

class TwoFAApp(App):
    def build(self):
        return TwoFA()

if __name__ == "__main__":
    TwoFAApp().run()