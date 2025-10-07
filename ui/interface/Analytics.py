from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class AnalyticsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="User Data Analytics", font_size=24, size_hint_y=None, height=50))

        # Example analytics data
        analytics_data = {
            "Total Sessions": 12,
            "Average Session Time (min)": 34,
            "Diseased Seeds Detected": 57,
            "Reviews Submitted": 4
        }

        grid = GridLayout(cols=2, size_hint_y=None, height=160)
        for key, value in analytics_data.items():
            grid.add_widget(Label(text=key, size_hint_y=None, height=40))
            grid.add_widget(Label(text=str(value), size_hint_y=None, height=40))
        self.add_widget(grid)

        self.add_widget(Label(text="Submit Your Review:", font_size=18, size_hint_y=None, height=40))
        self.review_input = TextInput(hint_text="Write your review here...", multiline=True, size_hint_y=None, height=100)
        self.add_widget(self.review_input)

        submit_btn = Button(text="Submit Review", size_hint_y=None, height=40)
        submit_btn.bind(on_press=self.submit_review)
        self.add_widget(submit_btn)

        self.reviews_label = Label(text="User Reviews:", font_size=18, size_hint_y=None, height=40)
        self.add_widget(self.reviews_label)

        self.reviews_box = GridLayout(cols=1, size_hint_y=None)
        self.reviews_box.bind(minimum_height=self.reviews_box.setter('height'))
        self.scroll = ScrollView(size_hint=(1, 1), size=(self.width, 200))
        self.scroll.add_widget(self.reviews_box)
        self.add_widget(self.scroll)

        self.reviews = []

    def submit_review(self, instance):
        review_text = self.review_input.text.strip()
        if review_text:
            self.reviews.append(review_text)
            self.review_input.text = ""
            self.update_reviews()
            popup = Popup(title="Thank You!", content=Label(text="Review submitted."), size_hint=(None, None), size=(300, 150))
            popup.open()

    def update_reviews(self):
        self.reviews_box.clear_widgets()
        for review in self.reviews:
            self.reviews_box.add_widget(Label(text=review, size_hint_y=None, height=40))

class AnalyticsApp(App):
    def build(self):
        return AnalyticsScreen()

if __name__ == "__main__":
    AnalyticsApp().run()