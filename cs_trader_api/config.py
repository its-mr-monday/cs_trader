import json, os

class config:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config_data = None
        
    def load_config(self):
        with open(self.config_file, "r") as f:
            self.config_data = json.load(f)
            
    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config_data, f, indent=4)
            
    def get(self, value):
        return self.config_data[value]
    
    def set(self, value, new_value):
        self.config_data[value] = new_value
        self.save_config()
        
    def __init_config__(self):
        if os.path.isfile(self.config_file):
            self.load_config()
            return
        else:
            #Create a empty file
            with open(self.config_file, "w") as f:
                f.write("{}")
            self.load_config()