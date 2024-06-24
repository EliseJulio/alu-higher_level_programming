#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))


# Example usage
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
