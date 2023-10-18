import models


class fn_wrapper:
    def __init__(self, function, argc):
        self.function = function
        self.argc = argc

    def exec(self, args):
        if len(args) != self.argc:
            print(f"This function need exactly {self.argc} arguments")
            return
        if self.argc == 0:
            return self.function()
        return self.function(args)


def addUser(args):
    user = models.User()
    user.email = args[0]
    user.first_name = args[1]
    user.last_name = args[2]
    user.save()
    return user


def printAllUser():
    user: models.User
    for user in models.User.objects:
        print("<--------User-------->")
        print("Email \t\t:", user.email)
        print("First Name \t:", user.first_name)
        print("Last Name \t:", user.last_name)
    return True
