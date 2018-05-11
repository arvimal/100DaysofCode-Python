#!/usr/bin/env python

import os


def walk_the_path(x):
    """
    Walk a specific filesystem path
    """
    for folderName, subFolders, fileNames in os.walk(x):
        print("\n- Folder name: {:<20}".format(folderName))

        for subFolder in subFolders:
            print("- - Sub-folder of {}: {}".format(folderName, subFolder))
        for fileName in fileNames:
            print("- - - File inside {}/{}/ : {}".format(folderName, subFolder, fileName))


walk_the_path("/home/vimal/00-Help/")
