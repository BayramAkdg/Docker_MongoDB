from crud import BookManager

def main():
    manager = BookManager()

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Güncelle")
        print("4. Kitap Sil")
        print("5. Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            kitap_adi = input("Kitap Adı: ")
            yazar = input("Yazar: ")
            yayin_yili = input("Yayın Yılı: ")
            sayfa_sayisi = input("Sayfa Sayısı: ")
            manager.add_book(kitap_adi, yazar, yayin_yili, sayfa_sayisi)

        elif secim == "2":
            manager.list_books()

        elif secim == "3":
            kitap_adi = input("Güncellenecek Kitap Adı: ")
            yeni_yazar = input("Yeni Yazar: ")
            yeni_yayin_yili = input("Yeni Yayın Yılı: ")
            yeni_sayfa_sayisi = input("Yeni Sayfa Sayısı: ")
            manager.update_book(kitap_adi, yeni_yazar, yeni_yayin_yili, yeni_sayfa_sayisi)

        elif secim == "4":
            kitap_adi = input("Silinecek Kitap Adı: ")
            manager.delete_book(kitap_adi)

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
