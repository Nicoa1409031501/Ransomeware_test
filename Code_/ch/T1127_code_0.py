import subprocess

def execute_msbuild_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error executing command: {e}")

command = 'msbuild /target:Build path\to\project.csproj'
execute_msbuild_command(command)