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

    def compile_for_android(self):
        from kivy.utils import platform
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            # Example: Set the activity to full screen
            activity.getWindow().addFlags(1024)  # FLAG_FULLSCREEN
            # Add more Android-specific configurations as needed
            activity.getWindow().setFlags(128, 128)  # FLAG_KEEP_SCREEN_ON
            print("Compiled for Android with specific configurations.")
    
    

if __name__ == '__main__':
    MainApp().run()