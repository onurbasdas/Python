print("""
****************
3 sayı girilip en büyüğünü bulma......
****************
""")
a=int(input("İlk sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
c=int(input("Üçüncü sayıyı giriniz:"))

print("En büyük sayı hesaplanıyorr......")

if(a>b and a>c):
    print("En büyük sayı {} dır.".format(a))
elif(b>a and b>c):
    print("En büyük sayı {} dir.".format(b))
elif(c>a and c>b):
    print("En büyük sayı {} dir.".format(c))
