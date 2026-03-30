print("1--toplama")
print("2--çikartma")
print("3--çarpma")
print("4--bölme")

seçim=int(input("işleminizi seçiniz: "))
if seçim<=0 or seçim>=5:
    print("geçerli seçim yapiniz")
sayi1=float(input("1. sayiyi giriniz:"))
sayi2=float(input("2. sayiyi giriniz:"))

if seçim== 1:
    print(f"toplama = {sayi1 +sayi2}")
elif seçim== 2:
    print(f"çikartma = {sayi1 -sayi2}")
elif seçim== 3:
    print(f"çarpma== {sayi1 *sayi2}")
elif seçim== 4:
    if sayi2==0:
        print(" payda 0 olamaz")
    else:
        print(f"bölme== {sayi1 /sayi2}")



