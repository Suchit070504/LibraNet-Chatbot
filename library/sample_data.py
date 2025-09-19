from library.items import Book, AudioBook, EMagazine
from library.manager import LibraryManager

def load_sample_data(manager: LibraryManager):
    # users
    manager.register_user(1, "Alice", "alice@example.com")
    manager.register_user(2, "Bob", "bob@example.com")
    manager.register_user(3, "Charlie", "charlie@example.com")
    # items
    manager.add_item(Book(101, "The Great Gatsby", "F. Scott Fitzgerald"))
    manager.add_item(Book(102, "To Kill a Mockingbird", "Harper Lee"))
    manager.add_item(AudioBook(201, "Atomic Habits (Audio)", "James Clear"))
    manager.add_item(AudioBook(202, "Sapiens (Audio)", "Yuval Noah Harari"))
    manager.add_item(EMagazine(301, "Time Magazine - Sept 2025", "Time Editors"))
    manager.add_item(EMagazine(302, "National Geographic - Aug 2025", "NatGeo"))
    return manager
