import time
import yaml
from pyfirmata import Arduino, SERVO

# Load class names from data.yaml
with open(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\model Versions\v26(SML-Defect)\data.yaml", 'r') as file:
    data = yaml.safe_load(file)
    class_names = data['names']

# Define the port where the Arduino is connected
port = 'COM15'  # Change this to your Arduino port
board = Arduino(port)

# Define the pin where the servo is connected
servo_pin = 9
board.digital[servo_pin].mode = SERVO

# Function to rotate the servo to a specific angle
def rotate_servo(angle):
    board.digital[servo_pin].write(angle)
    time.sleep(5)  # Wait for the servo to reach the position

#annotated_frame,
def control_servo_based_on_class(class_name):
    print(f"Class detected: {class_name}")  # Debugging statement
    if class_name in ["Quality-Small", "Quality-Medium", "Quality-Large"]:
        print(f"Rotating servo to 45 degrees for {class_name}")
        rotate_servo(45)
    elif class_name == "Defective":
        print(f"Rotating servo to 135 degrees for {class_name}")
        rotate_servo(135)
    else:
        print("Rotating servo to 90 degrees for unrecognized class")
        rotate_servo(90)  # Default position if class is not recognized