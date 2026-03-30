import random

rastgeleSayi=random.randint(1,100)

print("1 ile 100 arasinda bir sayi söyleyin: ")

while True:
    tahmin=int(input("tahmininiz: "))

    if tahmin<1 or tahmin>100:
        print("kural ihlali 1 ile 100 arasinda seçiniz")
    elif tahmin < rastgeleSayi:
        print("DAHA BÜYÜK")
    elif rastgeleSayi < tahmin:
        print("DAHA KÜÇÜK") 
    else:
        print("Tebrikler cevabiniz doğru")
        break
