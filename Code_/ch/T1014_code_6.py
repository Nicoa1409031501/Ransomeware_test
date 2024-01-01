import win32api
   import win32con
   
   def hide_driver(driver_name):
       win32api.SetFileAttributes(driver_name, win32con.FILE_ATTRIBUTE_HIDDEN)