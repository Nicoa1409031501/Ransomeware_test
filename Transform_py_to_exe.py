import subprocess
from pathlib import Path

def convert_py_to_exe_with_path(source_directory, output_directory):
    # 定義源目錄和輸出目錄路徑
    source_dir = Path(source_directory)
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)  # 確保輸出目錄存在

    # 遍歷目錄中的 .py 文件
    for py_file in source_dir.glob("*.py"):
        # 定義 PyInstaller 命令
        command = [
            "pyinstaller",
            "--noconfirm",
            "--onefile",
            "--console",
            "--distpath",
            str(output_dir),
            str(py_file)
        ]

        # 使用 PyInstaller 轉換 .py 文件為 .exe
        subprocess.run(command)

# 使用函數並指定目錄名稱
source_directory_example = "./Code_/ch"  # 替換為實際的目錄名稱
output_directory_example = "./Executable/ch"
convert_py_to_exe_with_path(source_directory_example, output_directory_example)

