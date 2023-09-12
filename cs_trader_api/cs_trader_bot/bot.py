from steampy.client import SteamClient
from cs_trader_bot.botAuth import botAuth

class TradeBotException(Exception):
    pass

def is_logged_in(func):
    def func_wrapper(self, *args, **kwargs):
        if self.isLogged:
            return func(self, *args, **kwargs)
        raise TradeBotException("You are not logged in!")
    
class TradeBot:
    def __init__(self, auth: botAuth):
        self.auth = auth
        self.username = self.auth.get_username()
        self.password = self.auth.get_password()
        self.api_key = self.auth.get_api_key()
        self.steamguard_path = self.auth.get_steamguard_path()
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
        
        