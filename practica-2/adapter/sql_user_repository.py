from entities.user import User
import uuid

class SqlUserRepository(User):
    def __init__(self):
        self.connection = None

    def find_by_email(self, email):
        print(email)
        if email == 'a@a.com':
            return User('Carlos', 'a@a.com', '1234')
        else:
            return None

    def save(self, user):
        return {"id": uuid.uuid4(),"name": user.name,"email": user.email}