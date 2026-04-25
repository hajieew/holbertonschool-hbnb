class HBnBFacade:
    def __init__(self):
        self.users = {}

    # USER METHODS
    def create_user(self, user):
        self.users[user.id] = user
        return user

    def get_all_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)