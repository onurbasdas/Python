print("""***********
Beden Kitle Endeksi Hesaplama
***************
""")

a=int(input("Kilonuzu Giriniz:"))
b=float(input("Boyunuzu Giriniz:"))
bki=a/(b**2)
if(bki < 18.5):
    print("Zayıfsınız...")
elif(18.5 <= bki <25):
    print("Normal...")
elif(25 <= bki <30):
    print("Fazla Kilolu..")
else:
    print("Obez...")
