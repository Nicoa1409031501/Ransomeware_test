import subprocess
   
   def get_system_info():
       p = subprocess.Popen(['system_info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stdout, stderr = p.communicate()
       system_info = stdout.decode('utf-8')
       return system_info