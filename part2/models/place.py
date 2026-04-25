class Place:
    def __init__(self, title, description):
        self.id = None
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }