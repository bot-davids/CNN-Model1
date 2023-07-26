import base64
import numpy as np
import cv2
from io import BytesIO
from PIL import Image
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Assuming you have a function to perform facial recognition using your model
def facial_recognition(image_data):
    # Convert the base64-encoded image data to a numpy array
    image = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))
    # Process the image using your facial recognition model and get the prediction
    prediction = "John Doe"  # Replace this with the actual prediction from your model
    return prediction

def base64_to_image(base64_string):
    # Extract the base64 encoded binary data from the input string
    base64_data = base64_string.split(",")[1]
    # Decode the base64 data to bytes
    image_bytes = base64.b64decode(base64_data)
    # Convert the bytes to numpy array
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    # Decode the numpy array as an image using OpenCV
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image


@socketio.on("connect")
def test_connect():
    print("Connected")
    emit("my response", {"data": "Connected"})


@socketio.on("image")
def receive_image(image):
    # Decode the base64-encoded image data
    image = base64_to_image(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    frame_resized = cv2.resize(gray, (640, 360))
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, frame_encoded = cv2.imencode(".jpg", frame_resized, encode_param)
    processed_img_data = base64.b64encode(frame_encoded).decode()
    b64_src = "data:image/jpg;base64,"
    processed_img_data = b64_src + processed_img_data
    emit("processed_image", processed_img_data)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('image_data')
def process_image(data):
    image_data = data['image']
    # Perform facial recognition using your model
    prediction = facial_recognition(image_data)
    # Send the prediction back to the client
    emit('prediction_result', {'result': prediction})

if __name__ == '__main__':
    socketio.run(app, debug=True)
