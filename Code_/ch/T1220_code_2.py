import bs4

   def process_xsl_file(file_path, replacement):
       with open(file_path, 'r') as file:
           xsl_content = file.read()
   
       soup = bs4.BeautifulSoup(xsl_content, 'lxml')
   
       for script in soup.find_all('script'):
           script.string = bs4.BeautifulSoup(f'<script>{replacement}</script>', 'lxml').string
   
       revised_file_path = file_path.replace('.xsl', '_revised.xsl')
       with open(revised_file_path, 'w') as file:
           file.write(str(soup))
   
   # 使用範例
   process_xsl_file('example.xsl', 'alert("This is a replaced script")')