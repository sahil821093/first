import json
import os

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    # Load books from file
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    self.books.append(Book(**item))

    # Save books to file
    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    # Add Book
    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_books()
        print(f"✅ '{title}' added successfully.")

    # Display Books
    def display_books(self):
        print("\n📚 Library Collection:")
        if not self.books:
            print("Library is empty.")
            return

        for i, book in enumerate(self.books, 1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i}. {book.title} by {book.author} [{status}]")

    # Search Book
    def search_book(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"🔍 {book.title} by {book.author} [{status}]")
                found = True
        if not found:
            print("❌ No matching book found.")

    # Borrow Book
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    self.save_books()
                    print(f"🎫 You borrowed '{book.title}'.")
                else:
                    print("⚠️ Book already borrowed.")
                return
        print("❌ Book not found.")

    # Return Book
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    self.save_books()
                    print(f"🔄 '{book.title}' returned successfully.")
                else:
                    print("⚠️ This book was not borrowed.")
                return
        print("❌ Book not found.")

    # Delete Book
    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"🗑️ '{book.title}' deleted successfully.")
                return
        print("❌ Book not found.")


# Main Program
def main():
    library = Library()

    while True:
        print("\n🏛️ Advanced Library Management System")
        print("1. View Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Choose option (1-7): ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            library.search_book(keyword)

        elif choice == "4":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "5":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "6":
            title = input("Enter book title to delete: ")
            library.delete_book(title)

        elif choice == "7":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
