import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from model.train import model, device
import torch
from torchvision import transforms
from PIL import Image
import os
import json
import sys
import numpy as np
import time
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report

def predict(image_path):
    # Load and preprocess the image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # ViT expects 224x224 images
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device

    # Make prediction
    model.eval()
    with torch.no_grad():
        outputs = model(image).logits
        _, predicted = torch.max(outputs, 1)
        



    # If the prediction is for a bad seed, display bounding boxes
    if predicted.item() == 1:  # Assuming class 1 is 'bad seed'
        # Load original image for display
        orig_image = cv2.imread(image_path)
        orig_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        

        # Dummy bounding box coordinates (replace with your detection logic)
        # Example: [(x1, y1, x2, y2), ...]
        # Here we just use a fixed box for demonstration
        boxes = [(50, 50, 150, 150)]  # Replace with actual detection results

        fig, ax = plt.subplots(1)
        ax.imshow(orig_image)
        for box in boxes:
            x1, y1, x2, y2 = box
            rect = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
        plt.title("Detected Bad Seeds")
        plt.show()
    
    return predicted.item()