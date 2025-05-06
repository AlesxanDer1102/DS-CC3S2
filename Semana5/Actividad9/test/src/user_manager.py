class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class UserManager:
    def __init__(self,hash_service=None):

        self.users={}
        self.hash_service=hash_service
        if not self.hash_service:
            class DefaultHashService:
                def hash(self, plain_text: str) -> str:
                    return plain_text

                def verify(self, plain_text: str, hashed_text: str) -> bool:
                    return plain_text == hashed_text
            
            self.hash_service=DefaultHashService()

    def add_user(self, username, password):
        if self.user_exists(username):
            raise UserAlreadyExistsError(f"El usuario {username} ya existe.")
        hashed_pw=self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self,username):
        return username in self.users
    
    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            return UserNotFoundError(f"El usuario {username} no existe.")
        stored_hash=self.users[username]
        return self.hash_service.verify(password, stored_hash)
