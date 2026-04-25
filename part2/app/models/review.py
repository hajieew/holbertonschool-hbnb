from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, user, place):
        super().__init__()

        self.text = text
        self.rating = rating

        self.user = user
        self.place = place