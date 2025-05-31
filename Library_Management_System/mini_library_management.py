
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ '{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("❌ No books in library.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"📚 You borrowed '{book.title}'.")
                return
        print("❌ Book not available or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"🔁 '{book.title}' returned.")
                return
        print("❌ Book not found or wasn't borrowed.")


def main():
    library = Library()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author Name: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == '2':
            library.show_books()

        elif choice == '3':
            title = input("Enter title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            print("📕 Exiting the library system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()

