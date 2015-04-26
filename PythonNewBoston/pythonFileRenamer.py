import os
import re

"""
This script renamed all files in the script directory and scans for all files that starts with a digit
if the file starts for a digit ir renames the file by putting a letter 't' at the start of the filename.
"""
filesRenamed = 0
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    match = re.match('\d', string = f, flags = 0)
    if match != None:
        os.renames(f, "t"+f)
        filesRenamed += 1
        
print(str(filesRenamed) + " filesRenamed")
    