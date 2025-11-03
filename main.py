class Kitob:
    def __init__(self, nom, muallif):
        self.nom = nom
        self.muallif = muallif

    def __str__(self):
        return f"'{self.nom}' ({self.muallif})"


class Kutubxona:
    def __init__(self):
        self.kitoblar = []  # kitoblar ro'yxati

    def kitob_qosh(self, kitob):
        self.kitoblar.append(kitob)
        print(f"{kitob.nom} kutubxonaga qo‘shildi.")

    def muallif_kitoblari(self, muallif):
        natija = [kitob for kitob in self.kitoblar if kitob.muallif == muallif]
        return natija

kutubxona = Kutubxona()

kitob1 = Kitob("Alkimyogar", "Paulo Koelyo")
kitob2 = Kitob("Oq kema", "Chingiz Aytmatov")
kitob3 = Kitob("Veronika o‘lishni xohlaydi", "Paulo Koelyo")

kutubxona.kitob_qosh(kitob1)
kutubxona.kitob_qosh(kitob2)
kutubxona.kitob_qosh(kitob3)

paulo_kitoblari = kutubxona.muallif_kitoblari("Paulo Koelyo")

print("\nPaulo Koelyo kitoblari:")
for k in paulo_kitoblari:
    print("-", k.nom)
