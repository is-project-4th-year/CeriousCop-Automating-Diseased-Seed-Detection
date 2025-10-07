from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from ..backend.User import User

class ProfileView(BoxLayout):
    username = StringProperty("JohnDoe")
    email = StringProperty("john@example.com")

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="Profile", font_size=24, size_hint=(1, 0.2)))

        self.username_input = TextInput(text=self.username, multiline=False)
        self.add_widget(Label(text="Username:"))
        self.add_widget(self.username_input)

        self.email_input = TextInput(text=self.email, multiline=False)
        self.add_widget(Label(text="Email:"))
        self.add_widget(self.email_input)

        self.save_btn = Button(text="Save Changes", size_hint=(1, 0.2))
        self.save_btn.bind(on_press=self.save_profile)
        self.add_widget(self.save_btn)

        self.status_label = Label(text="", color=(0, 1, 0, 1), size_hint=(1, 0.1))
        self.add_widget(self.status_label)

    def save_profile(self, instance):
        self.username = self.username_input.text
        self.email = self.email_input.text
        self.status_label.text = "Profile updated!"

class ProfileApp(App):
    def build(self):
        return ProfileView()

if __name__ == "__main__":
    ProfileApp().run()