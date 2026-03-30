student=[]
while True:
    name=input("isim (çikiş için q giriniz): ").strip()
    if name.lower()== "q":
        break
    if not name:
        continue
    raw=input("Not (0-100): ").strip()
    if not raw.isdigit():
        continue

    grade=int(raw)
    if not(0<=grade <=100):
        continue
        
student.append((name, grade))

if student:
    student.sort(key=lambda x: x[0])
    grade = [o[1] for o in student]
    
    en_yuksek = max(grade)
    en_dusuk = min(grade)
    ortalama = sum(grade) / len(grade)
    
    print(f"Sirali Liste: {name}")
    print(f"En Yüksek Not: {en_yuksek}")
    print(f"En Düşük Not: {en_dusuk}")
    print(f"Sinif Ortalamasi: {ortalama:.2f}")
else:
    print("Hiç veri girilmedi.")