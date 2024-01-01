import olefile

def inject_malicious_code(docx_file):
    ole = olefile.OleFileIO(docx_file)
    vba_macros = ole.get_type_of_vbamacros()
    
    if vba_macros == olefile.VBA_UNSUPPORTED:
        print("The file does not contain VBA macros.")
    elif vba_macros == olefile.VBA_MACROS:
        # 檢測已存在的VBA macros
        current_macros = ole.listdir("macros")
        print("Existing macros:", current_macros)
    else:
        # 新增惡意VBA macros
        code = """
        Sub AutoOpen()
            MsgBox "Hello from malicious macro!"
            ' insert malicious code here
        End Sub
        """
        ole.openstream("macros/macro_name").write(code.encode())
        print("Malicious macro added.")
    
    ole.close()