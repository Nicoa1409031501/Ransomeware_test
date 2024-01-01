import subprocess
   
   def get_system_info():
       result = subprocess.run(['system_info'], capture_output=True, text=True)
       system_info = result.stdout
       return system_info