def Hello(to):
    print("Hello,", to)

name = input("what's your name?").strip().title()
Hello(name)


def Hello(to ="World!"):
    print("Hello,", to)


name = input("what's your name").strip().title()
Hello(name)


Hello()