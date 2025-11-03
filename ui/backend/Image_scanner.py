import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model.predict import predict
import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


class ScanImage:
    def __init__(self, image_path, label):
        self.image_path = image_path
        self.label = label
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['image_database']
        self.collection = self.db['image_data']

    def get_image_path(self):
        return self.image_path

    def get_label(self):
        return self.label

    def scan_image(self):
        
        result = predict(self.image_path) 
        self.collection.insert_one({
            "image_path": self.image_path,
            "scan_results": result
        })
        return f"Scanning image at {self.image_path} for label {self.label}" # Predict using the model
        return result

    def generate_prompt(self, text):
        prompt = f"What are the diseases likely associated with {text}?"
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')

        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model(**inputs)
        return outputs



    