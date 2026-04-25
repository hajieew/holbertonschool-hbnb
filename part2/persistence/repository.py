import uuid

class InMemoryRepository:
    def __init__(self):
        self.storage = {
            "users": {},
            "places": {},
            "reviews": {}
        }

    def save(self, collection, obj):
        obj.id = str(uuid.uuid4())
        self.storage[collection][obj.id] = obj

    def get(self, collection, obj_id):
        return self.storage[collection].get(obj_id)

    def get_all(self, collection):
        return list(self.storage[collection].values())