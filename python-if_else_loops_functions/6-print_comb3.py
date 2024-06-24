#!/usr/bin/python3
print(", ".format().join(["{}{}".format(i, j) for i in range(10) for j in range(i+1, 10)]))
