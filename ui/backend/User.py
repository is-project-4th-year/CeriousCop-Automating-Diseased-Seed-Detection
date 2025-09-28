

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role

    def login(self, username, password):
        isLoggedIn = False

        if self.username == username and self.password == password:
            isLoggedIn = True
        return isLoggedIn