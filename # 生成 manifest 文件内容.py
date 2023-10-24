# 生成 manifest 文件内容
manifest_content = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
"""

# 将 manifest 内容写入 manifest 文件
with open("admin_manifest.manifest", "w+") as manifest_file:
    manifest_file.write(manifest_content)

# 运行 Python 脚本以管理员权限
import os
os.system("python ScanFile.py")
