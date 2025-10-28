from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

class FileSelect(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.select_btn = Button(text='Select Image from Gallery', size_hint=(1, 0.1))
        self.select_btn.bind(on_release=self.open_filechooser)
        self.add_widget(self.select_btn)
        self.img = Image(size_hint=(1, 0.8))
        self.add_widget(self.img)
        self.status = Label(text='No image selected', size_hint=(1, 0.1))
        self.add_widget(self.status)

    def open_filechooser(self, instance):
        filechooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'], multiselect=False)
        popup = Popup(title='Select Image', content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_selection=lambda fc, x: self.select_image(x, popup))
        popup.open()

    def select_image(self, selection, popup):
        if selection:
            self.img.source = selection[0]
            self.status.text = f'Selected: {selection[0]}'
        else:
            self.status.text = 'No image selected'
        popup.dismiss()

class FileSelectApp(App):
    def build(self):
        return FileSelect()

if __name__ == '__main__':
    FileSelectApp().run()