from database import Database

class BookManager:
    def __init__(self):
        self.db = Database()

    def add_book(self, kitap_adi, yazar, yayin_yili, sayfa_sayisi):
        self.db.insert({
            "kitap_adi": kitap_adi,
            "yazar": yazar,
            "yayin_yili": yayin_yili,
            "sayfa_sayisi": sayfa_sayisi
        })
        print("Kitap eklendi!")

    def list_books(self):
        books = self.db.find_all()
        if not books:
            print("Kütüphanede hiç kitap yok.")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. Kitap Adı: {book['kitap_adi']}, Yazar: {book['yazar']}, Yayın Yılı: {book['yayin_yili']}, Sayfa Sayısı: {book['sayfa_sayisi']}")

    def update_book(self, kitap_adi, yeni_yazar, yeni_yayin_yili, yeni_sayfa_sayisi):
        self.db.update({"kitap_adi": kitap_adi}, {
            "yazar": yeni_yazar,
            "yayin_yili": yeni_yayin_yili,
            "sayfa_sayisi": yeni_sayfa_sayisi
        })
        print("Kitap güncellendi!")

    def delete_book(self, kitap_adi):
        self.db.delete({"kitap_adi": kitap_adi})
        print("Kitap silindi!")
