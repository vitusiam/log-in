# this is a simple log in system practice
# first create account
# store username and password
# and then log in


class User:
    def __init__(self):
        self.answer = input("\nYes to create a account, log to log-in your account: ")

    def create_account(self):
        username = input("Your username: ")
        password = input("Your password: ")
        check = input("password again: ")
        while password != check:
            print("Not the same, please check!")
            check = input("password agian: ")

        user_file = open("user.txt", "a")
        user_file.write(f"username: {username}, password: {password}\n\n")
        user_file.close()
        print("You have created a account!")

    def del_account(self):
        user_delete = input("Username:")

    def log_in(self):
        logfile = open("user.txt", "r").readlines()
        while True:
            username = input("Your username: ")
            if username == "quit":
                return False
            password = input("Your password: ")
            if username in logfile and password in logfile:
                print(f"Hi {username}, You have logged in!\n")
                return False
            elif username not in logfile or password not in logfile:
                print("Wrong password or username!")

    def look_user_info(self):
        print("\n" + open("user.txt").read())


log = True
while log:
    user = User()
    if user.answer == "yes":
        user.create_account()
    elif user.answer == "log":
        user.log_in()
    elif user.answer == "look":
        user.look_user_info()
    elif user.answer == "quit":
        answer = input("Are you sure? ")
        log = False if answer == "yes" else True
