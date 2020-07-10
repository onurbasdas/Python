print("""
*************************
Harf notu hesaplama...
*************************
""")

a=int(input("Vize1 notunuzu giriniz:"))
b=int(input("Vize2 notunuzu giriniz:"))
c=int(input("Final notunuzu giriniz:"))
toplam=((a*30)/100)+((b*30)/100)+((c*40)/100)
if(toplam>100):
    print("Geçersiz Not..")
elif(90<=toplam<=100):
    print("Tebrikler AA..")
elif (85 <= toplam < 90):
    print("Tebrikler BA..")
elif (80 <= toplam < 85):
    print("Tebrikler BB..")
elif (75 <= toplam < 80):
    print("Tebrikler CB..")
elif (70 <= toplam < 75):
    print("Fena değil CC..")
elif (65 <= toplam < 70):
    print("Çok çalışın DC..")
elif (60 <= toplam < 65):
    print("Çok çalışın DD..")
elif (55 <= toplam < 60):
    print("Kalmak üzeresiniz FD..")
elif (50 <= toplam < 55):
    print("Kaldınız FF..")
else:
    print("Seneye tekrardan bekleriz...")