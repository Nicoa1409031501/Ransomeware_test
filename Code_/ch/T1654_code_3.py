from pylogbeat import pylogbeat

def enumerate_logs():
    log_files = ["system.log", "service.log"] # 假設系統和服務日誌文件的名稱
    for log_file in log_files:
        client = pylogbeat.PyLogBeatClient(host=["localhost:5044"]) # logstash主機的地址和端口
        # 從攻擊者所需的日誌文件中讀取數據
        with open(log_file, "r") as file:
            data = file.read()
            # 發送日誌數據到logstash進行解析和存儲
            client.send({"message": data})
        client.close()

        # 讀取並輸出日誌文件內容
        with open(log_file, "r") as file:
            data = file.read()
            print(f"Enumerating {log_file}:")
            print(data)

enumerate_logs()