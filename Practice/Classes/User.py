class User:
    def __init__(self, first_name, last_name, **user):
        self.first_name = first_name
        self.last_name = last_name
        self.user = user
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        for key, value in self.user.items():
               print(f"{key}: {value}")

    def acessed(self, times):
         self.login_attempts = times
         
    def increment_login(self):
         self.login_attempts += 1

    def reset_login_attempts(self):
         self.login_attempts = 0


     


     