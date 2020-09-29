import requests


def greet(who_to_greet):
    text = "text"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Khubaib"))
print(greet("Dude"))