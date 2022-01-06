# Sanal Arkadaş Muubi
# -*- coding:utf-8 -*-
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


def help():
    print(">>> Yardım almak istediğiniz konu nedir")
    print(">>> (1) Sanal Arkadaş Muubi Hakkında")
    print(">>> (2) Setup veya Unninstal dosyası Hakkında")
    print(">>> (3) Muubiyi kullanma Hakkında")
    try:
        sayi = int(input("-> "))
    except ValueError:
        print(">>> Uygun bir sayı girin lütfen! [1],[2],[3]")
    if sayi == 1:
        print(">>> Sanal Arkadaş Muubi 2021 yılları arasında yapılmaya başlanıp 2022:01:07 tarihinde yayınlanan bir Yazılım Ürünüdür!")
        print(">>> Amacı insanlarla sohbet etmekdir!")
        print(">>> Hata ve görüşlerinizi belirtmek isterseniz")
        print(">>> Adres: https://github.com/rusy4li")
    elif sayi == 2:
        print(">>> Setup.py isimli dosya, programın stabil bir şekilde çalışmasına yardımcı olmak için kurulum yapar!")
        print(">>> Uninstall.py tüm dosya bileşenleriyle beraber programı sisteminizden kaldırır!")
    elif sayi == 3:
        print(">>> Muubi genelde çok konuşsada sanada bazen konuşman için hak tanıyacaktır")
        print(">>> O anlarda -> gibi bir işaret ekranda belirecek ve senden genellikle evet veya hayır veyada bir konu hakkındaki fikrini soracaktır")
    else:
        print(">>> Yardım almak istediğiniz konuyu bulamadınızmı?")
        print(">>> Adres: https://github.com/rusy4li")
    print()
    return ""


def moralduzeltme(sorgu):
    def rangetop():
        return r(1, 100)
    adeneme = rangetop()
    if (sorgu.lower() == "şaka") and (adeneme < 10):
        print(">>> 31")
    elif (sorgu.lower() == "şaka") and (adeneme >= 10):
        print(">>> AAAAAAAAAAAAAAAAAAAAA")
    elif (sorgu.lower() == "espri") and (adeneme < 10):
        print(">>> + İlişkiye ara verelim mi? – Ara vermeyelim, blok yapıp erken çıkalım.")
        print()
    elif (sorgu.lower() == "espri") and (adeneme >= 10):
        print(">>> Bill Gates neden grip olmuş? Windows açık kalmış da ondan.")
        print()
    return ""


