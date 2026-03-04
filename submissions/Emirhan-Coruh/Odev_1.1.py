
# Kullanıcıdan temel kimlik ve sıcaklık bilgilerini alıyoruz.
# Yaş ile mantıksal karşılaştırma yapacağımız için 'int' (tam sayı),
# Sıcaklık küsuratlı olabileceği için 'float' (ondalıklı sayı) türüne dönüştürüyoruz.
name = input("Adınızı giriniz: ")
surname = input("Soyadınızı giriniz: ")
age = int(input("Yaşınızı giriniz: "))
celsius = float(input("Hava sıcaklığını giriniz: "))

# Alınan Celsius değerini Fahrenheit'a dönüştüren matematiksel formül
fahrenheit = float(celsius * 1.8 + 32)

# Kullanıcının 18 yaşına eşit veya büyük olma durumunu (reşitlik) kontrol ediyoruz
if age >= 18:
    # Şart sağlanıyorsa (Reşitse) ekrana yazdırılacak formatlı f-string çıktısı
    print(
        f"Merhaba {name} {surname}, {age} yaşındasınız. Reşitlik durumu: Reşit."
        f" Girdiğiniz derece: {celsius}, {fahrenheit}'a eşittir."
        )
else:
    # Şart sağlanmıyorsa (Reşit değilse) ekrana yazdırılacak formatlı f-string çıktısı
    print(
        f"Merhaba {name} {surname}, {age} yaşındasınız. Reşitlik durumu: Reşit değil." 
        f" Girdiğiniz derece: {celsius}, {fahrenheit}'a eşittir."
        )

