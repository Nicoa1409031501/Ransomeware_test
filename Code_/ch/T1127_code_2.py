import os

def execute_msbuild_command(command):
    try:
        os.popen(command)
    except Exception as e:
        print(f"Error executing command: {e}")

command = 'msbuild /target:Build path\to\project.csproj'
execute_msbuild_command(command)