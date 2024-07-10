#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count


if __name__ == "__main__":
    my_list = [1, "hello", 3, "world", 5]
    result = safe_print_list_integers(my_list, 7)
    print("Number of integers printed:", result)