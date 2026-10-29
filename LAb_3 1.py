class AptekNovbesi:
    def __init__(self):
        self.novbe = []

    def yeni_elave_et(self, ad, derman):
        musteri = {"ad": ad, "derman": derman}
        self.novbe.append(musteri)
        print(f"-> {ad} növbəyə daxil oldu (İstədiyi dərman: {derman})")

    def xidmet_goster(self):
        if len(self.novbe) > 0:
            alinan = self.novbe.pop(0)
            print(f"<- {alinan['ad']} dərmanını aldı ({alinan['derman']}) və növbədən çıxdı.")
        else:
            print("Növbə boşdur, gözləyən müştəri yoxdur.")

    def hamisini_goster(self):
        if not self.novbe:
            print("Hazırda növbədə heç kim yoxdur.")
            return
        
        print("\n HAZIRKI NÖVBƏ ")
        for i, musteri in enumerate(self.novbe, 1):
            print(f"{i}. {musteri['ad']} ---> {musteri['derman']}")
        print("--\n")

if __name__ == "__main__":
    aptek = AptekNovbesi()

    aptek.yeni_elave_et("Elmir", "Aspirin")
    aptek.yeni_elave_et("Aysel", "Parasetamol")
    aptek.yeni_elave_et("Rəşad", "Vitamin C")

    aptek.hamisini_goster()

    aptek.xidmet_goster()

    aptek.hamisini_goster()