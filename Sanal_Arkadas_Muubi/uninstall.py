try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")

time.sleep(0.5)
print("Dosyalar siliniyor!!")
sorgu = input("Kabul ediyormusunuz? [Evet],[Hayır] -> ")
if sorgu.lower() == "evet":
    os.remove("main.py")
    os.remove("Note.txt")
    os.remove("setup.py")
    os.remove("data.txt")
    os.remove("uninstall.py")
    os.rmdir("Sanal_Arkadas_Muubi")
    time.sleep(1)
elif sorgu.lower() == "hayır":
    os.system("cls")
else:
    os.system("cls")