def konuhelp(sayi):
    # Müzik konusunu seçerse
    if sayi == 1:
        print(">>> Güzel konu :)")
        print(">>> Öncelikle Hangi tür müzik dinlediğini sormak istiyorum?")
        neturmuzik = input("-> ")
        print(">>> Hmm {} güzel bir tarz".format(neturmuzik))
        print(">>> En sevdiğin şarkı ney acaba?")
        ensevdiginsarki = input("-> ")
        if ensevdiginsarki.lower() == "lovely" or ensevdiginsarki.lower() == "aden" or ensevdiginsarki.lower() == "Dursun Zaman" or ensevdiginsarki.lower() == "idfc" or ensevdiginsarki.lower() == "papparazi":
            print(">>> Bu şarkıyı bende çok seviyorum!")
        else:
            print(">>> Bu şarkıyı bilmiyorum ama sen dinlediğine göre kesin güzeldir")
        if neturmuzik.lower() == "rap":
            print(">>> En sevdiğin rapci kim?")
            ensevdiginsanatci = input("-> ")
            if ensevdiginsanatci.lower() == "contra" or ensevdiginsanatci.lower() == "joker" or ensevdiginsanatci.lower() == "allame" or ensevdiginsanatci.lower() == "no1" or ensevdiginsanatci.lower() == "ceza" or ensevdiginsanatci.lower() == "uzi" or ensevdiginsanatci.lower() == "eminem":
                print(">>> AAAAAAA")
                print(">>> {} benim en sevdiğim rapçidir!".format(
                    ensevdiginsanatci))
            else:
                print("Off")
                print("Bu rapçiyi bilmiyorum")
        else:
            print(">>> En sevdiğin şarkıcı kim?")
            ensevdiginsanatci = input("-> ")
            if ensevdiginsanatci.lower() == "manga" or ensevdiginsanatci.lower() == "taylor swift" or ensevdiginsanatci.lower() == "tom odell" or ensevdiginsanatci.lower() == "hadise" or ensevdiginsanatci.lower() == "tarkan" or ensevdiginsanatci.lower() == "müslüm gürses":
                print(">>> AAAAAAA")
                print(">>> {} benim en sevdiğim şarkıcıdır".format(
                    ensevdiginsanatci))
            else:
                print(">>> Of")
                print(">>> Üzgünüm bu şarkıcıyı bilmiyorum!")

    # Okul konusunu seçerse
    elif sayi == 2:
        print(
            ">>> Öncelikle sana okul hakkında ne düşündüğünü sormak istiyorum [iyi],[kötü]")
        okulnedusunuyon = str(input("-> "))
        if okulnedusunuyon.lower() == "iyi":
            print(">>> İyi düşündüğüne göre çalışkansın galiba")
            soyledusunuyorum = str(input("-> "))
            if soyledusunuyorum.lower() == "evet":
                print(">>> Vay be burda bir cevher var!")
            else:
                print(
                    ">>> Takma kafaya usta ya okul zaten hayatı öğrenme yeri başarılı olmayı kim umursarki")
        elif okulnedusunuyon.lower() == "kötü":
            print(">>> Okul hakkında zaten kim iyi düşünebilir ki abi çöp bir yer")
        print()
        print(">>> neyse sevdiğin bir kız varmı bari [var],[yok]")
        kizvarmi = str(input("-> "))
        if kizvarmi.lower() == "evet" or kizvarmi.lower() == "evt" or kizvarmi.lower() == "var":
            print(">>> Vaaaay")
            print(">>> Sevdiğin kızın adı ne")
            kizinadi = str(input("-> "))
            try:
                with open("data.txt", "a", encoding='utf-8') as f:
                    f.write("\n" + kizinadi)
                print(">>> Güzel ismi varmış")
            except FileNotFoundError:
                print(">>> Dosya Bulunamadı Hatası!")
        elif kizvarmi.lower() == "hayır" or kizvarmi.lower() == "yok":
            print(">>> En iyisi ustaya rahat kafa oh")

    # Aşk konusunu seçerse
    elif sayi == 3:
        print(">>> Aşktan uzak dur evlat!")

    # Hakkında konusunu seçerse
    elif sayi == 4:
        try:
            bases = open("data.txt", "r").readlines()
            ad = bases[0]
        except FileNotFoundError:
            print(">>> Dosya Bulunamadı Hatası!")
        print(">>> Merhaba "+ad)
        print(">>> Ben Muubi Version: 0.01")
        print(">>> Rusy4li Tarafından kodlanan Sanal Arkadaş'ım")
        print(">>> Yeni bir sürümüm veya özelliğim çıkarsa Rusy4li'nin Github sayfasından paylaşılıcaktır!")
        print(">>> GitHub Hesabına gitmek ister'misin? [evet],[Hayır]")
        gitIstermisin = input("-> ")
        if gitIstermisin.lower() == "evet" or gitIstermisin.lower() == "evt" or gitIstermisin.lower() == "isterim":
            os.system("start \"\" https://github.com/rusy4li")

    # Anime konusunu seçerse
    elif sayi == 5:
        print(">>> Vay be animeler hakkında konuşucağımızı hiç düşünmezdim")
        print(">>> Animeler hakkında ne düşünüyorsun")
        input("-> ")
        print(">>> Ben mükemmel olduklarını düşünüyorum")
        print(">>> En sevdiğim animeler Demon Slayer Ve Akame Ga Kill")
        print(">>> Ya senin?")
        ensevdiginanime = input("-> ")
        if ensevdiginanime.lower() == "akame ga kill" or ensevdiginanime.lower() == "charlotte" or ensevdiginanime.lower() == "zero two" or ensevdiginanime.lower() == "komi cant communicate" or ensevdiginanime.lower() == "kakegurui" or ensevdiginanime.lower() == "naruto" or ensevdiginanime.lower() == "demon slayer" or ensevdiginanime.lower() == "one punch man" or ensevdiginanime.lower() == "my hero academia" or ensevdiginanime.lower() == "tsubasa" or ensevdiginanime.lower() == "tsukimichi":
            print(">>> {} Ufff bu en sevdiğim animelerdendir".format(ensevdiginanime))
        else:
            print(">>> Aaaa bu animeyi bilmiyorum ama sen izlediğine göre kesin güzeldir")
    return ""


