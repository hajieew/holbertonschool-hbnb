class User:
    def __init__(self, name, email):
        if not email:
            raise ValueError("Email is required")
        self.id = None
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }