from ...model import train

class Image:
    def __init__(self, image_path, label):
        self.image_path = image_path
        self.label = label

    def get_image_path(self):
        return self.image_path

    def get_label(self):
        return self.label

    def scan_image(self):
        model = train.model # Load the trained model
        result = model.predict(self.image_path) 
        return f"Scanning image at {self.image_path} for label {self.label}" # Predict using the model
        return result

    