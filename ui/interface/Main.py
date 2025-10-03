from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Go to Page 1', on_press=lambda x: self.manager.current = 'page1'))
        layout.add_widget(Button(text='Go to Page 2', on_press=lambda x: self.manager.current = 'page2'))
        self.add_widget(layout)

class Page1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Back to Home', on_press=lambda x: self.manager.current = 'home'))
        self.add_widget(layout)

class Page2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Back to Home', on_press=lambda x: self.manager.current = 'home'))
        self.add_widget(layout)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        return sm

if __name__ == '__main__':
    MainApp().run()