#!/usr/bin/python3

import os
import shutil
import datetime
import click


@click.command()
@click.option('--unsorted_folder', default="Desktop/unsorted/",
              help='Path to find unsorted files - by default:\
                    "Desktop/unsorted/"')
@click.option('--sorted_folder', default="Desktop/sorted/",
              help='Path to put sorted files - by default:\
                    "Desktop/sorted/"')
@click.option('--filename', default="_Fuji/",
              help='Name of the folder with sorted files - by default:\
                    "_Fuji/"')
def sort_files(unsorted_folder: str, sorted_folder: str, filename: str):
    """Function to sort files"""

    # Here you can put all files need to be sorted
    unsorted_files = os.path.join(os.path.join(os.path.expanduser('~')),
                                  unsorted_folder)

    # Create folder for sorted files.
    sorted_files = os.path.join(os.path.join(os.path.expanduser('~')),
                                sorted_folder)

    try:
        os.mkdir(sorted_files)
    except FileExistsError:
        pass

    # Loop for month, year creation check.
    # Create folders named like months and moving files there.
    for fls in os.listdir(unsorted_files):
        source = unsorted_files + fls
        check = datetime.datetime.fromtimestamp(os.path.getmtime(source))
        destination = sorted_files + f"/{check.month}.{check.year}{filename}"

        try:
            os.mkdir(destination)
        except FileExistsError:
            pass
        shutil.move(source, destination)

    click.secho('All files have been sorted!', fg='green')


if __name__ == '__main__':
    sort_files()
