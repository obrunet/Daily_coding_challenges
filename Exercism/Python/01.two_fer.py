"""
https://exercism.io/tracks/python/exercises/two-fer
Two-fer or 2-fer is short for two for one. One for you and one for me.
Given a name, return a string with the message:
    One for X, one for me.
    Where X is the given name.
However, if the name is missing, return the string:
    One for you, one for me.
"""


def two_fer(name = "you"):
    """prints 'One for X, one for me.' in different ways
    recieves X as an argument (name)"""
    assert type(name) is str, TypeError
    if name == "": name = "'default name'" 
    print(f"fstring --> One for {name}, one for me.")
    print("str concat with + --> One for " + name + ", one for me.")


def main():
    user_response = input("What's your name?\n>>>")
    two_fer(user_response)
    two_fer()
    two_fer("")
    two_fer(123) # raise exception


if __name__ == "__main__":
    main()