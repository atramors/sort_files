import os
import shutil
import datetime

# Folder with photos

photos = "/Users/atramors/Desktop/photos/"

# Create folders named like months

for i in range(1, 13):
    os.mkdir(f"/Users/atramors/Desktop/sorted_photos/{str(i)}.2020_Fuji/")

# Loop for month creation check and moving files

for fls in os.listdir(photos):
    source = "/Users/atramors/Desktop/photos" + "/" + fls
    month_checker = datetime.datetime.fromtimestamp(os.path.getmtime(source)).month
    destination = f"/Users/atramors/Desktop/sorted_photos/{month_checker}.2020_Fuji"

    shutil.move(source, destination)
