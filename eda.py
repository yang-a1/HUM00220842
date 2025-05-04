import os
import shutil
from datetime import datetime
import pytz

# Base directory where all k folders are located
BASE_DIR = '/mnt/c/Users/amyhy/OneDrive/Desktop/HUM00220842/kerim'

# Timezone setup
utc = pytz.utc
est = pytz.timezone('US/Eastern')

# Go through each folder in BASE_DIR
for folder_name in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, folder_name)
    
    # Only process folders that start with 'k' and are directories
    if os.path.isdir(folder_path) and folder_name.startswith('k') and '_FINAL' not in folder_name:
        print(f"Processing {folder_name}...")
        final_folder = os.path.join(BASE_DIR, folder_name + '_FINAL')
        os.makedirs(final_folder, exist_ok=True)

        # Look at all .avro files in the current folder
        for file in os.listdir(folder_path):
            if file.endswith('.avro'):
                file_path = os.path.join(folder_path, file)
                
                # Get the last modified time and convert to EST
                mod_time_utc = datetime.fromtimestamp(os.path.getmtime(file_path), tz=utc)
                mod_time_est = mod_time_utc.astimezone(est)
                date_folder = mod_time_est.strftime('%Y-%m-%d')
                
                # Make dated subfolder inside *_FINAL
                dated_path = os.path.join(final_folder, date_folder)
                os.makedirs(dated_path, exist_ok=True)
                
                # Move file
                dest_path = os.path.join(dated_path, file)
                shutil.move(file_path, dest_path)
                print(f"  → Moved {file} to {folder_name}_FINAL/{date_folder}/")

print("All files reorganized by EST date.")
