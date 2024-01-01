import re

   def process_xsl_file(file_path, replacement):
       with open(file_path, 'r') as file:
           xsl_content = file.read()
   
       revised_xsl_content = re.sub(r'<script>.*?</script>', f'<script>{replacement}</script>', xsl_content, flags=re.DOTALL)
   
       revised_file_path = file_path.replace('.xsl', '_revised.xsl')
       with open(revised_file_path, 'w') as file:
           file.write(revised_xsl_content)
   
   # 使用範例
   process_xsl_file('example.xsl', 'alert("This is a replaced script")')