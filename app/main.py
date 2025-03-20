from crud import add_book, get_books, update_book, delete_book
from utility import show_menu

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            add_book()
        elif choice == "2":
            get_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
