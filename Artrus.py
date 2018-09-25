import psutil
import time
import winsound


while True:
    if "clipstudiopaint.exe" in (p.name() for p in psutil.process_iter()):
        winsound.PlaySound('C:/Windows/Media/Windows Error.wav', winsound.SND_ASYNC)
        print("stop it.")
        time.sleep(0.5)
    
