class User():
    def __init__(self, first_name, last_name, age, sity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sity = sity
        self.login_attempts = 0

    def describe_user(self):
        """Read info about user"""
        print(f"\n{self.first_name} {self.last_name} \nage: {self.age} \nSity: {self.sity}")

    def greet_user(self):
        """sey Hello"""
        print(f"Hello {self.first_name} {self.last_name} !!!")

    def increment_login_attempts(self):
        """Добавляем по 1 в login_attempts"""
        self.login_attempts += 1

    def read_login_attempts(self):
        print(f"Колличество входа в систему : {self.login_attempts}")

    def reset_login_attempts(self):
        if self.login_attempts >= 0:
            self.login_attempts = 0


class Privileges():  # для 9.8 создали новый класс для атребута Admen
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей", "Admin царь разрешенно всё!!!"]

    def show_privileges(self):
        print(f"Что можeт admen :")
        for privilege in self.privileges:
            print(f"{privilege.capitalize()}")


class Admin(User):
    def __init__(self, first_name='admin', last_name='admin', age='admin', sity='admin'):
        super().__init__(first_name, last_name, age, sity)
        self.privileges = Privileges()
    #     self.privileges = ["разрешено добавлятьсообщения", "разрешено удалять пользователей",
    #                        "разрешено банить пользователей", "Admin царь разрешенно всё!!!"]
    #
    # def show_privileges(self):
    #     print(f"Что можeт {self.first_name} :")
    #     for privilege in self.privileges:
    #         print(f"{privilege}")