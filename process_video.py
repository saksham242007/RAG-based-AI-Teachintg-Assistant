import os
import subprocess

files = os.listdir("videos")
for file in files:
    print(files)
    tutorial_number = file.split(" [")[0].split(" #")[1]
    print(tutorial_number)