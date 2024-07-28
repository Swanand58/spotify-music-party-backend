import uuid
from datetime import datetime

class User:
    def __init__(self, id, name, email, password, username):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.username = username
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.name} ({self.username})"

    def __repr__(self):
        return f"{self.name} ({self.username})"
    
    