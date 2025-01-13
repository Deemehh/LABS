class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменен.")

    def check_password(self, password):
        return self.__password == password


def create_user_account():
    print("Создание аккаунта")
    username = input("Введите имя пользователя: ")

    while True:
        email = input("Введите электронную почту: ")
        if "@" in email:
            break
        else:
            print("Это не почта, попробуйте еще раз")

    password = input("Введите пароль: ")
    return UserAccount(username, email, password)


user = create_user_account()

input_password = input("Введите пароль для проверки: ")
print("Проверка пароля:", user.check_password(input_password))

new_password = input("Введите новый пароль: ")
user.set_password(new_password)

input_password = input("Введите пароль для проверки: ")
print("Проверка пароля:", user.check_password(input_password))
