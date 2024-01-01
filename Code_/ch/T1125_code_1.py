import pygame
import pygame.camera

def video_capture():
    # 初始化Pygame
    pygame.init()
    pygame.camera.init()

    # 取得可用的攝像頭列表
    cameras = pygame.camera.list_cameras()

    if not cameras:
        print("找不到可用的攝像頭")
        return

    # 開啟第一個攝像頭
    cam = pygame.camera.Camera(cameras[0], (640, 480))

    # 開始攝影
    cam.start()

    # 初始化視窗
    screen = pygame.display.set_mode((640,480))

    while True:
        # 擷取攝像頭的影像
        image = cam.get_image()

        # 顯示影像
        screen.blit(image, (0,0))
        pygame.display.flip()

        # 檢查是否按下 'q' 鍵退出迴圈
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # 停止攝影
                    cam.stop()
                    pygame.quit()
                    return