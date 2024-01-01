import xml.etree.ElementTree as ET

   def process_xsl_file(file_path, replacement):
       tree = ET.parse(file_path)
       root = tree.getroot()
   
       for script in root.iter('script'):
           script.text = replacement  # 將script標籤內容替換為指定的replacement
   
       revised_file_path = file_path.replace('.xsl', '_revised.xsl')
       tree.write(revised_file_path)
   
   # 使用範例
   process_xsl_file('example.xsl', 'alert("This is a replaced script")')