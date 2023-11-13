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
print(binary.libraries)
print(binary.imagebase)

# Using the abstract layer
for func in binary.imported_functions:
  print(func)

# Using the PE definition
for func in binary.imports:
  print(func)

for imported_library in binary.imports:
  print("Library name: " + imported_library.name)
  for func in imported_library.entries:
    if not func.is_ordinal:
      print(func.name)
    print(func.iat_address)