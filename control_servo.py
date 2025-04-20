import time
import yaml
from pyfirmata import Arduino, SERVO

# Load class names from data.yaml
with open(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\version7\Me.v7i.yolov11\data.yaml", 'r') as file:
    data = yaml.safe_load(file)
    class_names = data['names']

# Define the port where the Arduino is connected
port = 'COM13'  # Change this to your Arduino port
board = Arduino(port)

# Define the pin where the servo is connected
servo_pin = 9
board.digital[servo_pin].mode = SERVO

# Function to rotate the servo to a specific angle
def rotate_servo(angle):
    board.digital[servo_pin].write(angle)
    time.sleep(1)

# Function to control the servo based on the AI model's output
def control_servo_based_on_class(class_name):
    print(f"Class detected: {class_name}")  # Debugging statement
    if class_name == "Happy-Jed":
        rotate_servo(90)
    elif class_name == "Normie-Jed":
        rotate_servo(0)
    elif class_name == "wow-Jed":
        rotate_servo(45)
    elif class_name == "malupiton-Jed":
        rotate_servo(135)
    else:
        rotate_servo(90)  # Default position if class is not recognized