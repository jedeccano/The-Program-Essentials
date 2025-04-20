import cv2
import time
import threading
from ultralytics import YOLO
from control_servo import control_servo_based_on_class

# Global flag to stop the AI loop
running = False

def start_ai_model():
    global running
    running = True

    # Load the YOLO model
    try:
        model = YOLO(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\version7\et_yung_ai_model.pt")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Open the webcam
    cap = cv2.VideoCapture(0)  # Change the index if external webcam is used
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # Initialize variables for FPS calculation
    fps = 0
    frame_counter = 0
    start_time = time.time()

    while running:
        # Capture frame-by-frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Run YOLO inference on the captured frame
        try:
            results = model(frame)
        except Exception as e:
            print(f"Error during inference: {e}")
            break

        # Draw the results on the frame
        annotated_frame = results[0].plot()

        # Check the class of the detected object and control the servo
        for result in results:
            if result.boxes:
                class_id = result.boxes[0].cls.item()
                class_name = result.names[class_id]
                print(f"Detected class: {class_name}")  # Debugging statement
                control_servo_based_on_class(class_name)

        # Increment frame counter
        frame_counter += 1

        # Calculate FPS every second
        if time.time() - start_time >= 1:
            fps = frame_counter
            frame_counter = 0
            start_time = time.time()

        # Add FPS text to the frame
        cv2.putText(
            annotated_frame, 
            f"FPS: {fps}", 
            (20, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 0), 
            2
        )

        # Display the resulting frame
        try:
            cv2.imshow("YOLO Webcam Detection", annotated_frame)
        except cv2.error as e:
            print(f"Error displaying frame: {e}")
            break

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False

    # Release the capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def start_ai_thread():
    ai_thread = threading.Thread(target=start_ai_model)
    ai_thread.start()

def stop_ai_model():
    global running
    running = False