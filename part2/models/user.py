from models.base import BaseModel

class User(BaseModel):
    def __init__(self, name, email):
        super().__init__()
        if not email:
            raise ValueError("Email required")

        self.name = name
        self.email = email
        self.places = []
        self.reviews = []

    def to_dict(self):
        return self.__dict__