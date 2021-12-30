class UserDAO:
    def __init__(self):
        self.users_data = ["prohibition", "warining", "indication", "directional"]    
    
    def validate(self, username):
        return username.lower() in self.users_data