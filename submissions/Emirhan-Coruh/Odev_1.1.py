name = input("Adınızı giriniz: ")
surname = input("Soyadınızı giriniz: ")
age = int(input("Yaşınızı giriniz: "))
celsius = float(input("Hava sıcaklığını giriniz: "))

fahrenheit = float(celsius * 1.8 + 32)

if age >= 18:
    print(
        f"Merhaba {name} {surname}, {age} yaşındasınız. Reşitlik durumu: Reşit."
        f" Girdiğiniz derece: {celsius}, {fahrenheit}'a eşittir."
        )
else:
    print(
        f"Merhaba {name} {surname}, {age} yaşındasınız. Reşitlik durumu: Reşit değil." 
        f" Girdiğiniz derece: {celsius}, {fahrenheit}'a eşittir."
        )

