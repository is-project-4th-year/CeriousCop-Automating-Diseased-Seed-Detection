from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from ....model.predict import predict

class CameraInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.image_widget = Image()
        self.add_widget(self.image_widget)
        self.capture_btn = Button(text='Start Camera')
        self.capture_btn.bind(on_press=self.start_camera)
        self.add_widget(self.capture_btn)
        self.capture = None
        self.event = None

    def start_camera(self, instance):
        if not self.capture:
            self.capture = cv2.VideoCapture(0)
            self.event = Clock.schedule_interval(self.update, 1.0 / 30)

            self.capture_btn.text = 'Stop Camera'
        else:
            self.stop_camera()

    def stop_camera(self):
        if self.event:
            self.event.cancel()
        if self.capture:
            self.capture.release()
            self.capture = None
        self.capture_btn.text = 'Start Camera'

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image_widget.texture = texture
            # For demonstration, let's predict on the current frame every second
            if int(dt * 30) % 30 == 0:  # Roughly
                cv2.imwrite("current_frame.jpg", frame)
                prediction = predict("current_frame.jpg")
                print(f"Prediction: {prediction}")
               


    def on_stop(self):
        self.stop_camera()

class ImageScanApp(App):
    def build(self):
        return CameraInterface()

    def on_stop(self):
        self.root.on_stop()

if __name__ == '__main__':
    ImageScanApp().run()