import cv2
import subprocess

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

    # 設定FFmpeg的參數
    out_filename = "video_capture.mp4"
    codec = "mp4v"
    fps = 30.0

    # 取得視訊的寬度和高度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 使用FFmpeg開始錄製影片
    command = ['ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo',
               '-s', f"{width}x{height}", '-pix_fmt', 'bgr24', '-r',
               f"{fps}", '-i', '-', '-an', '-vcodec', f"{codec}",
               f"{out_filename}"]

    ffmpeg_proc = subprocess.Popen(command, stdin=subprocess.PIPE)

    while True:
        # 從攝像頭捕獲每一幀影像
        ret, frame = cap.read()

        # 顯示影像
        cv2.imshow("Video Capture", frame)

        # 寫入影像到FFmpeg進程
        ffmpeg_proc.stdin.write(frame.tostring())

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) == ord('q'):
            break

    # 釋放攝像頭資源
    cap.release()

    # 關閉打開的視窗
    cv2.destroyAllWindows()

    # 等待FFmpeg進程完成並關閉
    ffmpeg_proc.stdin.close()
    ffmpeg_proc.wait()