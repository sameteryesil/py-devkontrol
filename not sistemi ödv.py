
vize=float(input("vize notunuzu giriniz: "))
if vize<0 or vize>100:
    print("geçersiz not girişi")

final=float(input("final notunuzu giriniz: "))
if final<0 or final>100:
    print("geçersiz not girişi")

ort= float(vize*0.4 +final*0.6)

print(f"ortalamaniz ={ort} ")

if ort<50 and ort>=0:
    print("dersten kaldiniz")
elif ort<=60 and ort>=50:
    print("dersi şartli geçtiniz")
elif ort<70 and ort>=60:
    print("dersi D ile geçtiniz")
elif ort<80 and ort>=70:
    print("dersi C ile geçtiniz")
elif ort<90 and ort>=80:
    print("dersi B ile geçtiniz")
elif ort<=100 and ort>=90:
    print("dersi A ile geçtiniz")
else:
    print("sinirlarin dişinda bir değer aldiniz")
    
print("işlem sona erdi")    
    


