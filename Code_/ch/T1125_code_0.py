import cv2

def video_capture():
    # 開啟攝像頭
    cap = cv2.VideoCapture(0)

    # 設定視訊的解析度
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 檢查攝像頭是否成功打開
    if not cap.isOpened():
        print("無法開啟攝像頭")
        return

    while True:
        # 從攝像頭捕獲每一幀影像
        ret, frame = cap.read()

        # 顯示影像
        cv2.imshow("Video Capture", frame)

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) == ord('q'):
            break

    # 釋放攝像頭資源
    cap.release()

    # 關閉打開的視窗
    cv2.destroyAllWindows()