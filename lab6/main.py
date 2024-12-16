class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password
        print("Пароль успешно изменен.")

    def check_password(self, password):
        return self.password == password

user = UserAccount("ivandeluxe", "ivandeluxe@mail.ru", "password1")

print("Проверка пароля 'password1':", user.check_password("password1"))

user.set_password("password2")

print("Проверка пароля 'password2':", user.check_password("password2"))

print("Проверка пароля 'password1':", user.check_password("password1"))
