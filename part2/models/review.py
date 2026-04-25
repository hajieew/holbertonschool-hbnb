class Review:
    def __init__(self, text):
        self.id = None
        self.text = text

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text
        }