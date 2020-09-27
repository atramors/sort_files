import os
import shutil
import datetime
import pathlib

# Create folder for sorted files.


files = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/unsorted/')
# files = "/Users/atramors/Desktop/unsorted/"
# sorted_files = "/Users/atramors/Desktop/sorted_photos"
sorted_files = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/sorted_photos/')

os.mkdir(sorted_files)


# Loop for month, year creation check.
# Create folders named like months and moving files there.

for fls in os.listdir(files):
    source = files + fls
    check = datetime.datetime.fromtimestamp(os.path.getmtime(source))
    # destination = sorted_files + f"/{check.month}.{check.year}/"
    destination = sorted_files + f"/{check.month}.{check.year}_Fuji/"

    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    
    shutil.move(source, destination)
