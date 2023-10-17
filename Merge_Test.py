
import tkinter as tk
import os
from pathlib import Path

def scanRecurse(baseDir):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)
def countdown(count):
    # change text in label
    # count = '01:30:00'
    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    label['text'] = '{}:{}:{}'.format(hour, minute, second)

    if second > 0 or minute > 0 or hour > 0:
        # call countdown again after 1000ms (1s)
        if second > 0:
            second -= 1
        elif minute > 0:
            minute -= 1
            second = 59
        elif hour > 0:
            hour -= 1
            minute = 59
            second = 59
        root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second)) 



root = tk.Tk()

#root.iconbitmap("../Ransomeware_test/icon.ico")
root.title('Test Ransomware')
root.geometry('500x3000')
root.resizable(False, False)
label1 = tk.Label(root, text='Hi!\n', font=('calibri', 12,'bold'))
label1.pack()

with os.popen(r"net user",'r') as text:
    text_read=text.read()
user_name=text_read.splitlines()[5].split(' ')[0]
label1 = tk.Label(root, text=user_name, font=('calibri', 12,'bold'))
label1.pack()
label1 = tk.Label(root, text='You\'re done\n', font=('calibri', 12,'bold'))
label1.pack()
label = tk.Label(root,font=('calibri', 50,'bold'), fg='white', bg='blue')
label.pack()

directory = '../' # CHANGE THIS
list_file=[]
for item in scanRecurse(directory): 
    filePath = Path(item)
    fileType = filePath.suffix.lower()
    print(filePath)
    list_file.append(str(filePath))
    
#可配合 listboxs/canvases/text 元件使用#創建 scrollbar
scrollbar = tk.Scrollbar(root)# side='right' 放入右邊
# fill='y' 向 y 軸填滿
scrollbar.pack(side='right', fill='y')#創建 listbox
listbox = tk.Listbox(root,width=50, height=40,yscrollcommand=scrollbar.set)

for item in list_file:
    listbox.insert(list_file.index(item), item)
  
listbox.pack()
# call countdown first time    
countdown('01:30:00')
# root.after(0, countdown, 5)
root.mainloop()