One of my hobbies - photography, but it was such a pain to sort photos after my sd-card was filled (actually 2 cards with 64Gb). So I decide to automate boring process of sorting photos (actually any files can be sorted in a second) and wrote this small cli program to sort files.

This script is just create folders according to months and years of files creation and then sort and move there files from source directory.

### How to use 

1. Create folder on your Desktop(for example) at first and put your unsorted files there.
2. Open terminal and write this to see options you have (need python3 to be installed first):

   **python3 sorter.py --help** 
   
3. Just chose your names for folders 

**--unsorted_folder**
**--sorted_folder**
**--filename**

... and voila - you have folder containing folders with sorted files. 
