from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class VerifyEmailScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.add_widget(Label(text="Enter the OTP sent to your email:", font_size=18))
        self.otp_input = TextInput(hint_text="OTP", multiline=False, input_filter='int', font_size=16)
        self.add_widget(self.otp_input)
        self.verify_btn = Button(text="Verify", size_hint=(1, 0.3), font_size=16)
        self.verify_btn.bind(on_press=self.verify_otp)
        self.add_widget(self.verify_btn)
        self.result_label = Label(text="", font_size=16)
        self.add_widget(self.result_label)

    def verify_otp(self, instance):
        otp = self.otp_input.text.strip()
        # Replace '123456' with your actual OTP verification logic
        if otp == "123456":
            self.result_label.text = "OTP Verified Successfully!"
            self.result_label.color = (0, 1, 0, 1)
        else:
            self.result_label.text = "Invalid OTP. Please try again."
            self.result_label.color = (1, 0, 0, 1)

class VerifyEmailApp(App):
    def build(self):
        return VerifyEmailScreen()

if __name__ == "__main__":
    VerifyEmailApp().run()