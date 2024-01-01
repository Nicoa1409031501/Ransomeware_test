import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def capture_audio(filename, duration):
    fs = 44100  # 采樣率
    duration = duration  # 輸入音訊時間長度(秒)

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    wav.write(filename, fs, myrecording)

# 使用範例
capture_audio("audio.wav", 10)  # 錄製10秒音訊並存為audio.wav