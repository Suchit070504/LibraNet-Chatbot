from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, item_id:int, title:str, author:str):
        self.id = int(item_id)
        self.title = title
        self.author = author
        self.available = True
        self.due_date = None
        self.borrowed_by = None

    def borrow_item(self, user_id:int, duration_days:int):
        if not self.available:
            return False, "Item unavailable"
        self.available = False
        self.borrowed_by = user_id
        self.due_date = datetime.now() + timedelta(days=duration_days)
        return True, f"Borrowed '{self.title}' until {self.due_date.date()}"

    def return_item(self):
        if self.available:
            return False, "Item was not borrowed"
        user = self.borrowed_by
        due = self.due_date
        self.available = True
        self.borrowed_by = None
        self.due_date = None
        return True, (user, due)

    def __str__(self):
        return f"[{self.id}] {self.title} by {self.author} ({'Available' if self.available else 'Borrowed'})"

class Book(LibraryItem):
    pass

class AudioBook(LibraryItem):
    def play_sample(self):
        return f"Playing sample audio from '{self.title}'..."

class EMagazine(LibraryItem):
    def archive_issue(self):
        return f"Issue '{self.title}' archived."
