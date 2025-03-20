from apps.database import get_database, close_connection

db, client = get_database()
collection = db["books"]

def add_book():
    title = input("Kitap adı: ")
    author = input("Yazar: ")
    year = int(input("Yıl: "))
    pages = int(input("Sayfa sayısı: "))

    collection.insert_one({"title": title, "author": author, "year": year, "pages": pages})
    print("Kitap eklendi!")

def get_books():
    print("\n Kütüphanedeki Kitaplar:")
    for idx, book in enumerate(collection.find(), start=1):
        print(f"ID: {idx}, Kitap Adı: {book['title']}, Yazar: {book['author']}, Yıl: {book['year']}, Sayfa Sayısı: {book['pages']}")

def update_book():
    title = input("Güncellenecek kitap adı: ")
    new_author = input("Yeni yazar: ")
    new_year = int(input("Yeni yıl: "))
    new_pages = int(input("Yeni sayfa sayısı: "))

    collection.update_one({"title": title}, {"$set": {"author": new_author, "year": new_year, "pages": new_pages}})
    print("Kitap güncellendi!")

def delete_book():
    title = input("Silinecek kitap adı: ")
    collection.delete_one({"title": title})
    print("Kitap silindi!")

close_connection(client)
