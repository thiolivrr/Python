from User import User
from Privileges import Privileges

class Administrator(User):
    def __init__(self, first_name, last_name, **user):
          super().__init__(first_name, last_name, **user)
          self.privileges = Privileges()

        