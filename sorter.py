# !/bin/python3

import os
import shutil
import datetime

# Create folder for sorted files.

unsorted_files = os.path.join(os.path.join(os.path.expanduser('~')),
                              'Desktop/unsorted/')
sorted_files = os.path.join(os.path.join(os.path.expanduser('~')),
                            'Desktop/sorted_photos/')

os.mkdir(sorted_files)


# Loop for month, year creation check.
# Create folders named like months and moving files there.

for fls in os.listdir(unsorted_files):
    source = unsorted_files + fls
    check = datetime.datetime.fromtimestamp(os.path.getmtime(source))
    destination = sorted_files + f"/{check.month}.{check.year}_Fuji/"

    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    shutil.move(source, destination)
