class FindUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def find(self, email):
        return self.user_repository.find_by_email(email)