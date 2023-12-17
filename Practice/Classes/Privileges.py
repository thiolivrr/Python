class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"Admin advantages: {self.privileges}")

    def qnt_privileges(self):
         print(f"Quantity of Privilages: {len(self.privileges)}")
         if 'fuck your mom' not in self.privileges:
              self.privileges.append('fuck your mom')