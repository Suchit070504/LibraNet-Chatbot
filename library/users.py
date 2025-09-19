class User:
    def __init__(self, user_id:int, name:str, email:str):
        self.id = int(user_id)
        self.name = name
        self.email = email

    def __str__(self):
        return f"User[{self.id}]: {self.name} ({self.email})"
