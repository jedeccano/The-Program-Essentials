import tkinter as tk
from tkinter import ttk
from ai_model import start_ai_thread, stop_ai_model  # Import the necessary functions

# Function to stop the AI loop and close the application
def exit_app():
    stop_ai_model()
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("AI Model Launcher")
root.geometry("400x300")  # Set the size of the window
root.configure(bg="#f0f0f0")  # Set a light background color

# Add a label
label = tk.Label(
    root, 
    text="Welcome to the AI Model Launcher", 
    font=("Arial", 16, "bold"), 
    bg="#f0f0f0", 
    fg="#333"
)
label.pack(pady=20)

# Add a frame for the buttons to center-align them
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Style the Start button
start_button = ttk.Button(
    button_frame, 
    text="Start AI Model", 
    command=start_ai_thread
)
start_button.pack(pady=10, ipadx=10, ipady=5)

# Style the Exit button
exit_button = ttk.Button(
    button_frame, 
    text="Exit", 
    command=exit_app
)
exit_button.pack(pady=10, ipadx=20, ipady=5)

# Add a footer label
footer_label = tk.Label(
    root, 
    text="Press 'q' in the detection window to stop the AI model", 
    font=("Arial", 10), 
    bg="#f0f0f0", 
    fg="#555"
)
footer_label.pack(side="bottom", pady=10)

# Run the main event loop
root.mainloop()