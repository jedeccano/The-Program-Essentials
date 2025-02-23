import pandas as pd
import matplotlib.pyplot as plt
import os  # Import the os module to handle directory paths

# Load your data into a DataFrame (replace this with your actual data loading code)
df = pd.read_csv(r"C:\Users\Acer\OneDrive - Bicol University\Desktop\Design Project Tools\version7\resulta.csv")

# Print available columns to confirm
print("Available columns:", df.columns)

# Define the directory where you want to save the PNG files
output_directory = "C:/Users/Acer/OneDrive - Bicol University/Desktop/Design Project Tools/plots"

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to save individual plots
def save_plot(x, y, title, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=title, linestyle='-', color="blue")  # Removed marker
    plt.xlabel("Epoch")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True, axis='y', linestyle='-', alpha=0.7)  # Enable horizontal grid lines
    plt.savefig(os.path.join(output_directory, filename))  # Save the plot in the specified directory
    plt.close()  # Close the figure to free up memory

# Generate and save plots
save_plot(df["epoch"], df["metrics/precision(B)"], "Precision Over Epochs", "Precision", "precision.png")
save_plot(df["epoch"], df["metrics/recall(B)"], "Recall Over Epochs", "Recall", "recall.png")

# Calculate F-score (assuming F1-score) if not already in the DataFrame
# F1 = 2 * (precision * recall) / (precision + recall)
df["metrics/f1_score(B)"] = 2 * (df["metrics/precision(B)"] * df["metrics/recall(B)"]) / (df["metrics/precision(B)"] + df["metrics/recall(B)"])
save_plot(df["epoch"], df["metrics/f1_score(B)"], "F1-Score Over Epochs", "F1-Score", "f1_score.png")

# Save mean average precision (mAP) plot
save_plot(df["epoch"], df["metrics/mAP50(B)"], "Mean Average Precision (mAP50) Over Epochs", "mAP50", "mAP50.png")

print(f"Plots saved in: {output_directory}")