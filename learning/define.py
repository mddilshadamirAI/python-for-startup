def main():
    name = input("what's your name? ").strip().title()
    hello(name)
    hello()

def hello(to="World"):
    print("hello,", to)
   
main()


def main():
    x = int(input("What's x?"))
    print("x squared is:" , square(x))


def square(n):
    return n * n
main()