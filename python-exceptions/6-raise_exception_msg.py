#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("This is a custom message")
    except NameError as e:
        print("Caught an exception:", e)
