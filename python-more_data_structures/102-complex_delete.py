#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = [
            key for key in a_dictionary if a_dictionary[key] == value
            ]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print(new_dict)
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print(new_dict)
