from user.user_model import UserModel
from user.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, user_data):
        user = UserModel(**user_data)
        self.user_dao.create_user(user)

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def delete_user(self, user_id):
        self.user_dao.delete_user(user_id)

    def update_user(self, user_data):
        user = UserModel(**user_data)
        self.user_dao.update_user(user)
