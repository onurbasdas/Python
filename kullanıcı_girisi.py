print("""
****************************
Kullanıcı Girişi Programı
****************************
""")
sys_kullanıcı_adı="onur"
sys_parola="12345"
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
            print("Parolanız:12345")
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
