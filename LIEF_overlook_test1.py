import lief
'''
original dlls used are  USER32.dll,KERNEL32.dll,ADVAPI32.dll

'''
binary = lief.parse("D://Github_Desktop//Ransomeware_test//Ransomeware_test//LIEF//LIEF_example_unmodified.exe")
header = binary.header
print(header)
print(binary.dos_header)
print(binary.header)
print(binary.optional_header)

# Using the abstract layer
for func in binary.imported_functions:
  print(func)

# Using the PE definition
for func in binary.imports:
  print(func)
  
for imported_library in binary.imports:
  print("Library name: " + imported_library.name)
  '''
  for func in imported_library.entries:
    if not func.is_ordinal:
      print(func.name)
    print(func.iat_address)
    '''
list_implemented=['PROPSYS.dll','GDEI32']