sys_kullanıcı_adı= input("Kullanıcının Adı:")
sys_parola= int(input("Kullanıcı Parolası:"))
bilgiler=[sys_kullanıcı_adı,sys_parola]
print("Bilgiler Kaydediliyor...")
print("*\n*\n*\n*\n*")
print("Bilgiler Kaydedildi......")
giriş_hakkı=3
while True:
    kullanıcı_adı=input("Kullanıcı Adı:")
    parola=input("Parola=")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakkı -=1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giriş_hakkı -=1
        a=input("Şifrenizi unuttuysanız 5'e tıklayınız:")
        if(a == "5"):
            print("Parolanız: {} dir.".format(sys_parola))
            break
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakkı -=1
    else:
        print("Sisteme başarıyla giriş yapıldı...")
        break
    if(giriş_hakkı == 0):
        print("Giriş Hakkınız Bitti...")
        break
print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
4. EFT/HAVALE

Programdan 'q' tuşu ile çıkabilirsiniz.

""")
bakiye  = 1000 # Bakiyemiz 1000 lira olsun.

while True:
    işlem = input("İşlemi giriniz:")

    if (işlem == "q"):
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))
        bakiye += miktar
        print("Bakiyeniz {} tldir.".format(bakiye))
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0 ):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar
        print("İşlem Tamamlandı Paranızı Alabilirsiniz....")
        print("Bakiyeniz {} tldir.".format(bakiye))
    elif(işlem == "4"):
        iban = int(input("Göndericinin IBAN'ınını giriniz:"))
        tutar = int(input("Göndericiye tutarı giriniz:"))
        if(bakiye-tutar < 0):
            print("Bu kadar para gönderemezsiniz....")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= tutar
        print("İşlem Tamamlandı Paranız Başarıyla Gönderilmiştir...")
    else:
        print("Lütfen geçerli bir işlem giriniz.")
