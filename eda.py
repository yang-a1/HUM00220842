import os
import shutil
from datetime import datetime
import pytz

# CHANGE THIS: your folder containing the .avro files
SOURCE_DIR = r'C:\path\to\your\files'

# Optional: folder where sorted files will go
DEST_DIR = SOURCE_DIR  # You can change this if you want output elsewhere

# Time zone setup
utc = pytz.utc
est = pytz.timezone('US/Eastern')

for filename in os.listdir(SOURCE_DIR):
    if filename.endswith('.avro'):
        full_path = os.path.join(SOURCE_DIR, filename)
        mod_time = datetime.fromtimestamp(os.path.getmtime(full_path), tz=utc)
        est_time = mod_time.astimezone(est)
        date_folder = est_time.strftime('%Y-%m-%d')
        dest_path = os.path.join(DEST_DIR, date_folder)
        os.makedirs(dest_path, exist_ok=True)
        shutil.move(full_path, os.path.join(dest_path, filename))
        print(f'Moved {filename} → {date_folder}')

print('All files sorted by EST date')
