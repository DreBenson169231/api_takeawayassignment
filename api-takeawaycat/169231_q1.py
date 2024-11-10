
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print(f"Book '{book.title}' is not borrowed by {self.name}.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")



def main():
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")

    
    member = LibraryMember("Alice", "M001")

    
    member.borrow_book(book1)
    member.borrow_book(book2)
    member.list_borrowed_books()
    member.return_book(book1)
    member.list_borrowed_books()

if __name__ == "__main__":
    main()
