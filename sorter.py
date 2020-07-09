import os
import shutil
import datetime

# Create folder for sorted files.

files = "/Users/atramors/Desktop/unsorted/"
sorted_files = "/Users/atramors/Desktop/sorted_photos"
os.mkdir(sorted_files)


# Loop for month, year creation check.
# Create folders named like months and moving files there.

for fls in os.listdir(files):
    source = files + fls
    check = datetime.datetime.fromtimestamp(os.path.getmtime(source))
    destination = sorted_files + f"/{check.month}.{check.year}_Fuji/"
    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    
    shutil.move(source, destination)
