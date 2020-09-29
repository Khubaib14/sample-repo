import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    text = "text"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Khubaib"))
