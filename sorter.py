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
    month_checker = datetime.datetime.fromtimestamp(os.path.getmtime(source)).month
    year_checker = datetime.datetime.fromtimestamp(os.path.getmtime(source)).year
    destination = sorted_files + f"/{month_checker}.{year_checker}_Fuji/"
    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    
    shutil.move(source, destination)
    
