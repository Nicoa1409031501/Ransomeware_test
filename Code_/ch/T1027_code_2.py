import pyminifier

def obfuscate_code(code):
    # 使用語法混淆器來混淆程式碼
    obfuscated_code = pyminifier.obfuscate(code)

    return obfuscated_code