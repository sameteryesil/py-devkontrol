try:
    şifre=input("bir şifre belirleyiniz:")


    if len(şifre)<8:
        print("şifreniz en az 8 karakterden oluşmalidir tekrar deneyiniz.")
    elif " "in şifre:
        print("karakterler arasina boşluk koymadan tekrar deneyiniz.")
    else:
        print("şifreniz başariyle oluşturuldu.")
except Exception as e:
    print(f"beklenmedik bir hata oluştu: {e}")
