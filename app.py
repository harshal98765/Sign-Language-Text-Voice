import gradio as gr
import cv2
import numpy as np
from keras.models import load_model
from cvzone.HandTrackingModule import HandDetector
import enchant
import pyttsx3

# Initialize components
model = load_model('cnn8grps_rad1_model.h5')
hd = HandDetector(maxHands=1)
dictionary = enchant.Dict("en-US")

def process_frame(frame):
    if frame is None:
        return "No input detected"
    
    hands = hd.findHands(frame, draw=False, flipType=True)
    text = ""
    
    if hands[0]:
        hand = hands[0]
        x, y, w, h = hand[0]['bbox']
        # Add your existing prediction logic here
        
    return text

def interface():
    webcam = gr.Image(source="webcam", streaming=True)
    text_output = gr.Textbox(label="Predicted Text")
    
    demo = gr.Interface(
        fn=process_frame,
        inputs=webcam,
        outputs=text_output,
        live=True,
        title="Sign Language to Text Conversion",
        description="Convert sign language gestures to text using webcam"
    )
    
    return demo

if __name__ == "__main__":
    interface().launch()