from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder
from kivy.clock import Clock
from ImageScan import CameraInterface
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.Image_scanner import ScanImage
from ImageScan import CameraInterface

class ImageScanResultsLayout(BoxLayout):
    

Builder.load_string("""
<ImageScanResultsLayout>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Label:
        text: "Scan Results"
        font_size: '24sp'
        size_hint_y: None
        height: self.texture_size[1] + 10

    ScrollView:
        size_hint_y: 0.5
        BoxLayout:
            id: results_box
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height

    Label:
        text: "Other Visible Problems:"
        size_hint_y: None
        height: self.texture_size[1] + 10

    TextInput:
        id: other_problems_input
        multiline: True
        hint_text: "Describe any other visible problems here..."
        size_hint_y: None
        height: 100

    Button:
        text: "Submit"
        size_hint_y: None
        height: 50
        on_press: root.on_submit()
""")

class ImageScanResultsPage(BoxLayout):
    scan_results = CameraInterface().update(0)  # Placeholder for actual scan results

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(scan_results=self.update_results)

    def update_results(self, *args):
        results_box = self.ids.results_box
        results_box.clear_widgets()
        if not self.scan_results:
            results_box.add_widget(Label(text="No results to display.", size_hint_y=None, height=30))
        else:
            for result in self.scan_results:
                results_box.add_widget(Label(text=result, size_hint_y=None, height=30))

    def on_submit(self):
        other_problems = self.ids.other_problems_input.text
        Imagescanner = CameraInterface().update(0).image_instance
        Imagescanner.generate_prompt(other_problems)
        # Handle submission logic here (e.g., save results, send to backend, etc.)
        print("Scan Results:", self.scan_results)
        print("Other Visible Problems:", other_problems)
        # Optionally clear input after submission
        self.ids.other_problems_input.text = ""