# Öğrenci isimlerinin anahtar (key), not listelerinin değer (value) olduğu bir Sözlük (Dict).
ogrenci_notlari = {
    "Vindicta":[44, 63, 52],
    "Vyper":[86, 73, 78],
    "Shiv":[38, 67, 56]
}

# İçinde sadece benzersiz elemanları barındıran bir Küme (Set).
ogrenciler_ = {"Vindicta","Vyper","Shiv"}

# Değiştirilemez sabit verileri (okul adı ve kuruluş yılı) tuttuğumuz Demet (Tuple).
okul = ("Gazi University", 1926)

# Sözlükten 'Shiv' isimli öğrencinin not listesine gidip, 2. nota (indeks 1) ulaşıyoruz.
ikinci_not = ogrenci_notlari["Shiv"][1]
print("Öğrencinin 2. notu: ", ikinci_not)

# Sözlükteki toplam anahtar (öğrenci) sayısını len() fonksiyonu ile saydırıyoruz.
ogrenci_sayisi = len(ogrenci_notlari)
print("Öğrenci sayısı: ", ogrenci_sayisi)