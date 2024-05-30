class CreateUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user):
        return self.user_repository.save(user)
