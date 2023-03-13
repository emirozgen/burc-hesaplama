gun = int(input("Doğum gününüz: "))
ay = int(input("Doğduğunuz ay ( sayısal değer olarak): "))

#Burçlar ve tarih aralıkları

burclar = {
    "Kova": (20, 1 ,18, 2),
    "Balık": (20, 1 ,18, 2),
    "Koç": (21, 3, 19, 4),
    "Boğa": (20, 4, 20, 5),
    "İkizler": (21, 5, 20, 6),
    "Yengeç": (21, 6, 22, 7),
    "Aslan": (23, 7, 22, 8),
    "Başak": (23, 8, 22, 9),   
    "Terazi": (23, 9, 22, 10),
    "Akrep": (23, 10, 21, 11),
    "Yay": (22, 11, 21, 12),
    "Oğlak": (22, 12, 19, 1)
}
#Hesap
for burc, (baslangic_gun, baslagic_ay, bitis_gun, bitis_ay) in burclar.items():
    if (gun >= baslangic_gun and ay == baslagic_ay) or (gun <= bitis_gun and ay == bitis_ay):
        print("Burcunuz:", burc)
        break
