import os
from pathlib import Path
COUNT=0
COUNT_FAIL=0
def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)
            


with os.popen(r"net user",'r') as text:
    text_read=text.read()
user_name=text_read.splitlines()[5].split(' ')[0]

directory = 'C:/Users/'+user_name # CHANGE THIS
try:
    for item in scanRecurse(directory): 
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        COUNT+=1
        print(filePath)
        print(fileType)
except:
    print("Done")
    COUNT_FAIL+=1
    
print(COUNT)
print(COUNT_FAIL)