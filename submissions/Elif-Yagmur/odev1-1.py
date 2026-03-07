isim = input("Adinizi giriniz: ")
soyad = input("Soyadinizi giriniz: ")
yas = int(input("Yasinizi giriniz: "))

C = int(input("Celcius giriniz: "))
F = C*1.8+32


resit_mi = yas >= 18



print(f"Merhaba {isim} {soyad}, {yas} yasındasiniz. Resitlik durumu: {resit_mi}. Girdiginiz {C} derece, {F:.2f} Fahrenheit'a esittir. ")