try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")
try:
    from random import randint as r
except ImportError:
    print(">>> 'random' modül hatası!")
try:
    import datetime
except ImportError:
    print(">>> 'datetime' modulü hatası")

# Setup Notları:
# Sisteminizde python bulunmuyor ise lütfen indirin!
# Olduğunu kontrol etmek için cmd üzerinde Python -V Yazmanız yeterlidir.
# Program windows bilgisayarlarda sorunsuz bir şekilde çalışabilicek şekilde tasarlandı

time.sleep(1)
try:
    sr = os.listdir()
    if not "main.py" in sr:
        print(">>> Klasörde main.py dosyası eksik lütfen tekrardan indirin programı!")
    elif not "uninstall.py" in sr:
        print(">>> Klasörde uninstall.py dosyası eksik lütfen tekrardan indirin programı!")
    elif not "Note.txt" in sr:
        print(">>> Klasörde Note.txt dosyası eksik lütfen tekrardan indirin programı!")
    else:
        print(">>> Dosyalar Tam, Program stabil bir şekilde çalışabilir!")
except:
    print(">>> Os modulü hata veriyor!")
time.sleep(5)
