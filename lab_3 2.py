class AvtobusNovbesi:
    def __init__(self):
        self.prioritet_novbe = [] 
        self.normal_novbe = []     

    def yeni_sernisin_elave_et(self, ad, yas):
        sernisin = {"ad": ad, "yas": yas}
        
        if yas >= 65:
            self.prioritet_novbe.append(sernisin)
            print(f"-> [Prioritet] {ad} ({yas} yaş) yaşlılar növbəsinə əlavə olundu.")
        else:
            self.normal_novbe.append(sernisin)
            print(f"-> [Normal] {ad} ({yas} yaş) ümumi növbəyə əlavə olundu.")

    def avtobusa_mindir(self):
        if len(self.prioritet_novbe) > 0:
            sernisin = self.prioritet_novbe.pop(0)
            print(f"<- [Prioritet sərnişin] {sernisin['ad']} ({sernisin['yas']} yaş) avtobusa mindi.")
        elif len(self.normal_novbe) > 0:
            sernisin = self.normal_novbe.pop(0)
            print(f"<- [Normal sərnişin] {sernisin['ad']} ({sernisin['yas']} yaş) avtobusa mindi.")
        else:
            print("Dayanacaqda gözləyən heç bir sərnişin yoxdur.")

    def siyahini_goster(self):
        print("\n--- DAYANACAQDAKI NÖVBƏNİN VƏZİYYƏTİ ---")
        
        print("1. Yaşlılar (Prioritet) növbəsi:")
        if self.prioritet_novbe:
            for i, s in enumerate(self.prioritet_novbe, 1):
                print(f"   {i}. {s['ad']} ({s['yas']} yaş)")
        else:
            print("   (Boşdur)")

        print("2. Normal növbə:")
        if self.normal_novbe:
            for i, s in enumerate(self.normal_novbe, 1):
                print(f"   {i}. {s['ad']} ({s['yas']} yaş)")
        else:
            print("   (Boşdur)")
        print("--\n")


if __name__ == "__main__":
    dayanacaq = AvtobusNovbesi()

    dayanacaq.yeni_sernisin_elave_et("Elmir", 25)
    dayanacaq.yeni_sernisin_elave_et("Fatma ", 70)
    dayanacaq.yeni_sernisin_elave_et("Aysel", 30)
    dayanacaq.yeni_sernisin_elave_et("Əhməd ", 78)

    dayanacaq.siyahini_goster()

    dayanacaq.avtobusa_mindir()
    
    dayanacaq.avtobusa_mindir()

    dayanacaq.siyahini_goster()

    dayanacaq.avtobusa_mindir()