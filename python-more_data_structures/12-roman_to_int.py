#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    length = len(roman_string)

    for i in range(length):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            num += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            num += roman_dict[roman_string[i]]

    return num


if __name__ == "__main__":
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
