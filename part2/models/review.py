from models.base import BaseModel

class Review(BaseModel):
    def __init__(self, text, user, place):
        super().__init__()
        self.text = text
        self.user = user
        self.place = place

    def to_dict(self):
        return self.__dict__