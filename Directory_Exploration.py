import os
from pathlib import Path

def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)
            



directory = '../' # CHANGE THIS
try:
    for item in scanRecurse(directory): 
        filePath = Path(item)
        fileType = filePath.suffix.lower()
except:
    12