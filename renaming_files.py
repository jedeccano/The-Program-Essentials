import os
from tqdm import tqdm

def rename_images(directory, prefix="image"):
    """
    Renames all image files in the given directory with an incrementing number and a progress bar.
    
    Args:
        directory (str): Path to the folder containing images.
        prefix (str): Prefix for the new filenames (default: 'image').
    """
    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return
    
    image_files = sorted([f for f in os.listdir(directory) if f.lower().endswith(('png', 'jpg', 'jpeg'))])
    
    for idx, filename in enumerate(tqdm(image_files, desc="Renaming Files", unit="file"), start=1):
        old_path = os.path.join(directory, filename)
        ext = os.path.splitext(filename)[1]  # Get file extension
        new_filename = f"{prefix}_{idx:03d}{ext}"  # e.g., image_001.jpg
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)

# Example usage
image_directory = r"C:\Users\Acer\OneDrive - Bicol University\Pictures\abaniko directory\for_merging"  # Change this to your actual image folder
rename_images(image_directory, prefix="livin-large")