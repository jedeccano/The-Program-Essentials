from ultralytics import YOLO

# Load the trained YOLO model (replace path with your model)
model = YOLO(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\sigenanga\best (1).pt")

# Path to your image or directory of images
source_path = r"C:\Users\Acer\OneDrive - Bicol University\Pictures\abaniko directory\small-2\face_capture_001.png" # You can also put a directory here

# Run prediction
results = model.predict(source=source_path, save=True, conf=0.25)  # You can adjust 'conf' for confidence threshold

# Print results
for result in results:
    print(result.names)  # Class names
    print(result.boxes.xyxy)  # Bounding box coordinates
    print(result.boxes.cls)  # Class IDs
    print(result.boxes.conf)  # Confidence scores

print("Prediction completed and results saved.")
