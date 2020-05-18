class user():

    def __init__(self, username, fullname, dept, level):
        self.username = username
        self.fullname = fullname
        self.dept = dept
        self.level = level

    def describe_user(self):
        print(f'Username: {self.username.title()}')
        print(f'Fullname: {self.fullname.title()}')
        print(f'Department: {self.dept.title()}')
        print(f'Access level: {self.level}')

    def greet_user(self):
        print(f'Hello {self.username}')


new_user01 = user('teoespero', 'Teo Espero', 'Admin', 5)
new_user01.describe_user()
new_user01.greet_user()

new_user02 = user('kcadiente', 'Kelly Cadiente', 'Admin', 9)
new_user02.describe_user()
new_user02.greet_user()


