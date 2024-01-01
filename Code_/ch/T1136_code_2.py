import subprocess

# 創建Google Cloud帳戶的函式
def create_google_cloud_account(username, password):
    command = f"gcloud auth create-user --username={username} --password={password}"
    subprocess.run(command, shell=True)

# 呼叫函式來創建Google Cloud帳戶
create_google_cloud_account("test_user", "password123")