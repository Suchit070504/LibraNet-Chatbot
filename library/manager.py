from datetime import datetime
from collections import defaultdict

LATE_FEE = 10.0

class LibraryManager:
    def __init__(self):
        self.items = {}
        self.users = {}
        self.waitlist = defaultdict(list)
        self.fines = defaultdict(float)
        self.borrow_log = defaultdict(int)

    def register_user(self, user_id:int, name:str, email:str):
        if user_id in self.users:
            return f"User {user_id} already exists"
        self.users[user_id] = {"name": name, "email": email}
        return f"User {name} registered successfully"

    def add_item(self, item):
        self.items[item.id] = item
        return f"Item {item.id} added."

    def list_items(self):
        return [str(item) for item in self.items.values()]

    def borrow_item(self, user_id:int, item_id:int, duration_days:int = 10):
        if item_id not in self.items:
            return "Item not found"
        item = self.items[item_id]
        if item.available:
            ok, msg = item.borrow_item(user_id, duration_days)
            if ok:
                self.borrow_log[item_id] += 1
            return msg
        else:
            self.waitlist[item_id].append(user_id)
            return f"Item unavailable. User {user_id} added to waitlist."

    def return_item(self, item_id:int):
        if item_id not in self.items:
            return "Item not found"
        item = self.items[item_id]
        ok, data = item.return_item()
        if not ok:
            return data
        user_id, due_date = data
        fine = 0
        if datetime.now() > due_date:
            days_late = (datetime.now() - due_date).days
            fine = LATE_FEE * days_late
            self.fines[user_id] += fine
        msg = f"Returned. Fine = Rs.{fine}"
        if self.waitlist[item_id]:
            next_user = self.waitlist[item_id].pop(0)
            self.borrow_item(next_user, item_id, 10)
            msg += f"\nAuto-issued to waitlist user {next_user}."
        return msg

    def generate_reports(self):
        most_borrowed = max(self.borrow_log, key=self.borrow_log.get, default=None)
        active = {i: str(it) for i, it in self.items.items() if not it.available}
        return {
            "Total fines (per user)": dict(self.fines),
            "Most borrowed item id": most_borrowed,
            "Active borrowings": active
        }
