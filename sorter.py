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
    destination = {
        1: "/Users/atramors/Desktop/sorted_photos/1.2020_Fuji",
        2: "/Users/atramors/Desktop/sorted_photos/2.2020_Fuji",
        3: "/Users/atramors/Desktop/sorted_photos/3.2020_Fuji",
        4: "/Users/atramors/Desktop/sorted_photos/4.2020_Fuji",
        5: "/Users/atramors/Desktop/sorted_photos/5.2020_Fuji",
        6: "/Users/atramors/Desktop/sorted_photos/6.2020_Fuji",
        7: "/Users/atramors/Desktop/sorted_photos/7.2020_Fuji",
        8: "/Users/atramors/Desktop/sorted_photos/8.2020_Fuji",
        9: "/Users/atramors/Desktop/sorted_photos/9.2020_Fuji",
        10: "/Users/atramors/Desktop/sorted_photos/10.2020_Fuji",
        11: "/Users/atramors/Desktop/sorted_photos/11.2020_Fuji",
        12: "/Users/atramors/Desktop/sorted_photos/12.2020_Fuji"
    }
    shutil.move(source, destination[month_checker])
