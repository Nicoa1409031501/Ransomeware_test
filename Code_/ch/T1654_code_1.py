import logging

def enumerate_logs():
    log_files = ["system.log", "service.log"] # 假設系統和服務日誌文件的名稱
    for log_file in log_files:
        logger = logging.getLogger(log_file)
        logger.setLevel(logging.DEBUG)
        # 添加攻擊者感興趣的日誌文件處理器，例如FileHandler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        # 在攻擊者需要的地方，進行日誌記錄
        logger.info("This is a log message.")

        # 關閉日誌處理器
        logger.removeHandler(file_handler)
        file_handler.close()

        # 讀取並輸出日誌文件內容
        with open(log_file, "r") as file:
            data = file.read()
            print(f"Enumerating {log_file}:")
            print(data)

enumerate_logs()