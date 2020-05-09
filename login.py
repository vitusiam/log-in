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
            check = input("password again: ")

        user_file = open("user.txt", "a")
        user_file.write(f"{username}:{password}\n")
        user_file.close()
        user_dic[username] = password
        print("You have created a account!")

    def del_account(self):
        user_delete = input("Username: ")

    def log_in(self):
        logged_in = False
        while not logged_in:
            username = input("Your username: ")
            if username == "quit":
                logged_in = True
            elif username in user_dic:
                right_password = False
                while not right_password:
                    password = input("Your password: ")
                    if user_dic[username] == password:
                        print(f"Hi {username}, you have logged in!\n")
                        right_password = True
                        logged_in = True
                    elif password == "quit":
                        right_password = True
                    else:
                        print("Wrong password!")
            elif username not in user_dic:
                print("Wrong username")

    def look_user_info(self):
        print("\n" + open("user.txt").read())


user_dic = {}
user_logfile = open("user.txt", "r").read().splitlines()
for i, v in enumerate(user_logfile):
    new = user_logfile[i].split(":")
    user_dic[new[0]] = new[1]

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
