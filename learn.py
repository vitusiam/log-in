
password = open("user.txt", "r").read().splitlines()
dic = {}
x = "123"
y = "mars"
for i, v in enumerate(password):
    new = password[i].split(":")
    dic[new[0]] = new[1]


print(dic)
if x in dic:
    print(x)
"""for i in dic:
    if x == i:
        if dic[x] == y:
            print("right")
        else:
            print("wrong try again")
            break"""



"""this = open("user.txt", "r").read().splitlines()
x = "vitus"
y = "123"
for i, v in enumerate(this):
    new = this[i].split(":")
    print(new)

    if x == new[0] and y == new[1]:
        print("logged in!")
    else:
        print("wrong")"""
