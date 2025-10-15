from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text='Admin Dashboard', font_size=32, size_hint=(1, 0.2)))

        layout.add_widget(Button(text='View Seed Reports', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='Manage Users', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='System Settings', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='Logout', size_hint=(1, 0.15)))

        self.add_widget(layout)

class AdminDashboardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    AdminDashboardApp().run()