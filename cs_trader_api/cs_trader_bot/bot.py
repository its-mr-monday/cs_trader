from steampy.client import SteamClient

class TradeBotException(Exception):
    pass

def is_logged_in(func):
    def func_wrapper(self, *args, **kwargs):
        if self.isLogged:
            return func(self, *args, **kwargs)
        raise TradeBotException("You are not logged in!")
    
class TradeBot:
    def __init__(self, username: str, password: str, api_key: str, steamguard_path: str):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.steamguard_path = steamguard_path
        self.isLogged = False
        self.client = SteamClient(self.api_key)
        self.login()
        
    def login(self) -> bool:
        response = self.client.login(self.username, self.password, self.steamguard_path)
        if self.client.is_session_alive():
            self.isLogged = True
            return True
        else:
            self.logout()
            return False
        
    def logout(self) -> bool:
        self.client.logout()
        if not self.client.is_session_alive():
            self.isLogged = False
            return True
        else:
            return False
        
        