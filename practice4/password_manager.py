class Password_manager:
    def __init__(self, list_of_passwords=[]):
        self.passwords = list_of_passwords
    def get_password(self):
        return self.passwords[len(self.passwords)-1]
    def set_password(self, new_password):
        if new_password not in self.passwords:
            self.passwords.append(new_password)
        else:
            return f"You already used {new_password} as your password"
    def is_correct(self, password):
        if str(password) == str(self.passwords[len(self.passwords)-1]):
            return True
        else:
            return False

passw = ["abcde", "fghij", 'klmnop', "qrstuvwxyz", "10265ghj"]

azat = Password_manager(passw)
print(azat.get_password())
azat.set_password("650290AA")
print(azat.get_password())
enter_passw = input()
print(azat.is_correct(enter_passw))

