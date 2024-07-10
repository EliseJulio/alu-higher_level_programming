#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    value = "hello"
    result = safe_print_integer(value)
    print("Is value printed as integer:", result)
