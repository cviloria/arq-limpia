from abc import abstractmethod
class UserRepository:
    @abstractmethod
    def get_user(self, user_id):
        pass