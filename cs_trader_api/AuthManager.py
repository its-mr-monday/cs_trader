from db.models import User
import jwt

class TOKEN:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return self.value
    
class RefreshToken(TOKEN):
    def __init__(self, value: str):
        super().__init__(value)
        
class AuthToken(TOKEN):
    def __init__(self, value: str):
        super().__init__(value)

class AuthManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key