def tanisma():
    # Bu bölüm tanışma bölümüdür!
    print(">>> Merhaba ben rusy4li tarafından kodlanan Sanal Arkadaş Muubi pekiya sen kimsin?")
    senkimsin = input("-> ")
    try:
        f = open("data.txt", "w")
        f.write(senkimsin.strip("\n"))
        f.close()
    except FileNotFoundError:
        print(">>> Dosya Bulunamadı Hatası!")
    print(">>> Merhaba {}, tanıştığıma memnun oldum kaç yaşındasın?".format(senkimsin))
    try:
        kacyasindasin = int(input("-> "))
        try:
            f = open("data.txt", "a")
            f.write("\n"+str(kacyasindasin))
            f.close()
        except FileNotFoundError:
            print(">>> Dosya Bulunamadı Hatası!")
        print(">>> Güzel bende 1 yaşındayım")
    except ValueError:
        print(">>> Yaşını sadece sayılarla belirtirsen sevinirim")
    print(">>> Ama yaşımın 1 olduğuna bakma ben bir yapayzeka olduğum için çok akıllıyımdır\U0001F607")
    print()
    print(">>> Seni biraz daha yakından tanımak istiyorum, biraz daha kişisel soru sormamı istermisin?")
    kisiselsoru = input("-> ")
    if kisiselsoru.lower() == "evet" or kisiselsoru.lower() == "e" or kisiselsoru.lower() == "olur" or kisiselsoru.lower() == "onay":
        print()
        print(">>> Nelerden Hoşlanırsın?")
        input("-> ")
        print(
            ">>> AA çok zevkli birisin, bende bütün gün şarkı dinlemekten hoşlanırım.")
        print(">>> Peki ya en sevdiğin dizi serisi ne?")
        ensevdigindizi = input("-> ")
        if (ensevdigindizi.lower() == "witcher") or (ensevdigindizi.lower() == "the walking dead") or (ensevdigindizi.lower() == "peaky blinders") or (ensevdigindizi.lower() == "suskunlar") or (ensevdigindizi.lower() == "ragnarok") or (ensevdigindizi.lower() == "breaking bad") or (ensevdigindizi.lower() == "arcane"):
            print(">>> Vayy be gerçekten güzel bir dizi zevkin var")
        else:
            print(">>> İzlemedim ama sen sevdiğine göre kesin güzeldir\U0001F601")
        print(">>> En sevdiğin Film ney?")
        ensevdiginfilm = input("-> ")
        if (ensevdiginfilm.lower() == "avengers") or (ensevdiginfilm.lower() == "yenilmezler"):
            print(
                ">>> End Game biraz kötüydü ama genel olarak süper film serisi ya!")
        elif (ensevdiginfilm.lower() == "star wars"):
            print(">>> Klasik bir uzayda geçen film serisi")
            print(">>> Şaka şaka!")
            print(">>> Sen ciddimisin abicimya harika film serisi Star Wars")
        else:
            print(">>> İzlemedim ama sen sevdiğine göre kesin güzeldir\U0001F601")
        print(">>> En sevdiğin marvel kahramanı ney?")
        ensevdiginkahraman = input("-> ")
        if (ensevdiginkahraman.lower() == "thor"):
            print(">>> Thor çok güzel kahramanya 'Yıldırım Tanrısı'")
        elif (ensevdiginkahraman.lower() == "spiderman") or (ensevdiginkahraman.lower() == "spider man") or (ensevdiginkahraman.lower() == "örümcek adam"):
            print(">>> {} sevmeyen olurmuya çocukluğumun kahramanı!".format(
                ensevdiginkahraman))
        elif (ensevdiginkahraman.lower() == "iron man") or (ensevdiginkahraman.lower() == "ıronman") or (ensevdiginkahraman.lower() == "demir adam"):
            print(">>> {} en sevdiğim marvel kahramanlarındandır".format(
                ensevdiginkahraman))
        elif (ensevdiginkahraman.lower() == "kaptan amerika") or (ensevdiginkahraman.lower() == "captain america") or (ensevdiginkahraman.lower() == "kaptanamerika"):
            print(">>> {} en sevdiğim marvel kahramanıdır".format(
                ensevdiginkahraman))
        elif (ensevdiginkahraman.lower() == "superman") or (ensevdiginkahraman.lower() == "süpermen"):
            print(">>> Marveldan değil ama onuda çok severim")
        else:
            print(">>> Bu kahramanı bilmiyorum üzgünüm!")
        print(">>> En sevdiğin Dc kahramanı ney?")
        ensevdigindc = input("-> ")
        if (ensevdigindc.lower() == "batman"):
            print(">>> Batman'i Çok severimya çok zevklisin")
        elif (ensevdigindc.lower() == "superman") or (ensevdigindc.lower() == "süpermen") or (ensevdigindc.lower() == "super man"):
            print(">>> {} sevmeyen olurmu ya".format(ensevdigindc))
        else:
            print(">>> Bu kahramanı bilmiyorum üzgünüm!")
        print()
    elif (kisiselsoru.lower() == "hayır") or (kisiselsoru.lower() == "h"):
        print()
        print(">>> Pekala!")
    else:
        print(">>> Anlayamadım üzgünüm :(")
    print()
    print(">>> Tanışma Kaydı Oluşturuluyor")
    for i in range(3):
        time.sleep(.3)
        print('.', end='', flush=True)
        os.system("cls")
        print()


