def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])