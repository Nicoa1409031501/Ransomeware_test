import lief
'''
# ELF
binary = lief.parse("/usr/bin/ls")
print(binary)
# Mach-O
binary = lief.parse("/usr/bin/ls")
print(binary)
'''
# PE
binary = lief.parse(r"C:\\Users\\nick5\\output\\T\\Malware.exe")
print(binary)
print(binary.imagebase)

