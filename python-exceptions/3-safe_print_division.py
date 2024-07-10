#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result


if __name__ == "__main__":
    a, b = 10, 2
    result = safe_print_division(a, b)
    print("Result of division:", result)
