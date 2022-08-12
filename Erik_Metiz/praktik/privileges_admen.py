from user import User


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