def nasilsin():
    i = 0
    while i == 0:
        try:
            bases = open("data.txt", "r")
            ad = bases.readline()
            print(">>> Tekrardan Merhaba {}".format(ad))
            bases.close()
        except FileNotFoundError:
            print(">>> Dosya Bulunamadı Hatası!")
        print(">>> Nasılsın?")
        nasilsin = str(input("-> "))
        if (nasilsin.lower() == "iyi") or (nasilsin.lower() == "çok iyi") or (nasilsin.lower() == "süper"):
            print(">>> {} olmana Çok sevindim".format(nasilsin))
            i += 1
        elif (nasilsin.lower() == "iyiyim") or (nasilsin.lower() == "çok iyiyim") or (nasilsin.lower() == "süperim"):
            print(">>> Bunu duyduğuma çok sevindim")
            i += 1
        elif (nasilsin.lower() == "kötü") or (nasilsin.lower() == "çok kötü") or (nasilsin.lower() == "üzgün"):
            print(">>> {} olmana Çok üzüldüm neden {}'sün lütfen anlat".format(
                nasilsin, nasilsin))
            input("-> ")
            i += 1
            px = 0
            while px == 0:
                print(
                    ">>> Peki ya şimdi moralini düzeltmek için ne yapabilirim? [espri],[şaka]")
                sorgu = str(input("-> "))
                if sorgu.lower() == "espri" or sorgu.lower() == "şaka":
                    moralduzeltme(sorgu)
                    px += 1
                else:
                    print(">>> Kullanabileceğiniz kelimeler! [espri],[şaka]")
        elif (nasilsin.lower() == "kötüyüm") or (nasilsin.lower() == "çok kötüyüm") or (nasilsin.lower() == "üzgünüm"):
            print(">>> bunu duyduğuma çok üzüldüm bir derdin varsa lütfen anlat dinlerim")
            input("-> ")
            i += 1
            px = 0
            while px == 0:
                print(
                    ">>> Peki ya şimdi moralini düzeltmek için ne yapabilirim? [espri],[şaka]")
                sorgu = str(input("-> "))
                if sorgu.lower() == "espri" or sorgu.lower() == "şaka":
                    moralduzeltme(sorgu)
                    px += 1
                else:
                    print(">>> Kullanabileceğiniz kelimeler! [espri],[şaka]")
        elif nasilsin.lower() == "help" or nasilsin.lower() == "help!" or nasilsin.lower() == "'help'" or nasilsin.lower() == "'help!'":
            print()
            help()
        else:
            print(
                ">>> Lütfen türkçe kelime kullanıp kullanmadığınıza dikkat edin!\nBu bölümde kullanabileceğiniz kelimeler\nOlumlu: [iyi],[iyiyim],[çok iyi],[çok iyiyim],[süper],[süperim]\nOlumsuz: [kötü],[kötüyüm],[çok kötü],[çok kötüyüm],[üzgün],[üzgünüm]")


def nekonusmak():
    i = 0
    while i == 0:
        print()
        print(">>> Bugün ne konuşmak istersin? Ben konu bulmada pek iyi değilimde!")
        print("-")
        print(">>> Şu konuları rahat bir şekilde konuşabilirsin!")
        print("-------------------------------------------------")
        print("<(1)> Müzik Konusu")
        print("<(2)> Okul Konusu")
        print("<(3)> Aşk Konusu")
        print("<(4)> Senin Hakkında")
        print("<(5)> Anime Konusu")
        print("-------------------------------------------------")
        print()
        print(">>> Şimdi konuşmak istediğin konunun yanındaki harfi yaz")
        try:
            harfalim = int(input("-> "))
            print(konuhelp(harfalim))
            i += 1
        except ValueError:
            print(
                ">>> Anlamadım! Lütfen konuşmak istediğiniz konunun yanındaki rakamı giriniz!")


def run():
    sr = os.listdir()
    if "data.txt" not in sr:
        tanisma()
    nasilsin()
    time.sleep(0.5)
    nekonusmak()
    print(">>> Ya sohbete bayıldım, arayı açma devamlı gelip yaz seni özlüyorum!")
    time.sleep(2)
    os.system("cls")
    print("Kapanıyor!")
    time.sleep(2)


# Sistem Başlatma:
datetime_modulü = datetime.datetime.now()
vakitT = datetime_modulü.strftime("%Y-%M-%D")
vakits = datetime_modulü.strftime("%I:%M:%S")
os.system("cls")
print("""
.___  ___.  __    __   __    __  .______    __  
|   \/   | |  |  |  | |  |  |  | |   _  \  |  | 
|  \  /  | |  |  |  | |  |  |  | |  |_)  | |  | 
|  |\/|  | |  |  |  | |  |  |  | |   _  <  |  | 
|  |  |  | |  `--'  | |  `--'  | |  |_)  | |  | 
|__|  |__|  \______/   \______/  |______/  |__| 
                                                
""")
print()
print("[*] help! @ {} /{}/".format(vakits, vakitT))
print()
run()
