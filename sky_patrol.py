import os
from PIL import Image
from datetime import datetime
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Initialize colorama for colored output in terminal
init(autoreset=True)

# === FOLDERS AND SETTINGS ===
image_folder = 'images'                 # Folder with drone images
log_file = 'detection_log.txt'          # File to save results
suspicious_keywords = ['1', '2', 'unauthorized']  # Keywords to simulate detection

# === CHECK IF IMAGE FOLDER EXISTS ===
if not os.path.exists(image_folder):
    print(Fore.RED + " Oops! The 'images' folder is missing.")
    exit()

# === GET ALL IMAGE FILES ===
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

if not image_files:
    print(Fore.YELLOW + " No image files found in the 'images' folder.")
    exit()

# Clear previous logs (if any)
with open(log_file, 'w') as log:
    log.write("SKY_PATROL - Unauthorized Construction Detection Log\n")
    log.write("------------------------------------------------------\n")

# === FUNCTION TO CHECK IMAGE NAME FOR SUSPICIOUS ACTIVITY ===
def is_suspicious(filename):
    return any(word in filename.lower() for word in suspicious_keywords)

# === FUNCTION TO SHOW IMAGE ===
def preview_image(path):
    try:
        img = Image.open(path)
        plt.imshow(img)
        plt.title(os.path.basename(path))
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(Fore.RED + f" Couldn't show image: {e}")

# === MAIN DETECTION LOOP ===
for filename in image_files:
    filepath = os.path.join(image_folder, filename)
    print(f"\n Checking image: {filename}")

    # Step 1: Try opening the image to make sure it works
    try:
        img = Image.open(filepath)
        img.verify()
    except Exception as error:
        print(Fore.RED + f" Error opening {filename}: {error}")
        continue

    # Step 2: Simulated detection
    if is_suspicious(filename):
        message = f" ALERT: Unauthorized construction detected in {filename}"
        print(Fore.RED + message)
        status = "UNAUTHORIZED"
    else:
        message = f" No construction detected in {filename}"
        print(Fore.GREEN + message)
        status = "AUTHORIZED"

    # Step 3: Save the result to log file
    with open(log_file, 'a') as log:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{time_now} | {filename} | {status}\n")

    # Step 4 (Optional): Show image preview
    # preview_image(filepath)  # ← uncomment to preview each image

# === DONE ===
print(f"\n All results saved in '{log_file}'. Review complete.")
