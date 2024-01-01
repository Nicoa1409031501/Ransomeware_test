import psutil
   
   def hide_process(process_name):
       for proc in psutil.process_iter(['name']):
           if proc.info['name'] == process_name:
               proc.suspend()