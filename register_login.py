class User:
    def __init__(self, name, lastname, age) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age

    def register(self):
        print("Kayıt ol")
        register = input("Name: ")
        register2 = input("Lastname: ")
        register3 = input("Age: ")
        if register and register2 and register3:
            self.user_name = register
            self.user_lastname = register2
            self.user_age = register3
            return self.user()
        else:
            return self.register()

    def user(self):
        print("Giriş yap")
        login = input("Kullanıcı adı:")
        login2 = input("Kullanıcı soyadı:")
        login3 = input("Kullanıcı yaşı:")
        self.logName = login
        self.logLastName = login2
        self.logAge = login3
        if (
            self.user_name == self.logName
            and self.user_lastname == self.logLastName
            and self.user_age == self.logAge
        ):
            print("Hoşgeldiniz ", self.user_name)
        else:
            print("Böyle bir kullanıcı bulunamadı lütfen tekrar deneyiniz!")
            return self.user()


kullanici = User("efe", "karabulut", "19")
kullanici.register()
