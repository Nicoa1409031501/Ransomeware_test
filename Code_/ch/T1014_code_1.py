import subprocess
   
   def get_system_info():
       result = subprocess.check_output("system_info", shell=True, text=True)
       system_info = result.stdout
       return system_info