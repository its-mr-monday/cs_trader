class botAuth:
    def __init__(self, auth_json: dict, steamguard_path: str):
        self.auth_json = auth_json
        self.steamguard_path = steamguard_path
        
    def get_username(self) -> str:
        return self.auth_json["username"]
    
    def get_password(self) -> str:
        return self.auth_json["password"]
    
    def get_api_key(self) -> str:
        return self.auth_json["api_key"]
    
    def get_steamguard_path(self) -> str:
        return self.steamguard_path