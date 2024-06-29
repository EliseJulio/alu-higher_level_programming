#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = sum(weight for score, weight in my_list)
    weighted_sum = sum(score * weight for score, weight in my_list)
    return weighted_sum / total_weight if total_weight != 0 else 0


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
