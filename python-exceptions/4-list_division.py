#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)
    return new_list


if __name__ == "__main__":
    my_list_1 = [10, 20, 30, "hello"]
    my_list_2 = [2, 5, 0, 3]
    result = list_division(my_list_1, my_list_2, 5)
    print("Result of list division:", result)
