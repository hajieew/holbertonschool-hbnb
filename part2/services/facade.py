from persistence.repository import InMemoryRepository
from models.user import User

class HBnBFacade:
    def __init__(self):
        self.repo = InMemoryRepository()

    def create_user(self, data):
        user = User(**data)
        self.repo.save("users", user)
        return user.to_dict()