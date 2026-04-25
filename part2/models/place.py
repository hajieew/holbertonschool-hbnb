from models.base import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def to_dict(self):
        return self.__dict__