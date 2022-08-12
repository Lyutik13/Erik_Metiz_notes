from privileges_admen import*

admen = Admin()
admen.privileges.show_privileges()
admen.increment_login_attempts()
admen.read_login_attempts()
print(admen.greet_user())