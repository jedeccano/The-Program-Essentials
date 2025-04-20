import customtkinter as ctk
from PIL import Image  # Import the necessary modules from Pillow
from customtkinter import CTkImage  # Import CTkImage from customtkinter
from ai_model import start_ai_thread, stop_ai_model  # Import the necessary functions
from PIL import Image, ImageOps  # Import ImageOps for color transformation

# Function to stop the AI loop and close the application
def exit_app():
    stop_ai_model()
    root.destroy()

# Create the GUI window
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Abaniko Assessment")
root.geometry("600x400")  # Set the size of the window

# Load and resize images using CTkImage
home_icon = CTkImage(Image.open(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\The Program Essentials\home.png"), size=(20, 20))
user_manual_icon = CTkImage(Image.open(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\The Program Essentials\user_manual.png"), size=(20, 20))
about_us_icon = CTkImage(Image.open(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\The Program Essentials\about_us.png"), size=(20, 20))

# Function to switch to the Home tab
def show_home():
    for widget in main_frame.winfo_children():
        widget.destroy()
    # Add a header placeholder
    header_label = ctk.CTkLabel(
        main_frame, 
        text="Abaniko Assessment", 
        font=ctk.CTkFont("Arial", 20, "bold"),
        fg_color="#1e1e1e"
    )
    header_label.pack(pady=10)

    # Add a label
    label = ctk.CTkLabel(
        main_frame, 
        text="Welcome to the Abaniko Assessment", 
        font=ctk.CTkFont("Arial", 16, "bold"),
        fg_color="#1e1e1e"
    )
    label.pack(pady=10)

    # Add a frame for the buttons to center-align them
    button_frame = ctk.CTkFrame(main_frame, fg_color="#1e1e1e")
    button_frame.pack(pady=10)

    # Style the Start button
    start_button = ctk.CTkButton(
        button_frame, 
        text="Start AI Model", 
        command=start_ai_thread
    )
    start_button.pack(pady=5, ipadx=10, ipady=5, padx=10)

    # Style the Exit button
    exit_button = ctk.CTkButton(
        button_frame, 
        text="Exit", 
        command=exit_app
    )
    exit_button.pack(pady=5, ipadx=10, ipady=5, padx=10)

    # Add a footer label
    footer_label = ctk.CTkLabel(
        main_frame, 
        text="Press 'q' in the detection window to stop the AI model", 
        font=ctk.CTkFont("Arial", 10),
        fg_color="#1e1e1e"
    )
    footer_label.pack(side="bottom", pady=10)

def show_user_manual():
    for widget in main_frame.winfo_children():
        widget.destroy()
    # Add a header placeholder
    header_label = ctk.CTkLabel(
        main_frame, 
        text="Abaniko Assessment", 
        font=ctk.CTkFont("Arial", 20, "bold"),
        fg_color="#1e1e1e"
    )
    header_label.pack(pady=10)
    label = ctk.CTkLabel(
        main_frame, 
        text="User Manual", 
        font=ctk.CTkFont("Arial", 16, "bold"),
        fg_color="#1e1e1e"
    )
    label.pack(pady=10)

    # Add a CTkTextbox for the manual content
    manual_textbox = ctk.CTkTextbox(
        main_frame, 
        font=ctk.CTkFont("Arial", 12),
        fg_color="#2e2e2e",
        text_color="white",
        wrap="word",
        height=200
    )
    manual_textbox.pack(pady=10, padx=10, fill="both", expand=True)

    # Insert the user manual text into the textbox
    manual_textbox.insert("1.0", 
        "1. Make sure all the peripherals are connected, i.e. camera port, arduino port, servo motor.\n\n"
        "2. Press the start button to launch the trained AI model.\n\n"
        "3. Load the Abaniko Fan to the Conveyor Belt, and wait for it to be sorted before loading another.\n\n"
        "4. After sorting a certain number of abanikos, Press 'q' to quit the system."
    )
    manual_textbox.configure(state="disabled")  # Make the textbox read-only

# Function to switch to the About Us tab
def show_about_us():
    for widget in main_frame.winfo_children():
        widget.destroy()
    # Add a header placeholder
    header_label = ctk.CTkLabel(
        main_frame, 
        text="Abaniko Assessment", 
        font=ctk.CTkFont("Arial", 20, "bold"),
        fg_color="#1e1e1e"
    )
    header_label.pack(pady=10)
    label = ctk.CTkLabel(
        main_frame, 
        text="About Us", 
        font=ctk.CTkFont("Arial", 16, "bold"),
        fg_color="#1e1e1e"
    )
    label.pack(pady=10)
    about_text = ctk.CTkLabel(
        main_frame, 
        text="Information about us...", 
        font=ctk.CTkFont("Arial", 12),
        fg_color="#1e1e1e"
    )
    about_text.pack(pady=10)

# Create a sidebar frame
sidebar_frame = ctk.CTkFrame(root, width=200, fg_color="#2e2e2e")
sidebar_frame.pack(side="left", fill="y")

# Add a title to the sidebar
sidebar_title = ctk.CTkLabel(
    sidebar_frame, 
    text="Abaniko Assessment", 
    font=ctk.CTkFont("Arial", 18, "bold"),
    fg_color="#2e2e2e",
    text_color="white"
)
sidebar_title.pack(pady=20)

# Add buttons to the sidebar with icons
home_button = ctk.CTkButton(sidebar_frame, text="Home", image=home_icon, compound="left", anchor="w", command=show_home, fg_color="#2e2e2e", text_color="white")
home_button.pack(pady=5, fill="x")

user_manual_button = ctk.CTkButton(sidebar_frame, text="User Manual", image=user_manual_icon, compound="left", anchor="w", command=show_user_manual, fg_color="#2e2e2e", text_color="white")
user_manual_button.pack(pady=5, fill="x")

about_us_button = ctk.CTkButton(sidebar_frame, text="About Us", image=about_us_icon, compound="left", anchor="w", command=show_about_us, fg_color="#2e2e2e", text_color="white")
about_us_button.pack(pady=5, fill="x")

# Create a main content frame with a darker background
main_frame = ctk.CTkFrame(root, fg_color="#1e1e1e")
main_frame.pack(side="right", fill="both", expand=True)

# Show the Home tab by default
show_home()

# Run the main event loop
root.mainloop()